'''
Creation of List
Hetrogenious
list is Mutable
indexing and slicing
List concatination and repetation
List Comparissions
List Traverals
Adding elements to tlist
.appentd(element)
Extend(itarable)
insert(index,element)
copy()
Removing Elements from List
.pop(index)
.remove
.clear
.del
Indexing,sort,reverse
.index(element,start,end)
.count()
.reverse()
.sort()
List Comprehensions
exp for item in ittarable
Nested List
'''

# L1=['ganesh','janani','rajesh','keerity','sirya']
# L2=[1,2,3,4,5,6,7]
# L3=[2.3,4.5,6.7]
# L4=[2+3j,9+10j,20+31j]
# L5=['ganesh',45,True,23.789,23+45j]

# Ways to create a list
# L1=[1,2,3,4,5]
# L2=list((1,2,3,4,5))
# print(L2)
# L3=list('python')
# print(L3)
# L4=[]

# slice
# L1=[1,2,3,4,5,6,7]
# L2=L1[0:5]
# print(L2)

# print(L1[1])
# L1[1]=8
# print(L1)
# L1[2:5]=[9,4,5,6]
# print(L1)
# L1[0]=[1,2,3,4]
# print(L1)

#  List Concatinations and Repitations
# L1=[1,2,3]
# L2=[4,5,6]
# L3=L1+L2
# print(L3)
# L4=L1*3
# print(L4)

# List Traverals
# L1=[1,2,3,4,5,6]
# print(len(L1))
# # meathod 1
# for x in L1:
#     print(x)

# for i in range(len(L1)):
#     print(L1[i])    

# Adding elements to tlist
# # append
# L1=[1,2,3,4,5,6]    
# L1.append([1,2,3])
# print(L1)
# # extend
# L1.extend([2,3,4,5])
# print(L1)
# # insert
# L1.insert(6,7)
# print(L1)
# # copy
# L2=L1.copy()
# print(L2)

# Removing Elements from List
L1=[1,2,3,4,5,6,7,8,9,0,5,6]
# POP()
L1.pop(0)
print(L1)
# remove
L1.remove(5)
print(L1)
L1.remove(5)
print(L1)
# clear
L1.clear()
print(L1)
# del
del(L1)

l1=['Kundan','hareesh']
l1[0]='Ramcharan'
print(l1)

l2=list('kundan')
print(l2)
l2[1]='a'
print(l2)

# Indexing,sort,reverse

# L1=[1,2,3,4,5,6,2,7,8]
# L3=L1[::-1]
# print(L3)
# L1.reverse()
# print(L1)
# print(L1.index(2,2,len(L1)))

# print(L1.count(2))

# L2=list('python')
# print(L2)


# L4=[70,10,30,60,20,50,40]
# L4.sort(reverse=True)
# print(L4)

# L5=['cat','dog','apple','bannana','Zeebra','Lion']
# L5.sort(key=len,reverse=True)
# print(L5)

# List Comprehensions
# syntax: exp for x in ittarable


# L1= [x for x in range(1,6)]
# print(L1)
# L2=[x**2 for x in range(1,6)]
# print(L2)
# L3=[x.upper() for x in 'python']
# print(L3)

# Nested List
L1=[1,2,3,4,[5,6,7]]
print(L1[4][0])
print(L1[0]+L1[1])

L1=[[],[],[]]
L1[0].extend([1,2,3,4])
L1[1].extend([5,6,7,8])
L1[2].extend([9,10,11,12])

for i in range(len(L1)):
    for j in range(len(L1)+1):
        print(L1[i][j],end=' ')
    print(' ')    

    

 