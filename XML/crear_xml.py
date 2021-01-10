# coding: utf-8

from xml.dom import minidom

Ordenador1 = ['Pentium M', '512MB']
Ordenador2 = ['Pentium Core 2', '1024MB']
Ordenador3 = ['Pentium Core Duo', '1024MB']
listaOrdenadores = [Ordenador1, Ordenador2, Ordenador3]

# Abro un modelo DOM en modo implementar
DOMimpl = minidom.getDOMImplementation()

#Crear el documento econ la etiqueta principal estacionesTrabajo
xmldoc = DOMimpl.createDocument(None,"estacionesTrabajo", None)
doc_root = xmldoc.documentElement

# Recorro la lista de ordenadores
for ordenador in listaOrdenadores:
    
    #Crear Nodo... (*)
    nodo = xmldoc.createElement("Ordenador")

	# Crear un subnodo, llamado procesador
    elemento = xmldoc.createElement('Procesador')
    # Le añado un nodo de texto, y le asigno la posición 0 de la lista
    elemento.appendChild(xmldoc.createTextNode(ordenador[0]))
    # Añado el subnodo al nodo anterior
    nodo.appendChild(elemento)
    
    # Idéntico.
    elemento = xmldoc.createElement('Memoria')
    elemento.appendChild(xmldoc.createTextNode(ordenador[1]))
    nodo.appendChild(elemento)

	# (*)... que se añade como hijo al doc_root
    doc_root.appendChild(nodo)

# Recorrer para presentar en pantalla la lista de los nodos
listaNodos = doc_root.childNodes
for nodo in listaNodos:
    print nodo.toprettyxml()

# Guardar la información en un fichero de texto
fichero = open("ordenadores.xml", 'w')
# fichero.write(xmldoc.toxml())
# fichero.write(xmldoc.toprettyxml()) --> diferentes formas de guardar un fichero xml
fichero.write(xmldoc.toprettyxml(encoding="utf-8"))
fichero.close()
