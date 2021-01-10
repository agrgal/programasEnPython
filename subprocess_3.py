# -*- coding:utf-8 -*-

from subprocess import PIPE, Popen
 
proceso = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE)
error_encontrado = proceso.stderr.read()
proceso.stderr.close()
listado = proceso.stdout.read()
proceso.stdout.close()

if not error_encontrado: 
    print listado 
else: 
    print "Se produjo el siguiente error:\n%s" % error_encontrado

