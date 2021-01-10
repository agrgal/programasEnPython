# coding: utf-8

import json

data = {"Frutería": [  {"Fruta":   [    {"Nombre":"Sandía","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ]}

data_string = json.dumps(data)

archivo = open("fruteria.txt","w")
archivo.write(data_string.encode("utf-8"))
archivo.close()
