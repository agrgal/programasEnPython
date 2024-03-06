edad = int(input("Dime una edad: "))

condicion = "Mayor de edad" if edad>=18 else "Menor de edad"
print(condicion)

trabajo = "No puede trabajar" if edad<=18 else ("Puede trabajar" if edad>=18 and edad<=65 else "Puedes jubilarte")
print(trabajo)