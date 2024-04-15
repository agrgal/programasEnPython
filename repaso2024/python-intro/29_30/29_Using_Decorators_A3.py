# usando funciones decoradores

def recuadrar(func):
    def funcion_recuadrar(valor):
        print("=" * (len(valor)+15))
        func(valor)
        print("=" * (len(valor)+15))

    return funcion_recuadrar


@recuadrar
def target(valor):
    print("Este es mi " + valor)


t1 = target
t1("objetivo")
