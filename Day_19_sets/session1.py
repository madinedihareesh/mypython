# set
# Creating set
# s1={1,2,3,4,56,34+11j,'ganesh',1}
# print(type(s1),s1)
# s2=set([1,2,3,4,5])
# print(type(s2),s2)
# s3=set('python')
# print(type(s3),s3)
# s4={5} 
# print(type(s4))
# s5=set()
# print(type(s5),s5)

# s1={1,1,2,3,4,5,6}
# s1.pop()
# s2=set('python')
# for x in s2:
#     print(x)



# print(s1)


# s3={23,44,56,79,60,12}
# print(s3)
# s3.pop()
# print(s3)

# s4={5,10,21,15,3,11}
# s4.pop()
# print(s4)

'''
1.union
2.intersetion
3.diffrence
4.symmetic diffrence
5.intersection_update
6.diffrence_update
7.symmetic diffrence _update
'''

s1={1,2,3,4,5,6,7,8,9,10}
s2={1,2,3,4,5}
s3={4,5,8,9,10}

print(s2.union(s3))
print(s2.intersection(s3))

# s2.intersection_update(s3)
# print(s2)

print(s2.difference(s3))

# s2.difference_update(s3)
# print(s2)

print(s2.symmetric_difference(s3))

s1.add(11)
print(s1)

s1.update('python')
print(s1)

s1.pop()
print(s1)

s1.remove('o')
print(s1)

s1.clear()
print(s1)

del s1
# print(s1)

print(s2|s3)
print(s2&s3)
# s2&=s3
# print(s2)
print(s2-s3)
s2-=s3
print(s2)
s2^=s3
print(s2)


