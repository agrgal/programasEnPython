# *-* coding: utf-8 *-*
import timeit

start = timeit.timeit()

numeros = []
for i in range(2, 1001):
    numeros.append(int(i))

# print numeros

primos = [2]

# print numeros[1] % primos[-1]

while len(numeros) > 1:
    # ultimo = primos[-1]
    penultimo = primos[-1]
    for x in numeros:
        # print numeros
        # print x
        # print ("Valor %s, ..., %s") % (x, x % ultimo)
        if (x % primos[-1] == 0 or x % penultimo == 0):
            if numeros.index(x) > 0 and penultimo == primos[-1]:
                penultimo = numeros[0]
            numeros.remove(x)

    primos.append(numeros[0])

# print numeros
# primos.insert(0,1)

# print "\nTenemos %d números primos. Son: %s" % (len(primos), primos)

end = timeit.timeit()

print end - start

# ===============================================
''' Escribir en un fichero '''
# apertura
archivo = open("numerosprimos.txt", "w")

for i in primos:
	archivo.write(str(i)+"\n");

# cierre
archivo.close()

# ===============================================
''' Leer del fichero y escribir en UNICODE'''
# apertura
archivo = open("numerosprimos.txt", "a+")
archivo2 = open("numerosprimosUNICODE.txt","w")

i=1
u=""
for linea in archivo:
    linea = linea.rstrip("\n")
    # print ("%d: %s") % (i, linea)
    # archivo2.write(unichr(int(linea)))
    u = u + unichr(int(linea)) # convertir linea, que es un string, en int. Ir construyendo la cadena...
    i += 1
    
archivo2.write(u.encode("UTF-8")) #IMPORTANTE: al escribirlos en un fichero utilizar una codificación determinada
# En mi caso escogí UTF-8

# cierre
archivo.close()
archivo2.close()

# ===============================================
''' Leer desde el fichero UNICODE '''
archivo3 = open("numerosprimosUNICODE.txt","r")

for linea in archivo3:
	linea = linea.rstrip("\n")
	print linea
	linea2 = linea.decode("UTF-8") # Decodificar de UTF-8 a UNICODE otra vez...
	for n in linea2:
		print ord(n)

archivo3.close()

# ===============================================
''' Comparando '''
for i in primos:
	indice = primos.index(i) # obtiene el número de la lista
	j = ord(linea2[indice])
	if (i != j):
		print "Existe una discrepancia"
		print "En el número primo %d" % (i)
		break

