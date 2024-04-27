# list comprenhension

l1 = [1, 2, 3, 4, 5]
print(l1)

l2 = [item*item for item in l1]
print(l2)

l3 = [item*item for item in l1 if item%2 != 0]  # filtra y solo lo aplica con los impares
print(l3)