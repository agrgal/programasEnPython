# usando funciones decoradores

def rec(active=True):
    def recuadrar(func):
        def funcion_recuadrar():
            print("=" * 25)
            func()
            print("=" * 25)

        if active:
            return funcion_recuadrar
        else:
            return func

    return recuadrar


@rec()
def target1():
    print("Este es mi objetivo")


@rec(active=False)
def target2():
    print("Este es mi objetivo, pero no lo he conseguido")


target1()
target2()
