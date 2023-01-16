import sys
import datetime

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mailsender = "omar.fi.wwr@gmail.com" # Desde donde se envia (necesita contraseña de aplicacion)
mailreceip = "omar.fi.wwr@gmail.com,tanibet.escom@gmail.com" # A quien enviamos la notificacion

# mailreceip = "omar.fi.wwr@gmail.com,omar.aguirre.alvarez10@gmail.com,dummycuenta3@gmail.com" # A quien enviamos la notificacion
mailserver = 'smtp.gmail.com: 587'    # Servidor desde donde se envia
password = 'cjetckdxrxpewlyt'         # Contraseña de aplicacion

data = []
for line in sys.stdin: 
    data.append(line)

hostname = data[0]
ip = data[1]
date = datetime.datetime.now()
interface_disconnected = data[5].split() # interface_disconnected[1]
oid = data[3]
var = data[2] + data[4] + data[6] + data[7]


print("----------- Link Down -----------")
# for line in data:
#     print('Output:', line.rstrip())
print("HOSTNAME: " + hostname)
print("IP: " + ip)
print("FECHA: " + str(date) )
print("Interfaz que se desconecto: " + interface_disconnected[1])
print("VARIABLES: " + var)
print("OId: " + oid)
print("---------------------------------")

# CREAMOS Y ENVIAMOS CORREO
msg = MIMEMultipart()
msg['Subject'] = "ALERTA - Omar Aguirre Alvarez - 4CM13" # Asunto
msg['From'] = mailsender # Envia
msg['To'] = mailreceip   # Recibe 

msg.attach(MIMEText('\r\r\nAlumno: Omar Aguirre Alvarez', _charset='utf-8'))
msg.attach(MIMEText('\r\r\nGrupo: 4CM13', _charset='utf-8'))
msg.attach(MIMEText('\r\r\n', _charset='utf-8'))

msg.attach(MIMEText('\r\r\n---------------------------------', _charset='utf-8'))
msg.attach(MIMEText('\r\r\nSe recibió un mensaje de tipo ALERTA', _charset='utf-8'))
msg.attach(MIMEText('\r\r\nHOSTNAME: ' + hostname, _charset='utf-8'))
msg.attach(MIMEText('IP: ' + ip, _charset='utf-8'))
msg.attach(MIMEText('FECHA: ' + str(date), _charset='utf-8'))
msg.attach(MIMEText('\r\r\nInterfaz que se desconecto: ' + interface_disconnected[1], _charset='utf-8'))
msg.attach(MIMEText('\r\r\nVARIABLES: \r\r\n' + var, _charset='utf-8'))
msg.attach(MIMEText('OID: ' + oid, _charset='utf-8'))
msg.attach(MIMEText('---------------------------------', _charset='utf-8'))

s = smtplib.SMTP(mailserver)    

s.starttls()
# Login Credentials for sending the mail
s.login(mailsender, password) # Loggea en el correo (sender) para enviar el correo

s.sendmail(mailsender, mailreceip.split(","), msg.as_string()) # Se envia el correo
s.quit() # Finalizamos