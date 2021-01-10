# -*- coding:utf-8 -*-

from subprocess import call

print "No se verá esto"
call("clear")

print "Contenido de la carpeta actual"
print "=============================="

lista2 = ["ls","-lha"]
call(lista2)


