# *-* coding: utf-8 *-*
# Muestra 0,1,2,3,4

count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Muestra solo números impares - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x