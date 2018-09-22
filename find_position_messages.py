def find_possition_messages(target_file):
    import pyModeS as pms
    sensors = {'80596247': [47.4462937382234, 8.21036883309448, 438.847942268372],
               '80602915': [47.40017, 8.63068, 1413.0],
               '81483681': [47.0363, 8.32408, 1564.0],
               '81491016': [47.0559, 8.48391, 5843.0],
               '954778341': [47.1742, 8.5247, 0.0],
               '956151203': [47.1922290641956, 8.85319593600312, 416.746004776001],
               '1805967060': [47.2482931862621, 8.52975659072399, 2051.0]}
    import sqlite3  #
    # module to find positions messages
    conn = sqlite3.connect('time_icao.sqlite')
    sql = "INSERT INTO data VALUES (?,?,?,?,?,?,?);"
    c = conn.cursor()
    with open(target_file, 'r') as file:
        line = file.readline();
        for line in file:
            row = line.replace('\n', '').split(',')
            icao = row[0]
            msg = row[1]
            time = row[2]
            sensorSerialNumber = row[3]
            lat = sensors[sensorSerialNumber][0]
            lon = sensors[sensorSerialNumber][1]
            alt = sensors[sensorSerialNumber][2]
            typecode = pms.adsb.typecode(msg)
            if typecode >= 9 and typecode <= 18:

                try:
                    (flightLat, flightLong) = pms.adsb.position_with_ref(msg, float(lat), float(lon))
                    flightAlt = pms.adsb.altitude(msg)
                    args = (icao, msg, time, flightLat, flightLong, flightAlt, sensorSerialNumber)
                except:
                    pass

                c.execute(sql, args)

    conn.commit()
    conn.close()











