from process_controller import *
from proximity_matrix import ProximityMatrix
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
proximity_matrix = ProximityMatrix()

build_day_container(sqlTool, dayDeck)
build_pir_list(sqlTool, dayDeck.get_list_of_day())
build_lumen_list(sqlTool, dayDeck.get_list_of_day())
build_temp_list(sqlTool, dayDeck.get_list_of_day())
build_power_list(sqlTool, dayDeck.get_list_of_day())

proximity_matrix_generator(dayDeck.get_list_of_day(), proximity_matrix)
