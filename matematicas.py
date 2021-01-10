# -*- coding: utf-8 -*-

import math

# lista =  dir(math)

numberpi = 4 * math.atan(1)

t = True

while t:
	try:
		x = float(raw_input("Dime un ángulo entre 0 y 360: "))
		t = False
	except Exception, ex:
		print "Error " + str(ex)
	
angrad = x * numberpi / 180
print "En radianes: ", angrad, "rad"
print "Coseno del ángulo: ",math.cos(angrad)
print "Seno del ángulo: ",math.sin(angrad)	
print "Tangente del ángulo: ",math.tan(angrad)	



	
