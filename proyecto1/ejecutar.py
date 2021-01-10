# -*- coding:latin1 -*-

import funciones.persistencia_csv as csvfunc
valores = [("Concha", 456, "4:16"), ("Luis", 23, "18:42")]
csvfunc.guardar_puntajes("puntajes.txt", valores)
recuperado = csvfunc.recuperar_puntajes("puntajes.txt")
print recuperado


