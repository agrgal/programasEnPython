s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}

print("Unión: ", s1 | s2)  # elementos de los dos conjuntos no repetidos
print("Intersección: ", s1 & s2)  # elementos comunes

print("Diferencia: ", s1 - s2)  # diferencia: quita de s1 los elementos de él que estén en s2

print("Diferencia simétrica: ", s1 ^ s2)  # diferencia simétrica: la unión de los dos menos la intersección
print("Diferencia simétrica: ", (s1 | s2) - (s1 & s2))
