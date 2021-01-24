# *-* coding: utf-8 *-*

import math

# http://csis.pace.edu/~wolf/CS122/infix-postfix.htm
# http://hawkee.com/snippet/16636/

# Funciones

def esFloat(a):
    try:
        float(a)
        return True
    except:
        return False

# Fin de funciones

radOGrados=raw_input("Pulsa r para radianes y g para grados: ")
radOGrados=radOGrados[0:1].lower()

if radOGrados=="g":
	factor=4*math.atan(1)/180
else:
	factor=1

seguir = True
while seguir:
   
    cadena=raw_input("Introduce una cadena con operadores válida: ")

    operadores=["+","-","*","/","^","(",")","sin","cos","tan","sec","cosec","cotan","ln","log","exp","sqr","abs","asin","acos","atan"]
    prefoper=[0,0,1,1,2,-1,-1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    stack=[]
    postfix=""

    # =====================================
    # Pretratamiento para números negativos
    # =====================================
    cadena2=""
    previo=""
    bandera = 0
    for i in cadena:
        if ((i=="-" or i=="+") and (previo in operadores or previo=="" or not esFloat(previo)) 
			and previo!="e" and previo!=")" and bandera==0):
            cadena2+="(0"+i
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

    print "Esta es la cadena a convertir: %s" % (cadena2)

    bandera = 0

    for count, i in enumerate(cadena2):
      
        if bandera>0:
            bandera-=1 # va restando 1
            continue # permite leer funciones
         
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
        elif (cadena2[count:count+3]=="sin"
            or cadena2[count:count+3]=="cos"
            or cadena2[count:count+3]=="tan"
            or cadena2[count:count+3]=="sec"
            or cadena2[count:count+3]=="log"
            or cadena2[count:count+3]=="exp"
            or cadena2[count:count+3]=="abs"
            or cadena2[count:count+3]=="sqr"): # si son estas funciones, las añade
            stack.append(cadena2[count:count+3])
            bandera=len(cadena2[count:count+3])-1
        elif (cadena2[count:count+4]=="asin"
            or cadena2[count:count+4]=="atan"
            or cadena2[count:count+4]=="acos"): # si son estas más largas, las añade también
            stack.append(cadena2[count:count+4])
            bandera=len(cadena2[count:count+4])-1
        elif (cadena2[count:count+5]=="cosec"
            or cadena2[count:count+5]=="cotan"): # si son estas más largas, las añade también
            stack.append(cadena2[count:count+5])
            bandera=len(cadena2[count:count+5])-1
        elif cadena2[count:count+2]=="ln": # si es el ln
            stack.append(cadena2[count:count+2])
            bandera=len(cadena2[count:count+2])-1
        elif cadena2[count:count+2].lower()=="pi": # si es el número pi
            postfix+=str(4*math.atan(1))
            bandera=len(cadena2[count:count+2])-1
        elif (cadena2[count:count+4].lower()=="10e-"
            or cadena2[count:count+4].lower()=="10e+"): # si es exponente positivo o negativo
            postfix+="1"+cadena[count+2:count+4]
            bandera=len(cadena2[count:count+4])-1
        elif cadena2[count:count+3].lower()=="10e": # si es exponente positivo sin el signo más
            postfix+="1e"
            bandera=len(cadena2[count:count+3])-1
        elif i=="e" and (cadena2[count+1:count+2] in operadores[0:7] or cadena2[count+1:count+2]==""): # número e
            postfix+=str(math.exp(1))
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
        # print cadena2.index(i), i, stack, postfix

    # termina añadiendo el stack a la cadena postfix
    while len(stack)>=1:
        if prefoper[operadores.index(stack[len(stack)-1])]>=0:
            postfix+=" "+stack[len(stack)-1]
        stack.pop()

    print "La cadena postfix: %s" % (postfix)

    # ============================
    # Cálculo de la cadena postfix
    # ============================

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
        elif item=="sin":
            calculo.append(math.sin(factor*calculo.pop()))
        elif item=="cos":
            calculo.append(math.cos(factor*calculo.pop()))
        elif item=="tan":
            calculo.append(math.tan(factor*calculo.pop()))
        elif item=="sec":
            calculo.append(1/math.cos(factor*calculo.pop()))
        elif item=="cosec":
            calculo.append(1/math.sin(factor*calculo.pop()))
        elif item=="cotan":
            calculo.append(1/math.tan(factor*calculo.pop()))
        elif item=="ln":
            calculo.append(math.log(calculo.pop()))
        elif item=="log":
            calculo.append(math.log10(calculo.pop()))
        elif item=="exp":
            calculo.append(math.exp(calculo.pop()))
        elif item=="asin":
            calculo.append(math.asin(calculo.pop())/factor)
        elif item=="acos":
            calculo.append(math.acos(calculo.pop())/factor)
        elif item=="atan":
            calculo.append(math.atan(calculo.pop())/factor)
        elif item=="abs":
            calculo.append(abs(calculo.pop()))
        elif item=="sqr":
            calculo.append(pow(calculo.pop(),0.5))
        elif esFloat(item):
            calculo.append(float(item))
        else:
            pass
         
        print calculo
      
    print "El resultado es: %.4f" % (calculo[0])
    
    seguir2 = raw_input("¿Quieres hacer otro cálculo? [s,n] ")
    if seguir2.lower()=="n":
		seguir = False
    
