# -*- coding: utf-8 -*-

import clases.misclases as miclase

# =========================
# Funciones
# =========================

def introducir():
	t = 5
	while t>0: 
		try:
			print ("Tienes %d oportunidades de introducir un dato correcto: ") % (t)
			numerador = int(raw_input("Introduce numerador: "))
			denominador = int(raw_input("Introduce numerador: "))
			a = miclase.fraccion(numerador, denominador)
			return a
		except ZeroDivisionError:
			print ("El denominador no puede ser cero\n")
			t = t - 1
		except TypeError:
			print ("No has introducido un tipo correcto. Debe ser entero\n")
			t = t - 1
		except ValueError:
			print ("No has introducido un valor entero\n")
			t = t - 1
		except Exception, ex:
			print ("Error producido :") + str(ex)
			raise
	raise ValueError, "Has tenido cinco oportunidades de introducir un dato correcto"


# =========================
# Programa principal
# =========================


print "Introduce fracción primera: "
f1 = introducir()
print "primera fracción:", f1, "\n"

print "Introduce fracción segunda: "
f2 = introducir()
print "segunda fracción:", f2, "\n"
		
f1.reducir()
print "primera fracción reducida:", f1, "\n"
f2.reducir()
print "segunda fracción reducida:", f2, "\n"

print "Inversa 1ª fracción reducida:", f1.inversa(), "\n"
print "Inversa 2ª fracción reducida:", f2.inversa(), "\n"

print "Suma de las dos: ", f1 + f2, "\n"
print "Resta de las dos: ", f1 - f2, "\n"
print "Multiplicar las dos: ", f1 * f2, "\n"
print "Dividir las dos: ", f1 / f2, "\n"
