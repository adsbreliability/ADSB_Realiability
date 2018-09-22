def find_loss( target_file):
    import geopy.distance as dist
    import sqlite3

    # This module finds out if a packet was lost or not using the distance module from geopy libarary
    # The file provided is a csv file and contains the msg and the sensors that received it plus their Lat and Long

    conn = sqlite3.connect('Data.sqlite')
    sql = "create table Distance (msg text,distance real,sensor real);"

    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    sql = "INSERT INTO Distance VALUES (?,?,?);"


    with open(target_file, "r") as file:
            sensors = {'80596247.0': [301.322168509665, 47.4462937382234, 8.21036883309448],
                       '80602915.0': [318.014887285749, 47.40017, 8.63068],
                       '81483681.0': [360.704772889835, 47.0363, 8.32408],
                       '81491016.0': [625.148353865216, 47.0559, 8.48391],
                       '954778341.0': [376.15805596962, 47.1742, 8.5247],
                       '956151203.0': [269.653750744384, 47.1922290641956, 8.85319593600312],
                       '1805967060.0': [361.565517932316, 47.2482931862621, 8.52975659072399]}
            for line in file:
                row = line.replace('\n').split(',')
                msg = row[0]
                receivedSensors = row[3].split("-")

                for sensor, sensorInfo in sensors.iteritems():
                    distance = (dist.vincenty((float(row[1]), float(row[2])), (sensorInfo[1], sensorInfo[2])).km)

                    if sensor not in receivedSensors and distance < sensorInfo[0]:
                        args = (msg, distance, sensor)
                        c.execute(sql, args)
            conn.commit()
            conn.close()







