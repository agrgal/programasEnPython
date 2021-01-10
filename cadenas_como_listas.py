# *-* coding:utf-8 *-*

miCadena = "Esta es una frase o conjunto de palabras con sentido"

print miCadena

# Separando la cadena por el caracter espacio
# no hace falta. En el caso del espacio es el caracter por defecto. Funcionaría
# cs = miCadena.split()
cs = miCadena.split(" ")
print cs

# Vuelvo a unirla, pero usando los caracteres ---
miCadena2 = "---".join(cs)
print miCadena2
