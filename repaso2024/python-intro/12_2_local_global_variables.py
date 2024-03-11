# diferencia entre variables globales y locales

def mi_func():
    a = 100  # defino la variable como local
    print(a)  # La función imprime la versión local


a = 5  # Defino la versión global de la variable
mi_func()
print(a)  # imprimo la versión global
