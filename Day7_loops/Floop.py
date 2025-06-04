#range(start,end,step)
'''
for var in range(10,1,1)
'''
for i in range(1,11,3):
    print(i)

name='KundanRamCharan'
scount=0
for x in name:
    print(x)
    scount+=1
print('Total letters in the string',scount)      

factor=int(input("Enter the number to find the factors"))
count=0
for i in range(1,factor+1,1):
    if factor%i==0:
        print(i)
        count+=1
print("The number of factors for the given number",count)   

#0,1,1,2,3,5,8,13,21
'''
a=0
b=1
c=a+b
'''
fibb=int(input("Enter the limit of fibbonocci series"))
a=0
b=1
for i in range(0,fibb+1,1):
    print(a, end=' ')
    c=a+b
    a=b
    b=c

sumOfAll=0
for i in range(1,11):
    a=int(input('Enter the value'))
    sum+=a
           

    