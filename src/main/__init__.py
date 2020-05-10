from linkage_container import LinkageContainer
from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
linkage_list = LinkageContainer()

print("Welcome to behavioral pattern cluster analysis system!")

dbname = input("Enter the dbname: ")
user = input("Enter the database user: ")
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
while True:
    kind = int(input("Enter: "))
    if kind == 1:
        build_pir_list(sqlTool, dayDeck.get_list_of_day())
        break
    elif kind == 2:
        build_lumen_list(sqlTool, dayDeck.get_list_of_day())
        break
    elif kind == 3:
        build_temp_list(sqlTool, dayDeck.get_list_of_day())
        break
    elif kind == 4:
        build_power_list(sqlTool, dayDeck.get_list_of_day())
        break
    elif kind == 5:
        build_pir_list(sqlTool, dayDeck.get_list_of_day())
        build_lumen_list(sqlTool, dayDeck.get_list_of_day())
        build_temp_list(sqlTool, dayDeck.get_list_of_day())
        build_power_list(sqlTool, dayDeck.get_list_of_day())
        break
    else:
        print('\033[1;31m Please enter a number from 1 to 5. \033[0m')

print("Preparing exec hierarchical clustering")
max_cluster = input("please enter the max cluster for "
                    "presentation the common pattern(\033[1;35m recommended 1 to 3 \033[0m):")
common_pattern_list = hierarchical_clustering(dayDeck, linkage_list, int(max_cluster))
data_visualization(dayDeck, linkage_list.linkage_list, common_pattern_list)
