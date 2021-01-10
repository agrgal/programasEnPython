# coding: utf-8

import json

data = {"Frutería": [  {"Fruta":   [    {"Nombre":"Manzana","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ]}

#Nos imprime en pantalla data como un tipo de dato nativo.
print 'DATA:', str(data)

#Nos devuelve el String con el JSON
data_string = json.dumps(data) # --> Analiza el dato como JSON . Como string.
print 'JSON:', data_string

decoded = json.loads(data_string)
print 'DECODIFICADO:', data_string

tab = "-" * 3
for clave, elemento in decoded.items():
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
