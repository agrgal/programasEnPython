"""This is a test module"""
"""Este módulo tiene un código ejecutable. Pero si lo llamo desde mi programa,
el código no se ejecuta, igual que le módulo1_BIS. Pero además la forma de escribirlo 
 con una función main() - principal - es la forma de PYTHON IDIOMÁTICO o PYTHONIC"""
print('Hello I am module 1')


def f1():
    print('f1[1]')


def f2():
    print('f2[1]')


def main():
    """Esto permite que se ejecute SOLO cuando es llamado de forma INDEPENDIENTE, STANDALONE"""
    x = 1 + 2
    print('x is', x)
    f1()
    f2()


if __name__ == '__main__':
    main()
