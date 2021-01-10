# coding: utf-8

import json

archivo = open("fruteria.txt","r")
data_string = archivo.read()
archivo.close()

# --> Obtenido como cadena de texto
print data_string

data = json.loads(data_string)
tab = "-" * 3
for clave, elemento in data.items():
	# --> elemento es un diccionario, luego la clave es Fruteria, y elemento es el resto
	print tab,clave
	# print elemento # -> Imprimiría una lista de DOS elementos
	tab += tab
	for i in elemento: # -> recuerda, elemento es una lista. Tiene dos elementos diccionarios
		for clave, j in i.items(): 
			print tab, clave # --> Saca las claves, "Fruta" y "verdura
			# print j # -> Imprimiría dos listas
			for k in j:
				# --> print k, cada "k" es un diccionario
				for clave, l in k.items():
					print tab,tab,clave, ": ", l
