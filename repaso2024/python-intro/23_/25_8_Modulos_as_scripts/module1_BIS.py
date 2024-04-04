"""This is a test module"""
"""Este módulo tiene un código ejecutable. Pero si lo llamo desde mi programa,
el código no se ejecuta, """
print('Hello I am module 1')

def f1():
    print('f1[1]')


def f2():
    print('f2[1]')


if __name__ == '__main__':
    """Esto permite que se ejecute SOLO cuando es llamado de forma INDEPENDIENTE, STANDALONE"""
    x = 1 + 2
    print('x is', x)
    f1()
    f2()
