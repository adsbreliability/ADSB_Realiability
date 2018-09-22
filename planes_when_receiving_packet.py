def planes_when_receiving_packet(lossfile,searchfile,interval_time):
    import sqlite3



    conn = sqlite3.connect('data.sqlite')
    sql="CREATE TABLE data (icao text,lostMessage text,sensor real,meanTime real ,planes real,distance real)"

    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    sql = "INSERT INTO data VALUES (?,?,?,?,?,?);"
    with open(lossfile , 'r') as lossfile:
        with open(searchfile , 'r') as datafile:
            datafile.readline()
            lossfile.readline()
            lines = datafile.read().splitlines()

            last_start_position = 0
            for line in lossfile:

                row = line.replace('\n', '').split(',')
                lostMessage = row[0]
                distance = row[1]
                meanTime = float(row[2])
                sensor = row[3]
                lowerbound = meanTime - interval_time
                upperbound = meanTime + interval_time
                planes = set()
                firstimeInWindow = True
                # check number of airplanes
                for i in range(last_start_position, len(lines)):

                    rw = lines[i].replace('\n', '').split(',')
                    icao = rw[0]
                    messagereceived = rw[1]
                    time = float(rw[2])
                    if time >= lowerbound and time <= upperbound:
                        planes.add(icao)
                        if firstimeInWindow:
                            firstimeInWindow = False
                            last_start_position = i

                    if time > upperbound:
                        break
                args = (icao, lostMessage, sensor, meanTime, len(planes), distance)
                c.execute(sql, args)
            conn.commit()
            conn.close()









