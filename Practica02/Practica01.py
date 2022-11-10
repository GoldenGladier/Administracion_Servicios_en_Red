from Agent import Agent
from Report import makeReport

agents = []
FILE_NAME = 'agents.txt'

def writeAgent(agent):
    #agents.txt
    f = open (FILE_NAME,'a')
    f.write("\n" + str(agent))
    f.close()

def reSaveAgents():
    #agents.txt
    f = open (FILE_NAME,'w')
    f.write("")
    f.close()    

    f = open (FILE_NAME, 'a')
    for agent in agents:        
        f.write("\n" + str(agent))
    f.close()

def readAgents():
    # agents.txt
    f = open (FILE_NAME,'r')
    mensaje = f.read()
    # print(mensaje)
    f.close()
    
    agents.clear()
    tokens = mensaje.split(sep="---- Device ----")
    #print("DEVICES SPLIT: " + str(len(tokens)))
    if(len(tokens) > 1):
        for index, msg  in enumerate(tokens):
            if(msg != '\n' and msg != '\r\n' and msg != "\r"):
                print(str(index) + ".\n", end="")
                for line in msg.split('\n'):
                    if("Comunidad: " in line):
                        comunity = line.replace("Comunidad: ", '')
                    elif("SNMP version: " in line):
                        SNMP_v = line.replace("SNMP version: ", '')
                    elif("Puerto: " in line):
                        port = line.replace("Puerto: ", '')      
                    elif("IP: " in line):
                        ip = line.replace("IP: ", '')
                agent = Agent(comunity, SNMP_v, port, ip)
                agents.append(agent)
                print(agent)        

while(True):
    print("Sistema de Administración de Red")
    print("Práctica 01 - Adquisición de información")
    print("Omar Aguirre Alvarez - 4CM13 - 2020630593")

    print("Elige una opción: \n 1) Agregar dispositivo. \n 2) Cambiar información del dispositivo. \n 3) Eliminar dispositivo. \n 4) Ver dispositivos. \n 5) Reporte de un dispositivo. \n 6) Salir. \nOpción: ")

    opt = int(input())
    if(opt == 1):
        print("Asigne comunidad: ")
        comunity = input()
        print("Asigne versión SNMP: ")
        SNMP_v = input()
        print("Asigne puerto: ")
        port = input()
        print("Asigne IP: ")
        IP = input()                        
        agent = Agent(comunity, SNMP_v, port, IP)
        print(agent)
        writeAgent(agent)
    if(opt == 2):
        print("===== AGENTES =====")
        readAgents()    
        if len(agents) <= 0:
            print("No hay dispositivos para mostrar :c")                     
        print("===================")
        if len(agents) > 0:
            print("¿Qué agente desea cambiar? ", end="")
            index_agent = int(input()) - 1

            if index_agent > len(agents) - 1:
                print("No existe ese dispositivo\n")
            else:                
                current_agent = agents[index_agent] # Obtenemos el agente que vamos a modificar

                print("Ingrese la nueva información del dispositivo (enter para usar no cambiar)")
                print("\nComunidad: ")
                comunity = input()
                if(comunity != ''):
                    current_agent.setComunity(comunity)
                print("Versión SNMP: ")
                SNMP_v = input()
                if(SNMP_v != ""):
                    current_agent.setSNMP_version(SNMP_v)        
                print("Puerto: ")
                port = input()
                if(port != ""):
                    current_agent.setPort(port)           
                print("IP: ")
                IP = input()     
                if(IP != ""):
                    current_agent.setIP(IP)                             
                
                print(current_agent)      
                reSaveAgents()  
                readAgents()
    if(opt == 3):
        print("===== AGENTES =====")
        readAgents()    
        if len(agents) <= 0:
            print("No hay dispositivos para mostrar :c")                     
        print("===================")
        if len(agents) > 0:
            print("Agente a eliminar: ", end="")
            index_agent = int(input()) - 1

            if index_agent > len(agents) - 1:
                print("No existe ese dispositivo\n")
            else:                
                agents.pop(index_agent) # eliminamos el agente
                reSaveAgents()
                readAgents()
    
    if(opt == 4):
        print("===== AGENTES =====")
        readAgents()    
        if len(agents) <= 0:
            print("No hay dispositivos para mostrar :c")                     
        print("===================")    
    
    if(opt == 5):
        print("===== AGENTES =====")
        readAgents()    
        if len(agents) <= 0:
            print("No hay dispositivos para mostrar :c")                     
        print("===================")
        if len(agents) > 0:
            print("Agente para generar reporte: ", end="")
            index_agent = int(input()) - 1

            if index_agent > len(agents) - 1:
                print("No existe ese dispositivo\n")
            else:                                
                makeReport(agents[index_agent], index_agent + 1)
    if(opt == 6):
        exit(0)
