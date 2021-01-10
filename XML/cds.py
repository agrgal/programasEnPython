#!/usr/bin/python
# coding: utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

# Abre el documento XML usando el analizador (parser) minidom
DOMTree = xml.dom.minidom.parse("cd_catalogo.xml") #-> Modelo del Documento en forma de árbol
collection = DOMTree.documentElement # -> Objeto raíz
print "El nombre de la coleccion es: %s \n" % collection.localName


# Obtiene una lista de los objetos con la etiqueta CD
cds = collection.getElementsByTagName("CD")

# Muestra en pantalla cada detalle de cada CD
for cd in cds:	
   print "*****CD*****" 
   titulo = cd.getElementsByTagName('TITULO')[0]
   print "Título: %s" % titulo.childNodes[0].data.encode("utf-8")
   artista = cd.getElementsByTagName('ARTISTA')[0]
   print "artista: %s" % artista.childNodes[0].data.encode("utf-8")
   pais = cd.getElementsByTagName('PAIS')[0]
   print "País: %s" % pais.childNodes[0].data.encode("utf-8")
   comp = cd.getElementsByTagName('PAIS')[0]
   print "Compañía: %s" % comp.childNodes[0].data.encode("utf-8")
   precio = cd.getElementsByTagName('PRECIO')[0]
   print "Precio: %s €" % precio.childNodes[0].data.encode("utf-8")
   anno = cd.getElementsByTagName('ANNO')[0]
   print "Año: %s" % anno.childNodes[0].data.encode("utf-8")
   print "=" * 20 + "\n"
   
print collection.toxml()
