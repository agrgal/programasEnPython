# *-* coding:utf-8 *-*

miLista = ["cC","bB", "dD", "aA"]
print sorted(miLista)

# cuidado, y si las mayúsculas y las minúsculas están
# alternadas como primera letra ¿¿??
miLista = ["Cc","bB", "Dd", "aA"]
print sorted(miLista)
# Ordena PRIMERO LAS MAYÚSCULAS y después las minúsculas.

# A menos que use un criterio de ordenación
print sorted(miLista, key=str.lower)
# En este caso la ordena como si las mayúsculas las hubiera convertido a minúsculas.

# O al revés...
print sorted(miLista, key=str.upper)

#¿Qué ordena antes, números o letras?
miLista2 = [7, "cC", 2, 5, 1, "aA", 3, "fF", 0.1, 5.32]
print sorted(miLista2)

# o al revés
aa = sorted(miLista2, reverse=True)
print aa

print miLista2
miLista2.reverse()
print miLista2