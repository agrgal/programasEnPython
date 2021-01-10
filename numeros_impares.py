# *-* coding: utf-8 *-*
# Muestra los primeros 20 números impares
print "Primera serie de números impares"
count = 0
while True:
    print count * 2 + 1
    count += 1
    if count > 20:
        break

print "Segunda serie de números impares"
# Muestra solo números impares - 1,3,5,7,9
for x in xrange(0, 1001):
    print x * 2 + 1
    if x == 20:
        break