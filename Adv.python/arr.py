import array

a=array.array('i',[1,2,3,4,5])

a.append(6)
print(a)
a.extend([7,8,9,10])
print(a)

str1=b'abcdef'

a1=array.array('b',str1)
print(a1)

print(sum(a))