# coding: utf-8

from xml.dom import minidom, Node

doc = minidom.Document() #--> Crear un documento xml

doc.appendChild(doc.createComment("Creando documento de ejemplo XML")) #-> Escribir comentario

book = doc.createElement('libro') # --> Crear elemento dentro del documento
doc.appendChild(book) #-> Añadirlo a la raíz del documento 

title = doc.createElement('Título') # --> Crear elemento título
title.appendChild(doc.createTextNode('D. Quijote de La Mancha')) # --> Agrgar nodo de texto
book.appendChild(title) # --> Añadir dentro del elemento book

author = doc.createElement('Autor') # --> Crear elemento Autor
book.appendChild(author) # --> Añadir al elemento libro

name = doc.createElement('Nombre y Apellidos')  # --> Crear elemento Nombre y Apellidos
author.appendChild(name) # --> Añadir dentro de Autor

firstname = doc.createElement('Nombre') # --> Crear elemento Nombre
name.appendChild(firstname)
firstname.appendChild(doc.createTextNode('Miguel'))
name.appendChild(doc.createTextNode('Texto añadido aquí'))
lastname = doc.createElement('Apellidos') # --> Crear elemento  Apellidos
name.appendChild(lastname)
lastname.appendChild(doc.createTextNode('De Cervantes Saavedra'))

chapter = doc.createElement('Capítulo')
book.appendChild(chapter)
chapter.setAttribute('number', '1')
title = doc.createElement('title')
chapter.appendChild(title)
title.appendChild(doc.createTextNode('Capítulo Primero'))

print doc.toprettyxml(indent =' ')
