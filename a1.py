# *-* coding:utf-8 *-*

miCadena ="Frase rimbombante"

miCadena2 = sorted(miCadena, key=str.lower)
print miCadena2

print ("Número de caracteres: %d") % (len(miCadena2))
print ("Número de caracteres \"a\": %d") % (miCadena.count("a"))
