# Problema de las variables globales y locales

def mi_func():
    global mm  # Defino la variable global mm, es decir, tomará el valor global antes definido mm=5
               #  Si comento esta lineal global, incluso indica error, porque mm no estaría definida
    mm = mm + 1  # sumo uno.
    print(mm)  # Imprimirá la variable global


mm = 5
print(mm)  # Devuelve 5
mi_func()  # sumará 1 a mm y devolverá 6
print(mm)  # No cambia, devuelve 6
