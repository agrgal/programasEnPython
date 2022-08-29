def buscaminas(tablero,i,j):
	minas=0 #número de minas inicial
	longitud=len(tablero)
	for n in range(i-1,i+2):
		for m in range (j-1,j+2):
			if not (n==i and m==j) and n>=0 and n<longitud and m>=0 and m<longitud and tablero[n][m]=="X":
				minas=minas+1	
	return minas# El elemento 0 pero invertido


tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

for i in range(0,4):
	for j in range(0,4):
		print("fila: "+str(i)+ " // columna: "+str(j)+" --> "+str(buscaminas(tablero,i,j)))
		
