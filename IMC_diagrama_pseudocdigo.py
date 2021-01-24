# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20160408-l32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# El algoritmo no admite acentos
if __name__ == '__main__':
	print "Dime tu nombre, ","Dime tu altura en centmetros y ","Dime tu peso"
	nombre = raw_input()
	altura = float(raw_input())
	peso = float(raw_input())
	minombre = nombre
	mialtura = altura/100
	mipeso = peso
	indicemasacorporal = mipeso/(mialtura**2)
	print "Mi indice de masa corporal es ",indicemasacorporal
	# Se define un array con dimension 6. Los datos se introducen uno a uno...
	mislimitesinferiores = [float() for ind0 in range(6)]
	misdefiniciones = [str() for ind0 in range(6)]
	mislimitesinferiores[0] = 0
	misdefiniciones[0] = "delgadez"
	mislimitesinferiores[1] = 18.5
	misdefiniciones[1] = "peso normal"
	mislimitesinferiores[2] = 25
	misdefiniciones[2] = "sobrepeso"
	mislimitesinferiores[3] = 30
	misdefiniciones[3] = "obesidad"
	mislimitesinferiores[4] = 40
	misdefiniciones[4] = "obesidad morbida"
	mislimitesinferiores[5] = 1000
	misdefiniciones[5] = "limite inalcanzable"
	indice = 0
	while True:# no hay 'repetir' en python
		indice = indice+1
		if mislimitesinferiores[indice-1]>=indicemasacorporal: break
	resultado = misdefiniciones[indice-2]
	print minombre," presentas un estado de: ",resultado

