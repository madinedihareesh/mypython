def hello():
    print('Hello world')

hello()

def world():
    return 'welcome to my world'


def voloftri(h,b):
    vol= (h*b)/2
    print(vol)

voloftri(20,15)

def voloftra(l,b,/,*,h):
    vol=l*b*h
    return vol

def fun(*bala):
    print(bala)


action=fun
             
L1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[10,11,12]]
fun(*L1,*l2)


def fun1(**ganesh):
    print(ganesh)

fun1(name='hareesh',age=60,place='hell')

show=print

show('i did it')


