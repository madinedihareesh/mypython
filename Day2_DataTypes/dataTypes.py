import sys
'''
In python there are types of data types:
1. numaric
    a.int (numbers)
    b. flot
    c. boolen
    d. complex
2. sequence
 a.string
3. sets
4.dict
'''
# int
i=2_34_56_789
print("This is a intiger",i)
print(type(i))
print(i.__sizeof__())
print(sys.getsizeof(i))

_i=-24567899
print("This is a negitive intiger")

#flot
f=1259E-3
print(f)

#boolen
t,f1=True,False
print("the value of true is",t)
print("The value of false is",f1)

#complex
#i=squrt(-1)
c=complex(12,9)
print(c)

'''desimals
1.decimal {0,1,2,3,4,5,6,7,8,9}
2.binary(2) {0,1}
3.octa(8) {0,1,2,3,4,5,6,7}
4.hexa(16) {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}'''

#Base Conversion
print(bin(10))
print(oct(10))
print(hex(10))

#string 
s="my name is ganesh"
print(type(s))
print(len(s))
print(s.__sizeof__())
print(dir(str))
