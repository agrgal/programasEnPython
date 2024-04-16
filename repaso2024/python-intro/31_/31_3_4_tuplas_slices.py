# slices en una tupla

class Person():
    pass

t1=(1,3,5,7,9,11,13,15)

print("t1[0]: ",t1[0])
print("t1[1]: ",t1[1])
print("t1[2]: ",t1[2])
print(t1[1:3]) # índice 1 al índice 2, no incluye el 3.

print(t1[:3]) # del principio hasta el 2
print(t1[2:]) # del 2 hasta el final
print(t1[::-1]) # al revés

tup2 = (1, 'John', Person(), True, 8,8)
print(tup2)

for i in tup2:
    print(i)

print(len(tup2))

print(tup2.count('John'))

print(tup2.index(8))

