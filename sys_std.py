# -*- coding: utf-8 -*-

import os, sys

print "Escribo algo"

sys.stdout.write("Escribo algo de otra forma")

print "\n"

cadena = raw_input("Di algo...: ")
print cadena

print "Escribe algo más...", sys.stdin.readline()[:-1]
