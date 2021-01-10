# -*- coding: utf-8 -*-

import os

# Si quiero imprimir las variables de entorno, descomento
# for variable, valor in os.environ.iteritems():
# 	print ("%s ==> %s") % (variable, valor)

# El directorio actual
ruta = os.getcwd()
print ruta

# crear un subdirectorio
if not os.access("mod_os_ejemplo",0):
	os.mkdir("mod_os_ejemplo")
	
#Accede al subdirectorio
os.chdir("mod_os_ejemplo")
# y otro subdirectorio
if not os.access("probando",0):
	os.mkdir("probando")

# accede al directorio de ejecución del programa
# Si escribo la siguiente línea vuelvo atrás y escribe el archivo en 
# la ruta donde se ejecuta el programa
# os.chdir("../")
# Pero si escribo lo siguiente, escribirá el fichero en 
# el nuevo directorio
os.chdir("probando")

# Escribe un fichero en él
with open("prueba.txt", "a+") as archivo:
	archivo.write("Hola")
	
#Y le cambio el nombre...
os.rename("prueba.txt","probando.txt")

os.chdir("../")
print ("Tamaño del directorio... %.3f") % os.path.getsize("probando")
print ("Tamaño del fichero... %.3f") % os.path.getsize("probando/probando.txt")
	


