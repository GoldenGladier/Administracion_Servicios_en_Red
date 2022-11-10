#!/usr/bin/env python
import rrdtool
import os

def createRRD(IP, dataSources):
    if ( not os.path.exists('DBs/database_' + IP + '.rdd') ): # Si no existe la base de datos la crea

        ds = []
        for atribute in dataSources:
            ds.append("DS:{}:COUNTER:120:U:U".format(atribute))
        #print(ds)

        ret = rrdtool.create(
                            "DBs/database_{}.rdd".format(IP),
                            #"segmentosRed.rrd",
                            "--start",'N',
                            "--step",'60', # Cada 60 segundos grafica 1 punto     
                            # -------- DATA SOURCES --------
                            ds,                       
                            #"DS:segmentosEntrada:COUNTER:120:U:U",
                            # ------------------------------
                            # 1440 --> Guarda 24 horas con resolucion de 1 minuto
                            # 600 ---> Guarda 5 horas con resolucion de 30 segundos
                            # RRA:GUARDA_PROMEDIO:NO_PERMITE_DESCONOCIDOS:GUARDA_1_DATO_CADA_STEP:GUARDA_24_HORAS_RESOLUCION_1_MINUTO
                            "RRA:AVERAGE:0.5:1:1440",
                            )

        if ret:
            print (rrdtool.error())