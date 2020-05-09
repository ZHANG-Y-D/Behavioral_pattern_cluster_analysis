from linkage_container import LinkageContainer
from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
linkage_list = LinkageContainer()

build_day_container(sqlTool, dayDeck)

build_pir_list(sqlTool, dayDeck.get_list_of_day())
build_lumen_list(sqlTool, dayDeck.get_list_of_day())
build_temp_list(sqlTool, dayDeck.get_list_of_day())
build_power_list(sqlTool, dayDeck.get_list_of_day())

hierarchical_clustering(dayDeck, linkage_list)
data_visualization(dayDeck, linkage_list.linkage_list)
