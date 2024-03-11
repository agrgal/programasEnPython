# argumentos arbitrarios
# Usado cunado no sé cuántos argumentos pasará la función
# El parámetro es tratado como una lista

def misNombres(*mn):
    for i in mn:
        print(i, end=" ")
    print()

# Se puede pasar parámetro arbitario como pareja de valor clave - valor
def misNombres2(*mn, **otros):
    for i in mn:
        print("Nombres: ", i)
    for key in otros:
        print("Clave: ", key, " - Valor:", otros[key])


misNombres("Aurelio", "Maricarmen", "Luis", "Juan")
misNombres2("Aurelio", "Maricarmen", "Luis", "Juan", hijo="Alberto", hija="Luisa", nieto="Alfredo")
