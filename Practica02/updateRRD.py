import time
import rrdtool
from getSNMP import consultaSNMP

def updateRRD(IP, comunity, dataSources):
    print("Monitoreando agente (proceso en segundo plano)...\n\n")
    while 1:
        # Se sacarian 5 datos (1 para cada datasource)
        # tcp_in_segments = int(
        #     consultaSNMP(comunity,IP, '1.3.6.1.2.1.6.10.0'))

        # valor = "N:" + str(tcp_in_segments) + ':' + str(tcp_out_segments)
        valor = "N:"
        for atribute, oid in dataSources.items():
            tmp = int( consultaSNMP(comunity, IP, oid) )
            # print(atribute + ": " + str(tmp) )
            valor = valor + str(tmp) + ":"
        valor = valor[:-1]
        # print (valor)
        rrdtool.update('DBs/database_' + IP + '.rdd', valor)
        rrdtool.dump('DBs/database_' + IP + '.rdd', 'DBs/database_' + IP + '.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)