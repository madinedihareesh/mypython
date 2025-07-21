#functions are also objects:
show=print
show('hello world')

# nested functions:
def dia(l,h,b):
    d1=l*h
    d2=h*b
    d3=l*b
    def area():
        vol=2*(d1+d2+d3)
        print(vol)
    area()

dia(3,4,5)    


