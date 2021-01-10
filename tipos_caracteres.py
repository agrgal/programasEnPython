# *-* coding: utf-8 *-*
def clinic():
    print "¡Acabas de entrar en la clínica!"
    print "¿Vas a ir por la puerta de la izquierda o la de la derecha?"
    answer = raw_input("Escribe izquierda o derecha y presiona 'Enter'.")
    if answer == "IZQUIERDA" or answer == "Izquierda" or answer == "izquierda":
        print "¡Este es el cuarto de abuso verbal, montón de estiércol de pájaro!"
    elif answer == "DERECHA" or answer == "Derecha" or answer == "derecha":
        print "¡Por supuesto que este es el Cuarto de Discusiones, sí ya se lo dije!"
    else:
        print "¡No escogiste izquierda ni derecha! Inténtalo otra vez."
        clinic()

clinic()