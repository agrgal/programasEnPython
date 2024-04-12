# Ejemplo de context manager protocol.
# El objeto debe instanciarse primero, o bien se usa
# with ContextManagedClass() as cmc: - Fijarse en los paréntesis -
# o bien se crea una instancia primero. Ver el programa
class ContextManagedClass(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print("__enter__")
        return True

    # Args exception type, exception value and traceback
    def __exit__(self, *args):
        print('__exit__:', args)
        return True

    def __str__(self):
        return 'ContextManagedClass object'


print("Empezamos")

with ContextManagedClass() as cmc:
    print("Este es el objeto ", cmc)
    print("Salimos...")

print("Terminado")

instancia1 = ContextManagedClass()
with instancia1 as cmc2:
    print("Este es el objeto ", cmc2)
    print("Salimos...")