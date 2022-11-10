import sys
import rrdtool
import time
import datetime
import calendar

def graphRRD(IP, dataSource, epoch_initial, epoch_final):
    print("\nInicio: " + str( datetime.datetime.fromtimestamp( epoch_initial.timestamp() ) ) )
    print("Final: " + str( datetime.datetime.fromtimestamp( epoch_final.timestamp() ) ) )

    #print("Tiempo actual: " + str( datetime.datetime.fromtimestamp( tiempo_actual ) ) )
   # dateTime_tiempo_inicial = str( datetime.datetime.fromtimestamp( tiempo_inicial ) )
    #print("Tiempo inicial (datetime): " +  dateTime_tiempo_inicial)

    ti = str( time.mktime( epoch_initial.timetuple() ) )[:-2]
    tf = str( time.mktime( epoch_final.timetuple() ) )[:-2]

    # BUSCAR CONSEJO EN CARPETA 4. ADQUISICION RRD --> GRAPH.PY
    ret = rrdtool.graphv( "DBs/" + dataSource + "_" + IP + ".png",
                        "--start", str( ti ),
                        "--end", str( tf ),
                        "--vertical-label=Paquetes",
                        "--title=" + IP + " - " + dataSource,
                        "DEF:" + dataSource + "=DBs/database_" + IP + ".rdd:" + dataSource + ":AVERAGE",
                        "LINE1:" + dataSource + "#FF0000:" + dataSource,
    )
    print(ret)