# usando funciones decoradores

def recuadrar(func):
    def funcion_recuadrar():
        print("=" * 25)
        func()
        print("=" * 25)

    return funcion_recuadrar


@recuadrar
def target():
    print("Este es mi objetivo")


t1 = target
t1()
