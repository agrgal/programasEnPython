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

cds = coleccion.getElementsByTagName("CD")

for cd in cds:	
	
	titulo = cd.getElementsByTagName("TITULO")
	# titulo es una lista de Nodos, aunque sólo sea uno. Lo siguiente print titulo.toxml() no funcionará
	# print titulo[0].toxml() Esto si funcionará
	# print titulo[0].childNodes # --> Esto es un objeto
	print titulo[0].childNodes[0].data #--> Accede a un dato de texto
	# print titulo[0].childNodes[0].data.encode("utf-8") #-> no está de más codificar en utf-8
	if titulo[0].childNodes[0].data.encode("utf-8") == "Empire Burlesque":
		print "detectado"
		titulo[0].childNodes[0].data = u'Imperio Burlesco' # --> Tiene que ser en formato UNICODE u''
		print titulo[0].childNodes[0].data #--> Accede a un dato de texto
	print "=" * 20
	

fichero = open("cd_catalogo2.xml","w")
# fichero = open("cd_catalogo.xml","w") # --> Para sobrescribir en el mismo fichero.
fichero.write(coleccion.toxml(encoding='utf-8')) #--> Forzar la codificación a UTF-8
fichero.close()
# print coleccion.toprettyxml() # --> formas de presentar los daros como un bloque '''

