# adsb-reliability-tools


All the modules to process the data were written in python. In order to utilize them  you need to supply a csv file formatted according to your customized input.
The modules use other libraries that are built in python and some others you need to install them.

You need to install **geopy** and **pyModeS** libraries to run the code. 
Once you provide the module an input csv file, it will process it and store the result in **Sqlite DB**. 
The aim of outputing files in Sqlite is the capability it gives to manupilate the data.

### Converting Json to Sqlite Database:


In order to convert **Json** file to Sqlite database file, you need to first to convert it from **Avro** format to **Json** then supply it to this module for conversion.

### find_position_messages

Thi module filters the position messages from other Adsb messges and store them in a database. 


### messages_average

This module calculates the average messages sent by an airplanes in 5 seconds.


### find_loss

This module finds which message have been lost based on the distance of the plane from the receiversensor.

### number_of_planes_when_receiving_packet

This module calculates the number of distinct aircraft that exists in the transmission range of a sensor in certain time interval.
You need to provide the position messages received and the general file that contains all messages.




