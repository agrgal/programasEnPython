numero = int(input("Dime un número: "))
for i in range(1,numero+1):
  if i%2==0:
      continue
  if i%13==0 and i>13:
      break
  print("Este es un número impar {numero}.".format(numero=i))
else: # el else se ejecuta si llega a ejecutarse el FOR completamente.
    print("He impreso todos los números impares hasta llegar al {}".format(numero))
print("He terminado")