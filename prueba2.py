def cambia_lista(lista):

    for i in range(len(lista)):
        lista[i] = lista[i]**2
    lista = range(len(lista))
    print lista

lista = [10, 20, 30, 40]
print ("Antes de llamar la funcion: %s") % (lista)
cambia_lista(lista)
print ("Despues de llamar la funcion: %s") % (lista)

