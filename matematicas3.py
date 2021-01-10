# -*- coding: utf-8 -*-

import random, statistics as st

# lista de números al azar 
numeros = random.sample(range(0,400),100)

print "Listado: ",numeros

# print st.mean.__doc__
print "Media de la lista: ", st.mean(numeros)
print "Varianza: ", st.variance(numeros)
print "Mediana: ", st.median(numeros)


	





	
