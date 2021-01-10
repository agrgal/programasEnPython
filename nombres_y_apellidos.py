# -*- coding: utf-8 -*-

archivo1 = open("apellidos-es.txt")
archivo2 = open("nombres-propios-es.txt")

# lineas1 = archivo1.readlines()
# lineas2 = archivo2.readlines()
# print unicode(lineas1, "utf-8"), lineas2

linea1 = archivo1.readline() # ¡Ojo!, readline no readlineS
print linea1
while linea1 !="":
    linea1 = archivo1.readline() # ¡Ojo!, readline no readlineS
    linea1 = linea1.rstrip("\n")
    print linea1
archivo1.close()

print "=" * 50

for linea2 in archivo2:
    linea2 = linea2.rstrip("\n")
    print linea2
archivo2.close()