'''
def fun(*args):
   block of code
'''

def fun(*args,a,b):
   print(a,b,args)


fun(10,20,30,40,50,60,70,a=80,b=90)


'''
def fun(**kwargs):
    block of code
'''

def fun1(**kwargs):
   for item in kwargs.items():
      print(item[0],':',item[1])
      

fun1(name='sunil',age=22,place='nellor')   


def fun2(a,b):
   sum= a+b
   sub=a-b
   return sum,sub
   

print(fun2(10,20))


def fact(a):
   if a==0 or a==1:
      return 1
   else:
      return a*fact(a-1)
   

print(fact(10))   


