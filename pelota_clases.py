# *-* coding:utf-8 *-*
# EMPAQUETAR TUPLAS
lista1 = ["Hola", 103, 10.003]

dia = 10
mes = "Junio"
anno = 2015

fecha = dia, mes, anno

print fecha

# DESEMPAQUETAR TUPLAS
dia2, mes2, anno2 = fecha
print dia2
print ("En el mes de %s") % (mes2)
print ("dentro de dos años %d") % (anno2 + 2)

print lista1
lista1[0]="Adiós"
lista1[2] += 10
print lista1[2]
