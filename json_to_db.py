def json_to_db(target_file):
    import json
    import sqlite3

    # Creating the database

    conn = sqlite3.connect('Data.sqlite')

    sql = "create table data  (" \
          "sensorType real, sensorLatitude real, sensorLongitude real, sensorAltitude real, timeAtServer real, timeAtSensor real, timestamp real, rawMessage" \
          "text, real sensorSerialNumber, real RSSIPacket, real RSSIPreamble, real SNR, real confidence);"

    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    sql = "INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"


    with open(target_file, 'r') as f:
            for line in f:
                object = json.loads(line)
                sensorType = object['sensorType']
                try:
                    sensorLatitude = object['sensorLatitude']['double']
                except:
                    sensorLatitude = None
                try:
                    sensorLongitude = object['sensorLongitude']['double']
                except:
                    sensorLongitude = None
                try:
                    sensorAltitude = object['sensorAltitude']['double']
                except:
                    sensorAltitude = None
                timeAtServer = object['timeAtServer']
                try:
                    timeAtSensor = object['timeAtSensor']['double']
                except:
                    timeAtSensor = None
                try:
                    timestamp = object['timestamp']['double']
                except:
                    timestamp = None
                rawMessage = object['rawMessage']
                sensorSerialNumber = object['sensorSerialNumber']
                try:
                    RSSIPacket = object['RSSIPacket']['double']
                except:
                    RSSIPacket = None
                RSSIPreamble = object['RSSIPreamble']
                SNR = object['SNR']
                confidence = object['confidence']

                args = (
                sensorType, sensorLatitude, sensorLongitude, sensorAltitude, timeAtServer, timeAtSensor, timestamp,
                rawMessage, sensorSerialNumber, RSSIPacket, RSSIPreamble, SNR, confidence)
                c.execute(sql, args)

            conn.commit()

            conn.close()


