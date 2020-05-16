from input_output_tool import *
from linkage_container import LinkageContainer
from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
linkage_list = LinkageContainer()

# Connection the database
print("Welcome to behavioral pattern cluster analysis system!")

dbname = read_a_string("Enter the dbname: ")
user = read_a_string("Enter the database user: ")
if dbname == '' or user == '':
    dbname = 'leozhang'
    user = 'postgres'
password = read_a_string("Enter the password(If there is no password, please press enter): ")
host = read_a_string("Enter the host(press enter for the default value)： ")
port = read_a_string("Enter the port(press enter for the default port 5432)： ")
sqlTool.connection_sql(dbname, user, password=password, host=host, port=port)
print("Connection database succeeded!")

# Find all dates
build_day_container(sqlTool, dayDeck)

# Build for sensor list
print("There are 4 kinds of sensor data, which one do you want to analyze?")
print("1.the PIR sensor \n"
      "2.the lumen sensor \n"
      "3.the temperature sensor \n"
      "4.the power sensor \n"
      "5.all of them")
kind = read_a_number(1, 5, False)
if kind == 1:
    build_pir_list(sqlTool, dayDeck.get_list_of_day())

elif kind == 2:
    build_lumen_list(sqlTool, dayDeck.get_list_of_day())

elif kind == 3:
    build_temp_list(sqlTool, dayDeck.get_list_of_day())

elif kind == 4:
    build_power_list(sqlTool, dayDeck.get_list_of_day())

else:
    build_pir_list(sqlTool, dayDeck.get_list_of_day())
    build_lumen_list(sqlTool, dayDeck.get_list_of_day())
    build_temp_list(sqlTool, dayDeck.get_list_of_day())
    build_power_list(sqlTool, dayDeck.get_list_of_day())

# Exec hierarchical clustering algorithm
print("Preparing exec hierarchical clustering")
print("please enter the the desired number of clusters(max cluster) for "
      "presentation the common pattern(\033[1;35m recommended 1 to 5 \033[0m).")
common_pattern_list, the_corresponding_level_of_max_cluster = \
    hierarchical_clustering(dayDeck, linkage_list, read_a_number(1, None, False))

# Presentation
print(
    "Please enter the level of critical distance(DT), you can press Enter to input the default value(0.7*max(Z[:,2])).")
print("Hint:\033[1;35m The corresponding level\033[0m of critical distance of "
      "the desired number of clusters is \033[1;35m" + str(the_corresponding_level_of_max_cluster) + "\033[0m")
color_threshold = read_a_number(0, None, True, number_type='float')
data_visualization(dayDeck,
                   linkage_list.linkage_list,
                   common_pattern_list,
                   the_corresponding_level_of_max_cluster,
                   color_threshold=color_threshold)

sqlTool.close_connect()
