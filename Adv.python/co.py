import copy

L=[1,2,3,4,5]
L1=copy.copy(L)

print(L1)

print(id(L[0]))
print(id(L1[0]))

L2=copy.deepcopy(L)
print(L2)
print(id(L2[0]))