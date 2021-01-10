# -*- coding: utf-8 -*-

archivo1 = open("apellidos-es.txt")
archivo2 = open("nombres-propios-es.txt")

# lineas1 = archivo1.readlines()
# lineas2 = archivo2.readlines()
# print unicode(lineas1, "utf-8"), lineas2

for i, linea1 in enumerate(archivo1):
    linea1 = linea1.rstrip("\n")
    print " %4d: %s" % (i, linea1)
archivo1.close()

print "=" * 50

for i, linea2 in enumerate(archivo2):
    linea2 = linea2.rstrip("\n")
    print " %4d: %s" % (i, linea2)
archivo2.close()