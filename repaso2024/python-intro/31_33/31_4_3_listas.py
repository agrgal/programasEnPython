list1 = ['John', 'Paul', 'George', 'Ringo']
print('list1[1]:', list1[1])
print('list1[-1]:', list1[-1])
print('list1[1:3]:', list1[1:3])
print('list[:3]:', list1[:3])
print('list[1:]:', list1[1:])

list2=['Luis','Ana','Alberto']

list1.append('Jorge')
list1.extend(list2) # o bien list1 += list2

list1.insert(1,"Paloma") # inserta elemento en la posición 1.

list1.remove('Luis')

elemento_eliminado = list1.pop(2)
print(elemento_eliminado)

del list1[1] # elimino el eleemnto de posición 1

print(list1)