# ejemplo de diccionario

# note keys are not strings
dict1 = dict(uk='London', ireland='Dublin', france='Paris')
print('dict1:', dict1)

# añadiendo (mismo método de asignación para modificar)
dict1['españa'] = 'Madrid'
dict1['portugal'] = 'Lisboa'

# borrando
dict1.pop('uk')  #  o bien, del pero sin devolver valor. clear borra el diccionario.

print(dict1)
# iterando
for clave in dict1:
    print("Mi clave es: ",clave," y mi valor: ",dict1[clave])

for valor in dict1.values():
    print("Directamente el valor: ",valor)

print(dict1.items())
