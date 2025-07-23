from collections import Counter

L=['mark','james','mark','james','mathew','ben','mark']

c=Counter(L)
print(c)

print(c['mark'])
print(c.get('mark'))

c.update({'Andrew':4})

print(c)



print(c.most_common(2))
k=c.keys()
for i in k:
    print(i)

e=c.elements()
for i in e:
    print(i)    

v=c.values()
for i in v:
    print(i)    