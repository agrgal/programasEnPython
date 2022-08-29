def velocidad(distancia, tiempo):
  resultado = ""
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable resultado
  # recuerda que los datos están en las variables distancia y tiempo
  tiempoHoras = tiempo/3600 #calculo en horas
  distanciaMetros = distancia * 1000
  resultado ="La velocidad es %.1f km/h o %.1f m/s" % (distancia/tiempoHoras, distanciaMetros/tiempo)  
  return resultado
  
tiempo = 1  #segundos
distancia = 0.01 #kilometros

print(velocidad(distancia,tiempo))
