print('#{:25}#'.format('mi frase'))

print('|{:<25}|'.format('izquierda')) # por defecto alineación izquierda
print('|{:>25}|'.format('derecha')) #alineación derecha
print('|{:^25}|'.format('acentros')) #alineación izquierda

print('{:,}'.format(123456789)) # formato numérico con separador de miles
print('{:,}'.format(1234.56789)) # formato numérico con separador de miles
print('{:,}'.format(123456789.45)) # formato numérico con separador de miles

print('{:25,}'.format(123456789)) # formato numérico con separador de miles
print('{:25,}'.format(1234.56789)) # formato numérico con separador de miles
print('{:25,}'.format(123456789.45)) # formato numérico con separador de miles