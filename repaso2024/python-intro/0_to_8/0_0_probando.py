# split
title = 'The Good, The Bad, and the Ugly'
print('Source string:', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))

print("Recuento de espacios:",title.count(' ')) #recuento de caracteres
title = title.replace("Good","very Good") #reemplazar textos
print(title)
print(title.find('very')) #encontrar la posición de una palabra.