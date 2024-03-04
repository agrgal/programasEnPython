import string

plantilla = string.Template("$nombre es alumn${genero} del $ies")
print(plantilla.substitute(nombre="Alejandro",ies="IES Seritium",genero="o"))
print(plantilla.substitute(nombre="Elena",ies="IES Almunia",genero="a"))

#con diccionario
d=dict(nombre="María",ies="Alto Guadiana",genero="a")
print(plantilla.substitute(d))

# $$ escape para escribir el dolar
plantilla = string.Template("$nombre ha ganado $sueldo$$")
d =dict(nombre="Ana",sueldo=2800)
print(plantilla.substitute(d))

# prefijos con {}
plantilla = string.Template("${tipo}_nombre es el fichero cargado")
print(plantilla.substitute(tipo="01"))

# si no pongo todos los datos, tengo un error. Puedo usar safe_substitute
plantilla = string.Template("$nombre ha ganado $sueldo$$ en el año $año")
d =dict(nombre="Aurelio",sueldo=800)
# print(plantilla.substitute(d)) # da un error, porque no indico el año
print(plantilla.safe_substitute(d)) # NO da un error, pero imprime en pantalla la variable. 
