from proximity_matrix import ProximityMatrix


def build_day_container(sql_tool, day_deck):
    value = sql_tool.query_from_sql("select date(t_from) as date from person_position group by date order by date;")
    value.pop(0)
    value.pop()  # Because the data on the first and last day are not complete, exclude
    position_of_date = 1

    for date in value:
        day_deck.add_date(date[0], position_of_date)
        position_of_date += 1


def build_pir_list(sql_tool, list_of_day_deck):
    for day_container in list_of_day_deck:
        day_container.init_pir_list(2880)
        date_curr = day_container.get_date().strftime("%Y-%m-%d")
        query_result = sql_tool.query_from_sql("select id_room, t_from, t_to from person_position "
                                               "where date(t_from)='" + date_curr + "' or date(t_to)='"
                                               + date_curr + "'order by t_from, t_to, id_room;")
        for tuple_curr in query_result:
            day_container.add_pir_value(tuple_curr)

        # print("-------------------------------")
        # print(day_container.get_pir_list())
        day_container.fill_black_for_pir_list()
        # print(day_container.get_pir_list())


def build_lumen_list(sql_tool, list_of_day_deck):
    for day_container in list_of_day_deck:
        day_container.init_lumen_list(288)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_room, sd.value, sd.timestamp FROM sensor as se "
                                               "join stream_data as sd on se.id_sensor = sd.id_sensor "
                                               "WHERE se.id_sensor_type = 3 and date(timestamp) = '"
                                               + date_curr + "' order by se.id_room, timestamp;")
        for tuple_curr in query_result:
            day_container.add_lumen_value(tuple_curr)

        # print("-------------------------------")
        # for ele in day_container.get_lumen_list():
        #     print(ele)
        day_container.fill_black_for_list("lumen")
        # for ele in day_container.get_lumen_list():
        #     print(ele)


def build_temp_list(sql_tool, list_of_day_deck):
    for day_container in list_of_day_deck:
        day_container.init_temp_list(72)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_room, sd.value, sd.timestamp FROM sensor as se "
                                               "join stream_data as sd on se.id_sensor = sd.id_sensor "
                                               "WHERE se.id_sensor_type = 4 and date(timestamp) = '"
                                               + date_curr + "' order by se.id_room, timestamp;")
        for tuple_curr in query_result:
            day_container.add_temp_value(tuple_curr)

        # print("-------------------------------")
        # for ele in day_container.get_temp_list():
        #     print(ele)
        day_container.fill_black_for_list("temp")
        # for ele in day_container.get_temp_list():
        #     print(ele)


def build_power_list(sql_tool, list_of_day_deck):
    appliances_sampling_interval = [30, 120, 300, 1200, 120, 120, 120, 120, 120]
    for day_container in list_of_day_deck:
        day_container.init_power_list(appliances_sampling_interval)
        date_curr = day_container.get_date().strftime('%Y-%m-%d')
        query_result = sql_tool.query_from_sql("SELECT se.id_sensor, sd.value, se.threshold, sd.timestamp "
                                               "FROM sensor as se join stream_data as sd "
                                               "on se.id_sensor = sd.id_sensor WHERE se.id_sensor_type = 5 "
                                               "and date(timestamp) = '"
                                               + date_curr + "'order by se.id_sensor, timestamp;")
        for tuple_curr in query_result:
            day_container.add_power_value(tuple_curr, appliances_sampling_interval)

        # print("-------------------------------")
        # for ele in day_container.get_power_list():
        #     print(ele)
        day_container.fill_black_for_list("power")
        # for ele in day_container.get_power_list():
        #     print(ele)


def proximity_matrix_generator(list_of_day_deck, proximity_matrix):
    proximity_matrix.init_proximity_matrix(len(list_of_day_deck))
    for index_x, day_container in enumerate(list_of_day_deck):
        for index_y, later_day_container in enumerate(list_of_day_deck[index_x + 1:]):
            proximity_matrix.add_distance(index_x, index_y, day_container, later_day_container)

    for ele in proximity_matrix.get_proximity_matrix():
        print(ele)



