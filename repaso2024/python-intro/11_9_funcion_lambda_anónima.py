# Funciones anónimas, lambda

# Notación: lambda argumento1, argumento2,... : expresion
# Retornan un valor que se asigna a una variable

cuadrado = lambda x: x * x
modulo = lambda x, y: (x * x + y * y) ** 0.5
print(cuadrado(14))
print(modulo(3, 4))

# ¿Reutilizables? Sí ,lo son
print(cuadrado(100))
print(modulo(9, 4))
