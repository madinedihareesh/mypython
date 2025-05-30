'''
there are two types 
1. While Loop
2. for loop

1. while loop
syntax:
while contioin:
    statement1
statement    
'''
#counter

n=0
while n<5:
    n=n+1
    print(n)

#sumation

s=int(input("Enter the number for sumation"))
i=0
sum=0
while i<s:
    i=i+1
    sum= sum+i
print("The sumation of the value you have entered is:",sum)    

d=int(input("Enter the vlue to print each digit: "))
while d>0:
    r=d%10
    print(r)
    d=d//10
    print(d)    

v=int(input("Enter the value for sumation of digits: "))
sum=0

while v>0:
    r=v%10
    print(r)
    sum+=r 
    v=v//10
    print(v)
print("the sum of digits in the value is", sum)    
