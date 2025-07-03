l1=set([1,2,3,4,5,6,7])
it=iter(l1)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# genarator
r=iter(range(4))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

def myrange(a,b=1):
    i=0
    while i<a:
        yield i
        i+=b

for x in myrange(5,2):
    print(x)


# built math function:
# sum
# count
# max 
# min
# abs
# round
# divmod
# pow
# eval

L1=[1,2,3,4,5,6,7,8,9,10]
print(sum(L1)) 
# c=L1.count(0)
# print(c)
print(max(L1))
print(min(L1))
l2=[-1,-2,-3]
# l3=L1+abs(l2)
# print(l3)
print(round(15.5))
print(divmod(10,3))
print(eval('12*13'))
print(pow(7,5))

# object and attribute functions in python
print(type(10))
print(isinstance(10,int))
# hasattr
# getattr
print(id(l1))
# print(dir(str))
name=10
print(repr(name))

# Builtin itarators and sequence functions
sorted
reversed
slice
iter
next

a=sorted(L1,reverse=True)
print(a)
r=reversed(L1)
print(r)