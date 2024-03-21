# Cálculo de los números primos en un rango
otro='s'
while otro=='s':
    num = int(input("Dime un número mayor que 1: "))
    n=0
    if num>=2:
        for i in range(2,num):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                n+=1
                print("El número {primo} es primo en el lugar {n}º".format(primo=i,n=n))
    else:
        print("No puedo calcular en un rango menor o igual a 1")
    otro=input("¿Quieres calcular otro factorial? [s/n]: ")