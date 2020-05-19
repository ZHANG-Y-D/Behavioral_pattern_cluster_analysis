# Behavioral pattern cluster analysis system



## Introduction

This is a python program to execute cluster analysis for people's daily living behavior at home, it used agglomerative hierarchical clustering to cluster which days are similar and present the common pattern for similar days.
We named this program as “Behavioral Pattern Cluster Analysis System (BPCAS)”, For user, it’s very user-friendly cause it has a Command-line Interface (CLI), this CLI will guide the user to execute the right input and present the program running log. For operator, the code is very readable and maintainable.
This documentation has two parts, Usage and Architecture of BPCAS.
For the first part, the usage is a guidebook for “getting started”, we recommend that you read this section carefully before using, especially the dataset part, because BPCAS is designed for the special dataset, “ensuring that the dataset is valid” is the key to the correct operation of this program.
For the second part, if you only care about how to use it and don’t care about the internal implementation, you can ignore this part directly. This part is the architecture of BPCAS, it details the architecture of the program, from execution process to algorithm details, from data extraction to data presentation, they will be illustrated and explained as clearly & simple as possible.
So, here we go.



## Usage

The source code is under the path src/main, first of all, build the third-party libraries, and then run “ __init__.py ” file with python 3.6. The src/test is unit test codes.



### Command-line Interface (CLI)

The CLI is very user-friendly, you just have to insert the values following the instructions, and in case of an error, you'll be notified.

![CLI1](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/interactive1.png)

![CLI2](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/interactive2.png)



### Input

#### Dataset

##### Connection dataset

There are 5 arguments.

 * dbname: compulsory, the name of database.

 * database user: compulsory, the database administrator.

 * password: optional, the database password, if there is no password, just press Enter.

 * host: optional, the database host, press Enter for “localhost”

 * port: optional, the database port, press Enter for default port 5432
If the input fields have some problems, the program will exit automatically, please check the connection info and run it again.



##### Check if the dataset is applicable

###### Three tables are necessaries.

* person_position: This table stored the PIR sensor’s signals, we will extract dates from
id_room, t_from, t_to attributes.

* sensor: This table stored configuration information of all sensors, we will extract dates
from id_room, id_sensor, id_sensor_type, threshold attributes.

* stream_data: This table stored the Lumen Temperature and Power sensor’s signals,
we will extract dates from value, id_sensor, timestamp attributes. 



###### Determine the id of these three sensors in “sensor_type” table like this

| id   |      name      |
|:--------:|:-------------:|
| 3 | Light |
| 4 |   Temperature   |
| 5 | Energy |



###### Be sure appliances’ id in “sensor” table like this

| ID_SENSOR   |      NAME      |
|:--------:|:-------------:|
| 24 | Microonde |
| 26 |   Televisione   |
| 28 | HC2 Power |
| 32 | Frigorifero |
| 34 |   Forno   |
| 36 | Lavatrici |
| 45 | Serra A |
| 148 |   Lavastoviglie   |
| 150 | PC |





##### Dataset Error & Warning



###### Error

In case of a failed access to the database, an error message will be showed, and the program will exit automatically.
![Error](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/data_base_error.png)



###### Warning

Warning message will not cause the program to exit. There are two cases of warning
 * Warning for appliance. In the dataset, there are 9 appliances. If other appliances appear, this warning will raise, you can ignore it if you don’t care the new appliance.
 * Warning for signals: if some sensor non has signals in the whole day, this warning will appear

For example

``Warning: Room 9 No lumen signal received at 2020-04-01``
``Warning: Room 10 No lumen signal received at 2020-04-01``
``Warning: Room 9 No lumen signal received at 2020-04-02``
``Warning: Room 10 No lumen signal received at 2020-04-02``

It means that not have lumen signal at room 9 at whole day of 2020-04-01, maybe the sensor has not been installed on this day, so if you sure the dataset is right, you can ignore it.



#### The desired number of clusters

This value also called max_cluster, it will decide the number of common patterns to present in the output.



#### The level of critical distance(DT)

This value will decide the final cluster in the dendrogram, the default value is 0.7*max ( max distance of all cluster ). Of course, we recommend using the corresponding value of max_cluater and the CLI will give you a hint.

For example:
![input_for_max_cluster](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/input_for_max_cluster.png)





### Output



#### Dendrogram

In the dendrogram, except dendrogram, it also will present max_cluster and the level of critical distance(DT).
All days below the level of critical distance(DT) will be treated as same cluster,
And the desired number of clusters ( max cluster ) will present those cluster it passed.

For example:
![dendrogram](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/dendrogram.png)

As mentioned above, DT decides to dendrogram, and max_cluster decide the number of common pattern or abnormal day, if these two values are in a same interval, the common pattern and abnormal day will perfectly present the content of dendrogram.



#### Calendar

![Calendar](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/calendar.png)
This figure will present which days in the same cluster, the color is same at dendrogram, the abnormal days will color in blue.



####  Common pattern

For lumen signals, the darker the color, the darker the light and vice versa.
For temperature signals, the redder color means higher temperature and vice versa.
For power signals, the red color means on, the gray means off. But for “Serra A” and “Frigorifero” the redder color means larger power and vice versa.

![common_pattern1](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/common_pattern1.png)

![common_pattern2](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/common_pattern2.png)

![common_pattern3](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/common_pattern3.png)



#### Abnormal day

![abnormal_day](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/abnormal_day.png)