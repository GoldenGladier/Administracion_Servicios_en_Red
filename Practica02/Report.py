from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
from graphRRD import graphRRD
import Agent
import datetime
import time
import getSNMP as SNMP

def makeReport(agent : Agent, id):
    print("\nGenerando reporte del agente #" + str(id) + " ...")    
    try:
        c = canvas.Canvas("Report - " + agent.getIP() + ".pdf", pagesize=A3)
        text = c.beginText(100, 1100)
        text.setFont("Times-Roman", 18)
        # title and information
        text.textLine("Adeministración de Servicios en Red")
        text.textLine("Sistema de Administración de Red")
        text.textLine("Práctica 01 - Adquisición de información")
        text.textLine("Omar Aguirre Alvarez - 4CM13 - 2020630593")
        # information agent
        text.textLine("") 
        text.setFont("Times-Roman", 15)       
        text.textLine("Información del dispositivo #" + str(id))  

        text.setFont("Times-Roman", 12) 
        c.drawImage("img/"+str(agent.getSO())+".png", 550,1000, width = 100, height = 100)
        text.textLine("Sistema Operativo: " + agent.getSO())
        text.textLine("Version de Sistema Operativo: " + agent.getVersionSO())
        text.textLine("Nombre del dispositivo: " + agent.getName())
        text.textLine("Informacion de contacto: " + agent.getContact())
        text.textLine("Ubicacion: " + agent.getLocation())
        text.textLine("Numero de interfaces: " + agent.getNumInterfaces())
        text.textLine("1 .- up")
        text.textLine("2.- down")
        text.textLine("6.- notPresent")
        
        interfaces = agent.getInterfaces()
        for index, interfaz in enumerate(interfaces):
            #print("Interfaz " + str(index) + " - Estado: " + interfaz)
            text.textLine("Interfaz " + str(index) + " - Estado: " + interfaz)
        # Generate report
        c.drawText(text)
        c.save()
        print("Reporte generado correctamente.\n")
    except Exception as error:
        print("ERROR: " + str(error) + "\n")

def makeReportAccounting(agent : Agent, id, atributes, hora_inicial, hora_final):
    hora_inicial = hora_inicial.split(sep=':')
    # print("hora_inicial: " + str( hora_inicial ) )
    hora_final = hora_final.split(sep=':')
    # print("hora_final: " + str(hora_final) )
    today = datetime.date.today()
                                           # año, mes, dia, hora, minuto, segundo
    epoch_initial = datetime.datetime(today.year, today.month, int( hora_inicial[2] ) if len(hora_inicial) > 2 else today.day, int( hora_inicial[0] ), int( hora_inicial[1] ), 0)
    epoch_final = datetime.datetime(today.year, today.month, int( hora_final[2] ) if len(hora_final) > 2 else today.day, int( hora_final[0] ), int( hora_final[1] ), 0)
 
    for atribute in atributes:
        graphRRD(agent.getIP(), atribute, epoch_initial, epoch_final)
        # print(atribute)

    print("\nGenerando reporte del agente #" + str(id) + " ...")    
    try:
        c = canvas.Canvas("Accounting Report - " + agent.getIP() + ".pdf", pagesize=A3)
        text = c.beginText(100, 1100)
        text.setFont("Times-Roman", 18)
        # title and information
        text.textLine("Administración de Servicios en Red")
        text.textLine("Sistema de Administración de Red")
        text.textLine("Práctica 02 - Administración de contabilidad")
        text.textLine("Omar Aguirre Alvarez - 4CM13 - 2020630593")
        # information agent
        text.textLine("") 
        text.setFont("Times-Roman", 15)       
        text.textLine("Información del dispositivo #" + str(id))  

        text.setFont("Times-Roman", 12) 
        text.textLine("version: " + agent.getSNMP_version())
        text.textLine("device: " +  agent.getName())
        text.textLine("description: *")
        text.textLine("date: " + time.strftime("%c"))
        text.textLine("defaultProtocol: radius")
        text.textLine(" ")
        text.textLine("rdate: " + str( datetime.datetime.fromtimestamp( epoch_initial.timestamp() ) ) + "  -  " + str( datetime.datetime.fromtimestamp( epoch_final.timestamp() ) ))
        text.textLine("#NAS-IP-Address")
        text.textLine("4: " + agent.getIP())
        text.textLine("#NAS-Port")
        text.textLine("5: " + agent.getPort())
        text.textLine("#NAS-Port-Type")
        text.textLine("61: *")        
        text.textLine("#User-Name")
        text.textLine("1: " + agent.getContact())   
        text.textLine("#Acct-Status-Type")
        text.textLine("40: *")   
        text.textLine("#Acct-Delay-Time")
        text.textLine("41: *")   
        text.textLine("#Acct-Input-Octets")
        text.textLine("42: " + SNMP.consultaSNMP(agent.getComunity(), agent.getIP(), '1.3.6.1.2.1.2.2.1.10.1') )   
        text.textLine("#Acct-Output-Octets")
        text.textLine("43: " + SNMP.consultaSNMP(agent.getComunity(), agent.getIP(), '1.3.6.1.2.1.2.2.1.16.1') )   
        text.textLine("#Acct-Session-Id")
        text.textLine("44: *")
        text.textLine("#Acct-Authentic")
        text.textLine("45: *")
        text.textLine("#Acct-Session-Time")
        text.textLine("46: *")
        text.textLine("#Acct-Input-Packets")
        text.textLine("47: " + SNMP.consultaSNMP(agent.getComunity(), agent.getIP(), '1.3.6.1.2.1.4.3.0') )
        text.textLine("#Acct-Output-Packets")
        text.textLine("48: " + SNMP.consultaSNMP(agent.getComunity(), agent.getIP(), '1.3.6.1.2.1.4.10.0') )
        text.textLine("#Acct-Terminate-Cause")
        text.textLine("49: *")
        text.textLine("#Acct-Multi-Session-Id")
        text.textLine("50: *")
        text.textLine("#Acct-Link-Count")
        text.textLine("51: *")
        
        chartHeight = 850
        for atribute in atributes:
            image = "DBs/" + atribute + "_" + agent.getIP() + ".png"
            c.drawImage(image, 350, chartHeight, width = 400, height = 150)
            chartHeight = chartHeight - 170

        # Generate report
        c.drawText(text)
        c.save()
        print("Reporte generado correctamente.\n")
    except Exception as error:
        print("ERROR: " + str(error) + "\n")