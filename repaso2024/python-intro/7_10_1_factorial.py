# Cálculo del factorial de un número
otro ='s'

while otro=='s':
    num = int(input("Dime un número: "))
    if num<0:
        print ("No puedo calcular el factorial de un número negativo")
    elif num==0:
        print("El factorial del número {n} es {res}".format(n=num,res=1))
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact*i
        print("El factorial del número {n} es {res}".format(n=num,res=fact))
    otro=input("¿Quieres calcular otro factorial? [s/n]: ")