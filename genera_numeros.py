# -*- coding: utf-8 -*-

archivo = open("numeros.txt", "w")

for i in range(50):
    # genera números pares
    archivo.write(str((i+1)*2)+"\n")

archivo.close()
# cierra el archivo

# lo abre otra vez en modo añadir y lectura
archivo = open("numeros.txt", "a+")

for i in range(50):
    # genera números impares
    archivo.write(str((i+1)*2-1)+"\n")

archivo.seek(0) #apunta el fichero a la primera línea
i=1
for linea in archivo:
    linea = linea.rstrip("\n")
    print ("%d: %s") % (i, linea)
    i += 1

archivo.close()

