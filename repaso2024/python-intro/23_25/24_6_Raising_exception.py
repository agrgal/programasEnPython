# Usando raise para levantar excepciones

def mi_funcion():
    print("Empiezo la función")
    # raise ValueError("!Bang")  # provoco una excepción
    raise ValueError  # que puede escribirse simplemente así, sin pasarle un valor
    print("Acabo la función")  # Me avisa pychram que este código no puede alcanzarse


try:
    mi_funcion()
except ValueError as eee:
    print("Aquí hay un error....")
    print(eee)
    raise  # propagamos el error a otra parte del programa. En este caso se lanzará a la salida estándar
