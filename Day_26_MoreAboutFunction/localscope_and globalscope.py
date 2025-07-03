g=10
 
print(g) 
def fun():
    global g
    a=20
    g=200
    print(a)
    print(g)
    print(locals())
    print(globals())

fun()
print(g)
