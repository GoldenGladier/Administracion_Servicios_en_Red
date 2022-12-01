import sys
import rrdtool
import time
import datetime
from  Notify import send_alert_attached, send_alert_multiple_processors_attached
from datetime import datetime

rrdpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/RRD'
imgpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/IMG'
# UMBRAL = str(50)

def generarGraficaCPU(last):
    tiempo_final = int (last)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath + "/CPU0.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=Cpu load",
                            '--lower-limit', '0',
                            '--upper-limit', '100',
                            "--title=Monitoreo del CPU - Detección de umbrales",
                            "DEF:cargaCPU0=" + rrdpath + "/DB_cargaCPU0.rrd:cargaCPU0:AVERAGE",

                            "AREA:cargaCPU0#FB2576:Carga del CPU0",

                             "HRULE:45#10A19D:Umbral  45%",
                             "HRULE:50#FED049:Umbral  50%",
                             "HRULE:90#9C254D:Umbral  90%",
                        )

    except Exception as e:
        print('Error al momento de graficar CPU: '+ str(e))

def generarGraficaRAM(last):

    tiempo_final = int (last)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath+"/RAM.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=RAM load",
                            '--lower-limit', '0',
                            '--upper-limit', '100',
                            "--title=Monitoreo de la RAM - Detección de umbrales",
                            "DEF:RAM="+rrdpath+"/DB_RAM.rrd:RAM:AVERAGE",

                            "AREA:RAM#FB2576:Carga de la RAM",

                             "HRULE:45#10A19D:Umbral  45%",
                             "HRULE:50#FED049:Umbral  50%",
                             "HRULE:90#9C254D:Umbral  90%",
                        )

    except Exception as e:
        print('Error al momento de graficar RAM: '+ str(e))     

def generarGraficaRED(last):

    tiempo_final = int (last)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath + "/RED.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=Uso de Red load",
                            '--lower-limit', '0',
                            '--upper-limit', '200',
                            "--title=Monitoreo de la RED - Detección de umbrales",
                            "DEF:NETWORK=" + rrdpath + "/DB_NETWORK.rrd:NETWORK:AVERAGE",

                            "AREA:NETWORK#FB2576:Carga de la RED",

                             "HRULE:140#10A19D:Umbral  140",
                             "HRULE:150#FED049:Umbral  150",
                             "HRULE:180#9C254D:Umbral   180",
                        )

    except Exception as e:
        print('Error al momento de graficar RED: '+ str(e))           

alertaCPU = [True, True, True]
alertaRAM = [False, False, False]
alertaRED = [False, False, False]

while (1):

    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "/DB_cargaCPU0.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato=ultima_actualizacion['ds']["cargaCPU0"]

    now = datetime.now()
    date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + " - " + str(now.hour)  + ':' + str(now.minute)

    if dato > 45 and alertaCPU[0]:
        print("Sobrepasa el umbral del CPU (45%) [" + date + "]")
        time.sleep(5)
        generarGraficaCPU(int(timestamp))
        send_alert_attached("ALERTA: Agente sobrepaso el primer umbral (45%) del CPU  [" + date + "]", "El CPU ha pasado el 45%","CPU0")
        alertaCPU[0] = False

    if dato > 50 and alertaCPU[1]:
        print("Sobrepasa el umbral del CPU (50%) [" + date + "]")
        time.sleep(5)
        generarGraficaCPU(int(timestamp))
        send_alert_attached("ALERTA: Agente sobrepaso el segundo umbral (50%) del CPU [" + date + "]", "El CPU ha pasado el 50%","CPU0")
        alertaCPU[1] = False

    if dato > 90 and alertaCPU[2]:
        print("Sobrepasa el umbral del CPU (90%) [" + date + "]")
        time.sleep(5)
        generarGraficaCPU(int(timestamp))
        send_alert_attached("ALERTA: Agente sobrepaso el tercer umbral (90%) del CPU [" + date + "]", "El CPU ha pasado el 90%","CPU0")
        alertaCPU[2] = False
    
    # time.sleep(20)

    ultima_actualizacionR = rrdtool.lastupdate(rrdpath + "/DB_RAM.rrd")
    timestampR=ultima_actualizacionR['date'].timestamp()
    datoR=ultima_actualizacionR['ds']["RAM"]

    now = datetime.now()
    date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + " - " + str(now.hour)  + ':' + str(now.minute)

    if datoR > 90 and alertaRAM[2]:
        print("Sobrepasa el umbral de la RAM (90%)")
        time.sleep(30)
        generarGraficaRAM(int(timestampR))
        send_alert_attached("ALERTA: Agente sobrepaso el tercer umbral (90%) de la RAM [" + date + "]", "La RAM ha pasado el 90%","RAM")
        alertaRAM[2] = False
    if datoR > 50 and alertaRAM[1]:
        print("Sobrepasa el umbral de la RAM (50%)")
        time.sleep(30)
        generarGraficaRAM(int(timestampR))
        send_alert_attached("ALERTA: Agente sobrepaso el segundo umbral (50%) de la RAM ALERTA: Agente s" + date + "]", "La RAM ha pasado el 50%","RAM")
        alertaRAM[1] = False

    if datoR > 45 and alertaRAM[0]:
        print("Sobrepasa el umbral de la RAM (45%)")
        time.sleep(30)
        generarGraficaRAM(int(timestampR))
        send_alert_attached("ALERTA: Agente sobrepaso el primer umbral (45%) de la RAM [" + date + "]", "La RAM ha pasado el 45%","RAM")
        alertaRAM[0] = False



    # time.sleep(20)

    ultima_actualizacionRED = rrdtool.lastupdate(rrdpath + "/DB_NETWORK.rrd")
    timestampRED=ultima_actualizacionRED['date'].timestamp()
    datoRED=ultima_actualizacionRED['ds']["NETWORK"]

    now = datetime.now()
    date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + " - " + str(now.hour)  + ':' + str(now.minute)

    if datoRED > 30 and alertaRED[0]: #140
        print("Sobrepasa el umbral de RED")
        time.sleep(30)
        generarGraficaRED(int(timestampRED))
        send_alert_attached("ALERTA: Agente sobrepaso el primer umbral de RED[" + date + "]", "La RED ha pasado el 30Mb","RED")
        alertaRED[0] = False

    if datoRED > 35 and alertaRED[1]: #150
        print("Sobrepasa el umbral de RED")
        time.sleep(30)
        generarGraficaRED(int(timestampRED))
        send_alert_attached("ALERTA: Agente sobrepaso el segundo umbral de RED[" + date + "]", "La RED ha pasado el 35Mb","RED")
        alertaRED[1] = False

    if datoRED > 45 and alertaRED[2]:
        print("ALERTA: Agente sobrepasa el umbral de RED")
        time.sleep(30)
        generarGraficaRED(int(timestampRED))
        send_alert_attached("ALERTA: Agente sobrepaso el tercer umbral de RED [" + date + "]", "La RED ha pasado el 45Mb","RED")
        alertaRED[2] = False

    time.sleep(30)
    