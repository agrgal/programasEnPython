# *-* coding: utf-8 *-*

print "Otra serie de números impares"
# Muestra solo números impares - 1,3,5,7,9
for x in xrange(0, 42):
    if x % 2 == 0:
        continue
    print x