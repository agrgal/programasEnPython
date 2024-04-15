# usando funciones decoradores

def negrita(func):

    def poner_en_negrita(valor):
        print("<b>")
        func(valor)
        print("</b>")

    return poner_en_negrita

def recuadrar(func):
    def funcion_recuadrar(valor):
        print("=" * (len(valor)+15))
        func(valor)
        print("=" * (len(valor)+15))

    return funcion_recuadrar


@negrita
@recuadrar
def target(valor):
    print("Este es mi " + valor)


t1 = target
t1("objetivo")
