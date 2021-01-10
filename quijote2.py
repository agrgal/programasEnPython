# *-* coding:utf-8 *-*

archivo = open("quijote.txt")
for i, linea in enumerate(archivo):
    linea = linea.rstrip("\\n")
    print " %4d: %s" % (i, linea)
archivo.close()