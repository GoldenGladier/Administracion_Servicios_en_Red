import time
import rrdtool
from getSNMP import consultaSNMP

# CPU0 = "1.3.6.1.2.1.25.3.3.1.2.6"
CPU0 = "1.3.6.1.2.1.25.3.3.1.2.5"
RAMTOTAL = "1.3.6.1.2.1.25.2.3.1.5.2"
RAMUSO = "1.3.6.1.2.1.25.2.3.1.6.2"
OCTINPUT = "1.3.6.1.2.1.2.2.1.10.11"
OCOUTPUT = "1.3.6.1.2.1.2.2.1.16.11" 
SPEED = "1.3.6.1.2.1.2.2.1.5.11"

rrdpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/RRD'
carga_CPU0 = 0
 
COMUNITY = 'OmarAA'
IP = '192.168.100.31'
# IP = '172.100.87.189'

while 1:
    # print("Carga CPU: " + consultaSNMP(COMUNITY, IP, CPU0))
    carga_CPU0 = int( consultaSNMP(COMUNITY, IP, CPU0))  
    RAMT = int( consultaSNMP(COMUNITY, IP, RAMTOTAL) )
    RAMU = int( consultaSNMP(COMUNITY, IP, RAMUSO) )
    OCIN = int( consultaSNMP(COMUNITY, IP, OCTINPUT) )
    OCOUT = int( consultaSNMP(COMUNITY, IP, OCOUTPUT) )
    CSPEED = int( consultaSNMP(COMUNITY, IP, SPEED) )

    PORRAM = int((RAMU * 100)/ RAMT)
    RED = int((OCIN+OCOUT*8*100)/CSPEED)

    valorC = "N: " + str(carga_CPU0)
    valorR = "N: " + str(PORRAM) 
    valorTI = "N: " + str(RED)
    
    print ("CPU: " + valorC + " - RAM: " + valorR + " - RED: " + valorTI)
    # " - RAM USE: " + str(RAMU) + "/" + str(RAMT) +

    rrdtool.update(rrdpath + '/DB_cargaCPU0.rrd', valorC)
    rrdtool.dump(rrdpath + '/DB_cargaCPU0.rrd', rrdpath + '/DB_cargaCPU0.xml')

    rrdtool.update(rrdpath + '/DB_RAM.rrd', valorC)
    rrdtool.dump(rrdpath + '/DB_RAM.rrd', rrdpath + '/DB_RAM.xml')

    rrdtool.update(rrdpath + '/DB_NETWORK.rrd', valorC)
    rrdtool.dump(rrdpath + '/DB_NETWORK.rrd', rrdpath + '/DB_NETWORK.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
