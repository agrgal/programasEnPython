# solo se pueden incluir en set inmutables

set1 = { "árbol","abedul","roble"}
set2 = {"conífera","pino","haya"}
tup1 = (3,4,5)

set1.add(tup1)
print(set1)

# set1.add(set2) --> no se puede hacer. provoca un error

# Pero sí
set1.add(frozenset(set2))
print(set1)