from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()

build_day_container(sqlTool, dayDeck)
build_pir_list(sqlTool, dayDeck.get_list_of_day())
build_lumen_list(sqlTool, dayDeck.get_list_of_day())
print(dayDeck.get_list_of_day()[0].get_pir_list())
