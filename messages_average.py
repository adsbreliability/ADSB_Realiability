
def messages_average(target_file):
    class Icao:
        def __init__(self, icao):
            self.Icao = icao
            self.packets = []

        def addPackets(self, packet):
            self.packets.append(packet)

    class IcaoAverage:
        def __init__(self, icao, mean):
            self.icao = icao
            self.mean = mean

    with open(target_file, 'r')as file:
        firstline = file.readline()
        oldicaoname = firstline.split(",")[2]
        listofIcao = []
        object = Icao(oldicaoname)
        object.addPackets(firstline)
        for line in file:
            currenticaoname = line.split(",")[2]
            if currenticaoname != oldicaoname:
                listofIcao.append(object)
                object = Icao(currenticaoname)
                object.addPackets(line)
                oldicaoname = currenticaoname

            else:
                object.addPackets(line)
        listofIcao.append(object)

    numberOfPackets = []
    for icao in listofIcao:
        lst = icao.packets
        MessagesforSpecificIcao = []
        for i in range(0, len(lst)):
            endInterval = float(lst[i].split(",")[1]) + 5
            j = i
            packetsInTheWindow = 0
            MessageInTheWindow = []
            currentTime = float(lst[j].split(",")[1])
            while currentTime <= endInterval and j < len(lst):
                msg = lst[j].split(",")[0]
                if msg not in MessageInTheWindow:
                    MessageInTheWindow.append(msg)
                    packetsInTheWindow += 1

                j += 1
                if j >= len(lst):
                    break
                currentTime = float(lst[j].split(",")[1])
            if packetsInTheWindow >= 5:
                MessagesforSpecificIcao.append(packetsInTheWindow)
        # print MessagesforSpecificIcao
        mean = 0
        if len(MessagesforSpecificIcao) != 0:
            mean = sum(MessagesforSpecificIcao) / float(len(MessagesforSpecificIcao))
        numberOfPackets.append(IcaoAverage(icao.Icao, mean))

    with open('meanTimeResult.csv', 'w') as file:

        for item in numberOfPackets:
            file.write(str(item.icao) + "," + str(item.mean) + "\n")

