# Behavioral pattern cluster analysis system

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
- Error
In case of a failed access to the database, an error message will be showed, and the program will exit automatically.
![Error](https://github.com/ZHANG-Y-D/Behavioral_pattern_cluster_analysis/blob/master/documentation/maredown_pictures/data_base_error.png)

- Warning
Warning message will not cause the program to exit. There are two cases of warning
 * Warning for appliance. In the dataset, there are 9 appliances. If other appliances appear, this warning will raise, you can ignore it if you don’t care the new appliance.
 * Warning for signals: if some sensor non has signals in the whole day, this warning will appear

For example
   
   '''
   Warning: Room 9 No lumen signal received at 2020-04-01
   Warning: Room 10 No lumen signal received at 2020-04-01
   Warning: Room 9 No lumen signal received at 2020-04-02
   Warning: Room 10 No lumen signal received at 2020-04-02
  '''
  
It means that not have lumen signal at room 9 at whole day of 2020-04-01, maybe the sensor has not been installed on this day, so if you sure the dataset is right, you can ignore it.
