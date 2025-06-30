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


'''
1. only positonal arrguments
2. only keyword arrguments
'''

def volofsqr(s,/):
    vol=s**2
    return vol

print('The area of a squre is',volofsqr(5))
# print('The area of a squre is',volofsqr(s=6))

def voloftriangle(base,/,height):
    vol=(base*height)*0.5
    return vol

print(voloftriangle(6,height=10))

'only keyword arr'
def areaoftrep(breth,height,/,*,length):
    vol= length*breth*height
    return vol

def addoflist(a):
    sum=0
    for x in a:
        sum+=x
    return sum

List=[1,2,3,4,5]
s='python'

print(addoflist(List))
# print(addoflist(s))


def fun2(a,b,/,c,d,*,e,f):
    print('hello')
