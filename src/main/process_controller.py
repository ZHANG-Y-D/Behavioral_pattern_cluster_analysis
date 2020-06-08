import copy
from proximity_matrix import ProximityMatrix
import data_visualization as dv
from input_output_tool import *


def connection_database(sql_tool):
    dbname = read_a_string("Enter the dbname: ")
    user = read_a_string("Enter the database user: ")

    # For test
    if dbname == '' or user == '':
        dbname = 'leozhang'
        user = 'postgres'

    password = read_a_string("Enter the password(If there is no password, please press enter): ")
    host = read_a_string("Enter the host(press enter for the default value)： ")
    port = read_a_string("Enter the port(press enter for the default port 5432)： ")
    sql_tool.connection_sql(dbname, user, password=password, host=host, port=port)
    print("Connection database succeeded!")


def select_sensor_and_build(sql_tool, list_of_day):
    print("There are 4 kinds of sensor data, Which sensors do you want to analyze?")
    print("\033[1;35mHint:\033[0m You can enter the sensor combination, like ac or abcd.")
    print("a.the PIR sensor \n"
          "b.the lumen sensor \n"
          "c.the temperature sensor \n"
          "d.the power sensor ")
    kind = read_a_string(hint_string='Enter: ', must_include='abcd')
    if 'a' in kind:
        build_pir_list(sql_tool, list_of_day)

    if 'b' in kind:
        build_lumen_list(sql_tool, list_of_day)

    if 'c' in kind:
        build_temp_list(sql_tool, list_of_day)

    if 'd' in kind:
        build_power_list(sql_tool, list_of_day)


def build_day_container(sql_tool, day_deck):
    value = sql_tool.query_from_sql("SELECT date(t_from) as date FROM person_position group by date order by date;")

    for i, date in enumerate(value):
        day_deck.add_date(date[0], i)

    day_deck.init_num_of_clustering(len(day_deck.get_list_of_day()))


def build_pir_list(sql_tool, list_of_day_deck):
    print("Building PIR sensor list...")
    for day_container in list_of_day_deck:
        day_container.init_pir_list(2880)
        date_curr = day_container.get_date().strftime("%Y-%m-%d")
        query_result = sql_tool.query_from_sql("SELECT id_room, t_from, t_to FROM person_position "
                                               "WHERE date(t_from)='" + date_curr + "' or date(t_to)='"
                                               + date_curr + "'order by t_from, t_to, id_room;")
        for tuple_curr in query_result:
            day_container.add_pir_value(tuple_curr)

        day_container.fill_black_for_pir_list()

        # print(day_container.get_pir_list())


def build_lumen_list(sql_tool, list_of_day_deck):
    print("Building Lumen sensor list...")
    for day_container in list_of_day_deck:
        day_container.init_lumen_list(288)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_room, sd.value, sd.timestamp FROM sensor as se "
                                               "join stream_data as sd on se.id_sensor = sd.id_sensor "
                                               "WHERE se.id_sensor_type = 3 and date(timestamp) = '"
                                               + date_curr + "' order by se.id_room, timestamp;")
        for tuple_curr in query_result:
            day_container.add_lumen_value(tuple_curr)

        day_container.fill_black_for_list("lumen")

        # for ele in day_container.get_lumen_list():
        #     print(ele)


def build_temp_list(sql_tool, list_of_day_deck):
    print("Building temperature sensor list...")
    for day_container in list_of_day_deck:
        day_container.init_temp_list(72)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_room, sd.value, sd.timestamp FROM sensor as se "
                                               "join stream_data as sd on se.id_sensor = sd.id_sensor "
                                               "WHERE se.id_sensor_type = 4 and date(timestamp) = '"
                                               + date_curr + "' order by se.id_room, timestamp;")
        for tuple_curr in query_result:
            day_container.add_temp_value(tuple_curr)

        day_container.fill_black_for_list("temp")

        # for ele in day_container.get_temp_list():
        #     print(ele)


def build_power_list(sql_tool, list_of_day_deck):
    print("Building power sensor list...")
    for day_container in list_of_day_deck:
        appliances_sampling_interval = day_container.appliances_sampling_interval
        day_container.init_power_list(appliances_sampling_interval)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_sensor, sd.value, se.threshold, sd.timestamp "
                                               "FROM sensor as se join stream_data as sd "
                                               "on se.id_sensor = sd.id_sensor WHERE se.id_sensor_type = 5 "
                                               "and date(timestamp) = '"
                                               + date_curr + "'order by se.id_sensor, timestamp;")
        for tuple_curr in query_result:
            day_container.add_power_value(tuple_curr, appliances_sampling_interval)

        day_container.fill_black_for_list("power")
        #
        # for ele in day_container.get_power_list():
        #     print(ele)


def proximity_matrix_generator(list_of_day_deck, proximity_matrix):
    proximity_matrix.init_proximity_matrix(len(list_of_day_deck))
    for index_x, day_container in enumerate(list_of_day_deck):
        for index_y, later_day_container in enumerate(list_of_day_deck[index_x + 1:]):
            proximity_matrix.add_distance(index_x, index_y, day_container, later_day_container)

    # print(proximity_matrix.get_proximity_matrix())
    # for ele in proximity_matrix.get_proximity_matrix():
    #     print(ele)


def hierarchical_clustering(day_deck, linkage_list):
    print("Preparing exec hierarchical clustering")
    print("please enter the the desired number of clusters(max cluster) for "
          "presentation the common pattern.")
    max_cluster = read_a_number(down=1, if_can_be_empty=False)

    print("Executing hierarchical clustering...")
    proximity_matrix = ProximityMatrix()
    common_pattern_list = []
    the_corresponding_level_of_max_cluster = 0

    # Limit of max cluster value
    if max_cluster >= len(day_deck.dayDeck):
        common_pattern_list = copy.deepcopy(day_deck.dayDeck)
        the_corresponding_level_of_max_cluster = 1
    if max_cluster == 0:
        max_cluster = 1

    index = 0
    next_index = -1
    while len(day_deck.dayDeck) > 1:

        # Generate thw proximity matrix
        proximity_matrix_generator(day_deck.get_list_of_day(), proximity_matrix)

        # Calculate min value and get min coordinate, form: [x_axis, y_axis, min_value]
        min_coordinate_and_minvalue = ProximityMatrix.find_min_coordinate(proximity_matrix.proximity_matrix)

        # Pop those two days from day deck
        first_day = day_deck.dayDeck.pop(min_coordinate_and_minvalue[0])
        second_day = day_deck.dayDeck.pop(min_coordinate_and_minvalue[0] + min_coordinate_and_minvalue[1])

        # cluster those two days
        day_deck.clustering(first_day, second_day)

        # Add it to linkage list
        linkage_list.add_linkage_element(first_day.date_num,
                                         second_day.date_num,
                                         min_coordinate_and_minvalue[2],
                                         len(first_day.clustered_date) + len(second_day.clustered_date))

        if len(day_deck.dayDeck) == max_cluster:
            common_pattern_list = copy.deepcopy(day_deck.dayDeck)
            # The corresponding level of critical distance of the desired number of clusters
            the_corresponding_level_of_max_cluster = min_coordinate_and_minvalue[2]
            next_index = index + 1

        if index == next_index:
            the_corresponding_level_of_max_cluster = \
                (the_corresponding_level_of_max_cluster + min_coordinate_and_minvalue[2]) / 2

        index += 1

    # print(linkage_list.linkage_list)
    return common_pattern_list, the_corresponding_level_of_max_cluster + 0.1


def data_visualization(day_deck,
                       linkage_list,
                       common_pattern_list,
                       the_corresponding_level_of_max_cluster):

    print("Please enter the level of critical distance(DT), "
          "you can press Enter to input the default value(0.7*max(Z[:,2])).")
    print("Hint:\033[1;35m The corresponding level\033[0m of critical distance of "
          "the desired number of clusters is \033[1;35m" + str(the_corresponding_level_of_max_cluster) + "\033[0m")

    color_list = dv.presentation_dendrogram(day_deck,
                                            linkage_list,
                                            the_corresponding_level_of_max_cluster,
                                            color_threshold=read_a_number(down=0, number_type='float'))
    dv.presentation_calendar(common_pattern_list, color_list)
    dv.presentation_common_pattern(common_pattern_list, day_deck.dayDeck[0].appliances_sampling_interval)
    dv.show_all_figure()
