def xor(a, b):
  xor = False
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable xor
  # recuerda que los datos están en las variables a y b
  xor =((not a) and b) or ((not b) and a)
  return xor
  
a = True
b = True

print(xor(a,b))
