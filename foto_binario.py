# -*- coding: utf-8 -*-
imagen = open("coche.png", "rb")

print imagen.name
print imagen.mode
print imagen.encoding

print imagen.tell()
data = imagen.read()
print len(data)

imagen.seek(0)
lista = []
for i in range(len(data)):
    # lista.append(imagen.read(1))
    lista.append(ord(imagen.read(1)))

print lista
print len(lista)

print "terminó fichero"

imagen.close()