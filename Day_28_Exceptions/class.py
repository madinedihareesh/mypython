'''
3 types:
1. syntax error
2. logical error
3. runtime error

exception:
try:
risky code c=a/b 
expect zerodivisionerror:
print('Enter a valid number except zero')
else:
print(c)
finally:
print('The code has been excuted)
'''
# sysntax error
# def Test():
#     print('This is a syntax error')

# Test()
# type error
# str1='abc'
# num1=10

# print(str1+num1)

# logical error

# try:
#     a=int(input('Enter the A value:'))
#     b=int(input('Enter the B value:'))
#     c=a/b
    
# except Exception as e :
#     print('Enter a valid number',e) 
# else:
#     print(c)
# finally:
#     print('The program has been completed')
    
#custom error raise
a= int(input('Enter your age'))

if a<18:
    raise('Invalid age')
else:
    print('Elisible to vote')