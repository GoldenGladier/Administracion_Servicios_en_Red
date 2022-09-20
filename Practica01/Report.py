from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
import Agent

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