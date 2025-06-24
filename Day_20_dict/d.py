# Dictoary
# d1={1:'one',2.5:2,3+9j:3}
# d1[4]='four'
# print(d1)
# d1[1]='Ace'
# print(d1)
# l1=[]

# d1={'name':'Ganesh','age':21,'add':'Angalakuduru'}
# print('Hi every one i am ',d1['name'])

l1=[[1,'one'],[2,'two'],[3,'three']]
d1=dict(l1)
print(d1)

l2=[1,2,3,4]
l3=['one','two','three','four']
d2=dict(zip(l3,l2))
print(d2)

s1='apples'
s2='python'
d3=dict(zip(s2,s1))
print(d3)


l4=['one','two','three','four']
d4=dict(enumerate(l4,start=int(False)))
print(d4)

d5={}
print(type(d5),d5.__sizeof__())
