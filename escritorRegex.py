micadena=input("Escribe una cadena regular: ")
miresultado=""

"""
micadena=micadena.replace(" ","\s*")
micadena=micadena.replace("+","\+")
micadena=micadena.replace("(","\(")
micadena=micadena.replace(")","\)")
"""

micadena=micadena+" "
l=len(micadena)

for i in range(0,l):
	if (micadena[i].isalpha() and (micadena[i+1].isalpha() or micadena[i+1].isdigit())):
		miresultado=miresultado+micadena[i]
	elif (micadena[i].isalpha() and not micadena[i+1].isalpha() and not micadena[i+1].isdigit()):
		miresultado=miresultado+micadena[i]+"\s*"
	elif (micadena[i]=="+"):
		miresultado=miresultado+"\+\s*"
	elif (micadena[i]=="*"):
		miresultado=miresultado+"\*\s*"
	elif (micadena[i]=="("):
		miresultado=miresultado+"\(\s*"
	elif (micadena[i]==")"):
		miresultado=miresultado+"\)\s*"
	elif (micadena[i].isdigit() and (micadena[i+1].isdigit() or micadena[i+1].isalpha())):
		miresultado=miresultado+micadena[i]
	elif (micadena[i].isdigit() and not micadena[i+1].isdigit() and not micadena[i+1].isalpha()):
		miresultado=miresultado+micadena[i]+"\s*"
	elif (micadena[i]==" "):
		miresultado=miresultado+"\s*"
	else:
		miresultado=miresultado+micadena[i]+"\s*"

miresultado="^\s*"+miresultado+"\s*$"

while ("\s*\s*" in miresultado):
	miresultado=miresultado.replace("\s*\s*","\s*")

print(miresultado)

