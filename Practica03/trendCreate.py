import rrdtool

rrdpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/RRD'

# Averiguar OID de procesadores --> snmpwalk -v1 -c OmarAA 192.168.100.31 1.3.6.1.2.1.25.3.3
OID = "1.3.6.1.2.1.25.3.3.1.2."
# processors = ["5", "6", "7", "8", "9", "10", "11", "12"]

# ds = []
# for processor in processors:
#     ds.append("DS:{}:GAUGE:60:0:100".format('processor_' + processor))
#     print("DS: " + OID + processor)

# print(ds)


def makeDB(name):
    print("Created /DB_" + name + ".rrd")
    ret = rrdtool.create(rrdpath + "/DB_" + name + ".rrd",
                        "--start",'N',
                        "--step",'30', # Cada 60 segundos grafica 1 punto     
                        # -------- DATA SOURCES --------
                        # "DS:CPUload:GAUGE:60:0:100", # GAUGE --> Cada 60 seg. toma todos los datos y les aplica una funcion
                        "DS:" + name + ":GAUGE:60:0:100",
                        # ------------------------------
                            # 1440 --> Guarda 24 horas con resolucion de 1 minuto
                            # 600 ---> Guarda 5 horas con resolucion de 30 segundos                     
                        "RRA:AVERAGE:0.5:1:600")
    if ret:
        print (rrdtool.error())

makeDB('cargaCPU0')
makeDB('RAM')
makeDB('NETWORK')