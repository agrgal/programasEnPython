# coding: utf-8

from xml.dom import minidom                                        

xmldoc = minidom.parse('cd_catalogo.xml')     
print xmldoc                                                                 
grammarNode = xmldoc.firstChild 
print grammarNode # CATALOGO 

refNode = grammarNode.childNodes[1]       
print refNode #--> Nivel 1, etiqueta CD.
print refNode.childNodes  # --> Todo lo que hay bajo la etiqueta CD                           

pNode = refNode.childNodes[3] 
print pNode #--> El elemento que está tercero. "ARTISTA"
print pNode.toxml()  # -> Impresión de dicho nodo.

print pNode.firstChild      #-> Texto que hay dentro de "ARTISTA", pero como objeto                           
print pNode.firstChild.data #-> Texto extraído del objeto anterior.
