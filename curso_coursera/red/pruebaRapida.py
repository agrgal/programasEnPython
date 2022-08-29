s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i<len(s):
  resultado= resultado + s[len(s)-i-1]
  i=i+1
print(resultado)
