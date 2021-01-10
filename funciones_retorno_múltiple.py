# *-* coding: utf-8 *-*


def segA(sec):
    # Esta función es capaz de pasar los segundos
    # a horas minutos y segundos
    hs = sec / 3600
    minu = (sec % 3600) / 60
    seg = (sec % 3600) % 60
    return (hs, minu, seg)

segundos = int(raw_input("Introduce el números de segundos que han pasado: "))

(hora, minutos, segundos) = segA(segundos)
print ("%d:%d %d\"") % (hora, minutos, segundos)