#!/usr/bin/python
# coding: utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

# Abre el documento XML usando el analizador (parser) minidom
modelo = xml.dom.minidom.parse("cd_catalogo.xml") #-> Modelo # #  del Documento en forma de árbol. Apertura por nombre
# O bien
# fichero = open("cd_catalogo.xml")
# modelo = parse(fichero) # Otra forma de abrir el fichero.
# después al final habrá que cerrar el fichero. fichero.close()

coleccion = modelo.documentElement # -> Objeto raíz
print "El nombre de la coleccion es: %s \n" % coleccion.localName

print coleccion.toxml()
# print coleccion.toprettyxml() # --> formas de presentar los daros como un bloque

