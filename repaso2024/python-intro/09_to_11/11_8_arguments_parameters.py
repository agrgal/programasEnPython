def miFuncion(name, apellido, edad=25):
    """
    :param name: mi nombre
    :param apellido: mi apellido
    :param edad: mi edad, con valor por defecto, luego es opcional
    :return: nada
    """
    print("Mi nombre completo es {} {} y tengo {} años".format(name, apellido, edad))


# Los parámetros osn llamdos argumentos en las llamadas de las funciones
miFuncion(apellido="Gallardo", name="Aurelio")  # paso los argumentos con su valor
miFuncion("Aurelio", apellido="Gallardo", edad=53)  # esto es válido
# miFuncion(apellido="Gallardo", "Aurelio")  # ESTO NO ES VÁLIDO. Si empiezo a nombrar las claves de los argumentos, tengo que seguir haciéndolo.


