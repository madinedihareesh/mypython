# # def hello():
# #     print('Hello world')

# # hello()    

# def add(a,b):
#     sum=a+b
#     return sum
# print(add(10,20))

# def greet(person=1):
#     print('welcome to',person)

# greet(10)

# print(add(b=20,a=10))

# l1=[1,2,3,4,5,6,7,8,9]
# it=iter(l1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# def myrange(stop,step=1):
#     i=0
#     while i<stop:
#         yield i
#         i+=step

# print(myrange(11,2))

# msg='helloworld'
# def fun():
#     global msg
#     msg='welcome world'
#     print(msg)

# fun()
# print(msg)


# show=print

# show('hello world')

# def area(l,b,h):
#     d1=l*b
#     d2=l*h
#     d3=b*h
#     def volume():
#         vol=2*(d1+d2+d3)
#         return vol
#     return volume

# f=area(4,5,6)
# print(f())

#Functions as parameters
def add(a,b):
    sum=a+b
    return sum

def maths(f,a,b):
    result=f(a,b)
    return result

A=maths(add,10,20)
print(A)

def outter():
    msg='hi'
    def inner():
        print('+'*10)
        print(msg)
        print('+'*10)
    return inner

I=outter()
print(I())

def get_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter

g=get_counter()
g1=get_counter()
print(g(),g(),g())
print(g1(),g1())

def greet(f):
    def inner():
        print('+'*10)
        f()
        print('+'*10)
    return inner
@greet
def display():
    print('Welcome to world')

display()

def sqr(a):
    print(a**3)

sqr(10) 

sq1=lambda x: x**2
print(sq1(10))

L1=[1,2,3,4,5,6,7,8,9]
Lsq=list(map(lambda x: x**2,L1))
print(Lsq)

e=list(filter(lambda x:x%2==0,L1))
print(e)
