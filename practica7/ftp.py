Ruta__servidor_FTP = 'ftp.us.debian.org'
import ftplib
def cliente_ftp_conexion(servidor, nombreDeUsuario, correo):
    ftp=ftplib.FTP(servidor, nombreDeUsuario, correo)
    print ("Archivos disponibles en %s:" %servidor)
    archivos = ftp.dir()
    print (archivos)
    ftp.retrbinary('RETR welcome.msg',open ('welcome.msg', 'wb').write)
    ftp.quit()
if __name__ == '__main__':
  cliente_ftp_conexion(servidor=RUTA_SERVIDOR_FTP, nombreDeUsuario='Jorjais', correo='locogl4d05@gmail.com')
