# *-* coding:utf-8 *-*

miLista = [15, 10, 4, 7, 5, 3, 4]

miListaOrdenada = sorted(miLista)

print ("La lista desordenada es %s y la ordenada %s") % (miLista, miListaOrdenada)

print("... pero puedo convertir la lista original en una que ya se queda ordenada")

miLista.sort()

print ("La lista ya ordenada %s") % (miLista)

print("pero la puedo ordenar en orden inverso")

miLista.reverse()

print ("La lista en orden inverso %s") % (miLista)