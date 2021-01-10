#!/usr/bin/python
# -*- coding: utf-8  -*-

def introduce_resultado():
    # Pre: ninguna
    # Post: devuelve una tupála de valores. Nombre de equipos y fecha, texto.
    # Los resultados deben ser números enteros
    eqCasa = raw_input("Equipo de casa: ")
    eqVisitante = raw_input("Equipo visitante: ")
    resCasa = int(raw_input("Resultado equipo de casa: "))
    resVisitante = int(raw_input("Resultado equipo de casa: "))
    fecha = raw_input("Día en el que se jugó: ")
    return (eqCasa, eqVisitante, resCasa, resVisitante, fecha)


def guarda(nombre_fichero, datoIn):
    # pre: nombre de archivo válido, dato: tupla de datos de cinco elementos
    # post: se guardan valores en el archivo, separados por comas
    archivo = open(nombre_fichero, "a")
    archivo.write(datoIn[0] + "," + datoIn[1] + ","+ str(datoIn[2]) +
         "," + str(datoIn[3]) + "," + datoIn[4] + "\n")
    archivo.close


def recupera(nombre_fichero):
    # pre: nombre de archivo válido con la estructura de datos correcta
    # post: presentar las líneas con los datos
    archivo = open(nombre_fichero, "r")
    for linea in archivo:
        linea = linea.rstrip("\n")
        print linea
    archivo.close()

# Programa principal
nombre = "resultados.txt"

centinela = "n"
while centinela == "n":
    print "Guarda un dato: "
    dato = introduce_resultado()
    guarda(nombre, dato)
    centinela = raw_input("¿Quieres salir [s] ? ")
    if centinela.lower() == "s":
        break
    else:
        centinela = "n"

recupera(nombre)





