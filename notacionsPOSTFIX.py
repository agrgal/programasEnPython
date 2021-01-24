# *-* coding: utf-8 *-*

# http://csis.pace.edu/~wolf/CS122/infix-postfix.htm
# http://hawkee.com/snippet/16636/

def esFloat(a):
	try:
		float(a)
		return True
	except:
		return False

# Funciones

cadena=raw_input("Introduce una cadena con operadores válida: ")

operadores=["+","-","*","/","^","(",")"]
prefoper=[0,0,1,1,2,-1,-1]
stack=[]
postfix=""

# =====================================
# Pretratamiento para números negativos
# =====================================
cadena2=""
previo=""
bandera = 0
for i in cadena:
	if i=="-" and (previo in operadores or previo=="") and bandera==0:
		cadena2+="(0-"
		bandera=1
	elif i in operadores and bandera==1:
		cadena2+=")"+i
		bandera=0
	else:
		cadena2+=i
	previo = i

if bandera==1:
	cadena2+=")"
# ======================
# Fin del pretratamiento
# ======================

print "Esta es la conversión: %s" % (cadena2)

for i in cadena2:
	if i in operadores and prefoper[operadores.index(i)]>=0: # todos menos los paréntesis
		indice = operadores.index(i) # indice del elemento nuevo
		# la 5ª regla, la potencia, se consigue con un while en la siguiente en vez de un if.
		while len(stack)>=1 and prefoper[indice]<=prefoper[operadores.index(stack[len(stack)-1])]: 
			# y la preferencia del operador es mayor que la del último del stack
			# el igual incluye la asociación, 4ª regla
			postfix+=" "+stack[len(stack)-1] # añade el último al postfix
			stack.pop() # quita de la pila el último
		stack.append(i) # añade el operador al stack
		postfix+=" "
	elif i=="(":
		stack.append("(") # añade el paréntesis al stack
	elif i==")":
		while len(stack)>1 and stack[len(stack)-1]!="(":
			postfix+=" "+stack[len(stack)-1] # añade al postfix
			stack.pop() # lo quita de la pila
		if stack[len(stack)-1]=="(":
			stack.pop() # lo quita de la pila
	else: # si no está en operadores o no son paréntesis
		postfix+=i
	# imprime la lectura de la cadena, la posición, la cadena postfix y el stack
	print cadena2.index(i), i, stack, postfix

while len(stack)>=1:
	if prefoper[operadores.index(stack[len(stack)-1])]>=0:
		postfix+=" "+stack[len(stack)-1]
	stack.pop()

print postfix

# =======
# Cálculo
# =======

pila=[]
pila=postfix.split(" ")
calculo=[]
# print pila

while len(pila)>0:
	
	item = pila.pop(0)
	# print item
	
	if item=="+" and len(calculo)>1:
		calculo.append(calculo.pop()+calculo.pop())
	elif item=="-" and len(calculo)>1:
		tmp = calculo.pop()
		calculo.append(calculo.pop()-tmp)
	elif item=="*" and len(calculo)>1:
		calculo.append(calculo.pop()*calculo.pop())
	elif item=="/" and len(calculo)>1:
		tmp = calculo.pop()
		calculo.append(calculo.pop()/tmp)
	elif item=="^" and len(calculo)>1:
		tmp = calculo.pop()
		calculo.append(pow(calculo.pop(),tmp))
	elif esFloat(item):
		calculo.append(float(item))
	else:
		pass
		
	print calculo
	
print "El resultado es: %.4f" % (calculo[0])


    




