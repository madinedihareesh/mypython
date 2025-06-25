# # Dictoary
# # d1={1:'one',2.5:2,3+9j:3}
# # d1[4]='four'
# # print(d1)
# # d1[1]='Ace'
# # print(d1)
# # l1=[]

# # d1={'name':'Ganesh','age':21,'add':'Angalakuduru'}
# # print('Hi every one i am ',d1['name'])

l1=[(1,'one'),(2,'two'),(3,'three')]
# d1=dict(l1)
# print(d1)

l2=[1,2,3,4]
l3=['one','two','three','four']
# d2=dict(zip(l3,l2))
# print(d2)

# s1='apples'
# s2='python'
# d3=dict(zip(s2,s1))
# print(d3)


l4=['one','two','three','four']
# d4=dict(enumerate(l4,start=int(False)))
# print(d4)

# d5={}
# print(type(d5),d5.__sizeof__())

# L1=[x for x in [1,2,3,4]]
# # T1=(*(x for x in (1,2,3,4)))
# s={x for x in }

# Dict Comprahensions
D1={x:y for x,y in l1}
print(D1)
D2={x:y for x,y in zip(l2,l3)}
print(D2)
D3={x:y for x,y in enumerate(l4,start=1)}
print(D3)
D4={6:'six'}
# methods()
k=D1.keys()
print(k)
for i in k:
    print(i)

v=D1.values()
print(v)
for i in v:
    print(i)

it=D1.items()
print(it)

a=D1.get(1)
print(a)
print(D1[1])
D1[5]='Five'
print(D1)
b=D1.setdefault(4,'Four')
print(D1)

D1.update(D4)
print(D1)

D5=dict.fromkeys(l2,'head')
print(D5)

D6=D5.copy()
print(D6)

D6.popitem()
print(D6)

D6.clear()
print(D6)

del D6
s=set()
print(s)