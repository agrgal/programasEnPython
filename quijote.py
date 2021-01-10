archivo = open("quijote.txt")
i = 1
for linea in archivo:
    linea = linea.rstrip("\\n")
    # print " %d: %s" % (i, linea)
    print linea
    i+=1
archivo.close()