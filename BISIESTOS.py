# *-* coding:utf-8 *-*
a = int(raw_input("Dime el año (después de Cristo): "))

if a>0:
	multiplo4 = (a % 4==0) # si lo es	
	multiplo100 = (a % 100==0) # no lo es
	multiplo400 = (a % 400==0) # si lo es
	# print multiplo4 and multiplo400
	# print multiplo4 and not multiplo100	
	# calculo = (multiplo4 and multiplo400) or (multiplo4 and not multiplo100)
	# print calculo
	if (multiplo4 and multiplo400) or (multiplo4 and not multiplo100):
		print "El año es BISIESTO"
	else:
		print "No, no... Este año no es bisiesto"
else:
	print "Todos los años a partir del 0"
