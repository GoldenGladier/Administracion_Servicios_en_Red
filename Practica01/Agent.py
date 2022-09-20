import getSNMP as SNMP
class Agent(object):
    def __init__(self, comunity, SNMP_version, port, ip):
        self.comunity = comunity
        self.SNMP_version = SNMP_version
        self.port = port
        self.ip = ip

    def getComunity(self):
        return self.comunity

    def setComunity(self, comunity):
        self.comunity = comunity

    def getSNMP_version(self):
        return self.SNMP_version

    def setSNMP_version(self, SNMP_version):
        self.SNMP_version = SNMP_version        

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = port             

    def getIP(self):
        return self.ip

    def setIP(self, ip):
        self.ip = ip       

    def getSO(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.1.1.0')              
        if info.find('#') != -1:
            if (info.find("Ubuntu") > 0):  # En caso de ser Ubuntu
                soaux = info.split()[5]
                ''.join(soaux)
                self.SO = soaux[soaux.find('-') + 1:]
        else:
            self.SO = info.split()[14]
            self.versionSO = info.split()[16]        
        return self.SO

    def getVersionSO(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.1.1.0')              
        if info.find('#') != -1:
            if (info.find("Ubuntu") > 0):  # En caso de ser Ubuntu
                indice_igual = info.index('=') #obtenemos la posición del carácter c
                indice_hash = info.index('#') #obtenemos la posición del carácter h

                subcadena = info[indice_igual+2:indice_hash-1]  
                subcadena = subcadena.split()
                #print(subcadena)  
                versionSO = subcadena[2]                       
        else:
            versionSO = info.split()[16] 
        #print(info)       
        return versionSO        

    def getLocation(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.1.6.0')              
        info = info.split('=')
        return info[-1]

    def getName(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.1.5.0')              
        info = info.split('=')
        return info[-1]     

    def getContact(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.1.4.0')              
        info = info.split('=')
        return info[-1]              

    def getNumInterfaces(self):
        info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.2.1.0')              
        info = info.split('=')
        num_inter = info[-1]   
        return num_inter   

    def getInterfaces(self):
        i = 0
        interfaces = []
        #print("Comenzando a guardar interfaces")
        while( i < int(self.getNumInterfaces()) ):  
            info = SNMP.consultaSNMP(self.comunity, self.ip, '1.3.6.1.2.1.2.2.1.8.' + str(i+1) )  
            info = info.split('=')
            interfaces.append(info[-1])
            #print("Interfaz " + str(i) + " done")
            i += 1
        return interfaces          

    def __str__(self):
        return "---- Device ----\nComunidad: " + self.comunity + "\nSNMP version: " + self.SNMP_version + "\nPuerto: " + self.port + "\nIP: " + self.ip + "\n----------------"               
