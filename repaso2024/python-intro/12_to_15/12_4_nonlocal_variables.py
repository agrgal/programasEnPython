# Definir funciones DENTRO de otra función
# Las variables son siempre LOCALES, dentro de cada función.
# Si quiero usar una variable en una función interior, dentro de otra función, ya no puedo llamarlas
# global, tengo que hacerlo nonlocal
def exterior():
    title = "Título exterior"

    def interior():
        nonlocal title  # Comentar, descomentar esta línea.
                        # Comentada, cad afunción toma la definición de su variable.
                        # Descomentada, title puede ser modificada DENTRO de la función anidada, con lo que cambiaría también en la exterior
        title = "Título interior"
        print(title)

    interior()
    print(title)


exterior()
