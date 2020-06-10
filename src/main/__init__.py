"""
    Version: v2.0
    Date: 2020/06/07
    Author: Zhang Yuedong
    Version update:
        1.Fixed the color bug.
        2.Built a selector for the sensor in CLI system.
        3.Combine input values 'max_cluster' and 'the_corresponding_level_of_max_cluster',
          Now only need to enter the max_cluster value.
        4.Built a shortcut for modify appliances sampling interval.
"""
"""

3.Preview dendrogram
6.Separate present an appliance in a new figure

"""
from linkage_container import LinkageContainer
from process_controller import *
from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()
linkage_list = LinkageContainer()
"""
Default values of appliances_sampling_interval.
Order Microonde: Default 30s
      Televisione: Default 120s
      HC2 Power: Default 300s
      Frigorifero: Default 1200s 
      Forno: Default 120s
      Lavatrici: Default 120s 
      Serra A: Default 120s 
      Lavastoviglie: Default 120s 
      PC: Default 120s
"""
appliances_sampling_interval = [30, 120, 300, 1200, 120, 120, 120, 120, 120]


print("Welcome to behavioral pattern cluster analysis system!")

# Connection the database
connection_database(sqlTool)

# Find all dates
build_day_container(sqlTool, dayDeck)

# Build for sensor list
select_sensor_and_build(sqlTool, dayDeck.get_list_of_day(), appliances_sampling_interval)

# Exec hierarchical clustering algorithm
common_pattern_list, the_corresponding_level_of_max_cluster = hierarchical_clustering(dayDeck, linkage_list)

# Presentation
data_visualization(dayDeck,
                   linkage_list.linkage_list,
                   common_pattern_list,
                   the_corresponding_level_of_max_cluster,
                   appliances_sampling_interval)

# Close connection
sqlTool.close_connect()
