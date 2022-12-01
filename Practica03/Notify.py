import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from TrendUpdate import COMUNITY, IP
import getSNMP as SNMP

COMUNITY = 'OmarAA'
IP = '192.168.100.31'
COMMASPACE = ', '
# Define params
rrdpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/RRD'
imgpath = '/media/sf_School/Administracion_de_Servicios_en_Red/Practica03/IMG/'
fname = 'trend.rrd'

mailsender = "omar.fi.wwr@gmail.com" # Desde donde se envia (necesita contraseña de aplicacion)
mailreceip = "omar.fi.wwr@gmail.com,omar.aguirre.alvarez10@gmail.com,dummycuenta3@gmail.com" # A quien enviamos la notificacion
mailserver = 'smtp.gmail.com: 587'    # Servidor desde donde se envia
password = 'cjetckdxrxpewlyt'         # Contraseña de aplicacion

def getSO(COMUNITY, IP):
    info = SNMP.consultaSNMPCompleta(COMUNITY, IP, '1.3.6.1.2.1.1.1.0') 
    SO = ""             
    if info.find('#') != -1:
        if (info.find("Ubuntu") > 0):  # En caso de ser Ubuntu
            soaux = info.split()[5]
            ''.join(soaux)
            SO = soaux[soaux.find('-') + 1:]
    else:
        SO = info.split()[14] 
        versionSO = info.split()[16]    
        SO = SO + " - " + versionSO    
    return SO 

def getName(COMUNITY, IP):
    info = SNMP.consultaSNMPCompleta(COMUNITY, IP, '1.3.6.1.2.1.1.5.0')              
    info = info.split('=')
    return info[-1] 

def getLocation(COMUNITY, IP):
    info = SNMP.consultaSNMPCompleta(COMUNITY, IP, '1.3.6.1.2.1.1.6.0')              
    info = info.split('=')
    return info[-1]    
    # return info

def getTimeActive(COMUNITY, IP):
    info = SNMP.consultaSNMPCompleta(COMUNITY, IP, '1.3.6.1.2.1.1.3.0')              
    info = info.split('=')
    return info[-1]   
    # return info     

def send_alert_attached(subject, mensaje, img):
    """ Envía un correo electrónico adjuntando la imagen en IMG 
    NOTA: EL SALTO DE LINEA ESTA DADO POR --> \r\r\n
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject # Asunto
    msg['From'] = mailsender # Envia
    msg['To'] = mailreceip   # Recibe 
    # msg['Content-Type'] = "text/html"
    msg.attach(MIMEText(mensaje, _charset='utf-8'))
    fp = open(imgpath + img + '.png', 'rb') # Se abre la imagen que vamos a adjuntar (generada de la DB)
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img) # Se adjunta la imagen
    msg.attach(MIMEText('\r\r\nAlumno: Omar Aguirre Alvarez', _charset='utf-8'))

    msg.attach(MIMEText('\r\r\nDATOS DEL AGENTE:', _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nDispositivo: ' + getName(COMUNITY, IP), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nLocación: ' + getLocation(COMUNITY, IP), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nSistema operativo: ' + getSO(COMUNITY, IP), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nTiempo activo: ' + getTimeActive(COMUNITY, IP), _charset='utf-8'))
    s = smtplib.SMTP(mailserver)    

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password) # Loggea en el correo (sender) para enviar el correo

    s.sendmail(mailsender, mailreceip.split(","), msg.as_string()) # Se envia el correo
    s.quit() # Finalizamos

def send_alert_multiple_processors_attached(subject, images):
    """ Envía un correo electrónico adjuntando las imagenes en IMG
    """

    if( len(images) > 0):
        msg = MIMEMultipart()
        msg['Subject'] = subject # Asunto
        msg['From'] = mailsender # Envia
        msg['To'] = mailreceip   # Recibe 

        for img in images:
            #print("Attaching Image: " + img)
            fp = open(imgpath + img, 'rb') # Se abre la imagen que vamos a adjuntar (generada de la DB)
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img) # Se adjunta la imagen

        s = smtplib.SMTP(mailserver)    

        s.starttls()
        # Login Credentials for sending the mail
        s.login(mailsender, password) # Loggea en el correo (sender) para enviar el correo

        s.sendmail(mailsender, mailreceip, msg.as_string()) # Se envia el correo
        s.quit() # Finalizamos