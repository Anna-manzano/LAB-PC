#Script creado por:Anna Patricia Manzano
#Fecha: viernes 25 de mayo del 2023
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
palabra= str(input('ingrese la palabra que desee buscar '+'\n'))
html= urlopen('https://revistabyte.es/ciberseguridad/')
bs = BeautifulSoup (html, 'html.parser')

pags = bs.find_all ('a', {'href':re.compile(palabra)})
for pag in pags:
    link = pag['href']
    print (link)
    html2=urlopen(link)
    bs=BeautifulSoup (html2, 'html.parser')
    contenidos = bs.find_all('p')
    for contenido in contenidos:
      print (contenido.get_text()+'\n')

