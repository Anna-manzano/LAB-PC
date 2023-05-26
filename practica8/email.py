from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse, smtplib, json

Descripcion= """Modo de uso:
sendmail.cpy -to 'Destinatario' -subj 'Asunto' -Mensaje -atch 'Archivos adjuntos' """
Parser= argparse.ArgumentParser(Descripcion = 'Envio de Email', epilog= Descripcion, formatter_class=argparse.RawDescriptionHelpFormatter)
Parser.add_argumet("-to", type=str, metavar= 'Destino', dest="to", ayuda="Correo al que sera enviado el mensaje", required= True)
Parser.add_argument("-subj", type=str, metavar='Asunto', dest= "subj", ayuda="Agregar un asunto", required=True)
Parser.add_argument("-msj", type=str, metavar='Mensaje', dest= "msj", ayuda="Agregar mensaje", required=True)
Parser.add_argument("-atch", type=str, metavar='Archivo', dest= "atch", ayuda="Archivos adjuntos")




data = { }
with open ('pass.json') as f:
  data = json.load(f)
msg = MIMEMultipart ()
message = parameters.msj

msg[ ' From' ] = data ['user']
msg['to'] = parameters.to
msg['subject']=parameters.subj
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP(data['server'])
server.starttls()
server.login(data['user'], data['pass'])
server.sendmail(msg['From'],msg['to'], msg.as_string())
server.quit()
print("Se a enviado el mensaje a" + (msg['to'])
