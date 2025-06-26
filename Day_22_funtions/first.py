# functions:

'''
()
print()
id()
type()
len()
range()
....

syntax:
def name(parameters):
    ---------------
    ---------------
    ---------------
    ----------------
    return ......

range(stop=10)    
'''

l1=[1,2,3,-4,5]

l2=sorted(l1)
print(l2)

def add(a,b):
    rel=a+b
    return rel

print(add(5,6))    


print(add(b=7,a=10))


def volrec(l=10,b=20):
    vol = l*b
    return vol

print(volrec(b=40))


def write():
    print('Hello World')


write()