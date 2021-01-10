# coding: utf-8

import json

data = {"Frutería": [  {"Fruta":   [    {"Nombre":"Sandía","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ]}

desordenado = json.dumps(data)
ordenado = json.dumps(data, sort_keys=True) # --> Ordena por índices: Cantidad primero, nombre después, pero no por valores.
ordenado2 = json.dumps(data, sort_keys=True, indent=1) # --> Los presenta de una forma más legible. 
compacto = json.dumps(data, separators=(',',':')) #-> quita los espacios. Ahorra bytes en los ficheros.

print 'JSON:', desordenado,"\n"
print 'SORT:', ordenado,"\n" 
print 'SORT2:', ordenado2,"\n"
print 'COMPACTO:', compacto,"\n"

print 'UNSORTED MATCH:', desordenado == ordenado
print 'SORTED MATCH  :', ordenado == ordenado2

