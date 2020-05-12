from linkage_container import LinkageContainer
from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
linkage_list = LinkageContainer()


def read_a_number(down, up, if_can_be_empty):
    while True:
        number = input("Enter: ")
        if if_can_be_empty is True and number == '':
            return None
        try:
            number = int(number)
        except ValueError:
            print("Please enter a number.")
            continue
        if number < down:
            print("Please enter a number larger than " + str(down) + ".")
            continue
        elif up is not None and number > up:
            print("Please enter a number smaller than " + str(up) + ".")
            continue
        return number


print("Welcome to behavioral pattern cluster analysis system!")

dbname = input("Enter the dbname: ")
user = input("Enter the database user: ")
if dbname == '' or user == '':
    dbname = 'leozhang'
    user = 'postgres'
password = input("Enter the password(If there is no password, please press enter): ")
host = input("Enter the host(press enter for the default value)： ")
port = input("Enter the port(press enter for the default port 5432)： ")
sqlTool.connection_sql(dbname, user, password=password, host=host, port=port)
print("Connection database succeeded!")

build_day_container(sqlTool, dayDeck)

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

print("Preparing exec hierarchical clustering")
print("please enter the the desired number of clusters(max cluster) for "
      "presentation the common pattern(\033[1;35m recommended 1 to 5 \033[0m).")
common_pattern_list, the_corresponding_level_of_max_cluster = \
    hierarchical_clustering(dayDeck, linkage_list, read_a_number(1, None, False))

print("Please enter the level of critical distance, you can press Enter to input the default value.")
print("Default value = 0.7*max(Z[:,2]), and\033[1;35m the corresponding level\033[0m of critical distance of "
      "the desired number of clusters is " + str(the_corresponding_level_of_max_cluster))
color_threshold = read_a_number(0, None, True)
data_visualization(dayDeck,
                   linkage_list.linkage_list,
                   common_pattern_list,
                   the_corresponding_level_of_max_cluster,
                   color_threshold=color_threshold)

sqlTool.close_connect()
