# -*- coding: utf-8 -*-

import csv, random, statistics as st

f = open("temperatura_media.csv", 'r')
ultimo = []
try:
	reader = csv.reader(f)
	for i,row in enumerate(reader):
		ultimo = row
		print row
finally:
	print "He terminado de leer datos"

f.close()

# añado un nuevo dato
# calculado en torno al anterior
nuevo = []
for i, dato in enumerate(ultimo):
	if i==0:
		nuevo.append(int(dato)+1)
	elif i>0 and i<11:
		signo = random.randrange(-1,1,2)
		x = float(dato.replace(",","."))
		nuevo.append(x + random.randrange(-50,50,1)/10)

media = st.mean(nuevo[1:])
nuevo.append(media)
print nuevo

escribir =[]
for i, dato in enumerate(nuevo):
	escribir.append(str(dato).replace(".",","))

print "Añadiré el dato: ", escribir

f = open("temperatura_media.csv", 'a')
archivo_escribir = csv.writer(f)
archivo_escribir.writerow(escribir)
f.close()



