s='\u0041\u0042\u0043'
print(s)

print(ord('a'))
print(chr(97))

# '''
# \n next line
# \t tab space
# \v vertical tab space
# \f line feed
# \a alert 
# \ single line
# \\ plain slash
# \' single qote
# \" double qote
# \r carrige return
# \o octa demial
# \x hexa decimal
# '''

print('hello \nworld')
print('hello',end='\n')
print('world')
print('hello\tworld')
print('hello',end='\t')
print('world')
print('hello\vworld')
print('hello',end='\v')
print('world')
print('hello\fworld')
print('hello',end='\f')
print('world')
print('hello\\world')
print('hello',end='\\')
print('world')
print('hello World\a')
print('this is one of my favorite thing\'s')
print("He told me that \"i am ok\"")
print('hello world\rwelcome')
print('hello world\b')

print('\N{rupee sign}')


print('hi',789,96.34,sep='A',end='\n',flush='')

item='sand disk'
size=32
price=500.15

print(item,'Hard Drive with',size,'size is pricing about',price,'rupees')

"""
%s string
%d decimal
%i intiger
%f flot
%F flot
%g genral flot
%o octa
%h hexa 
"""
print('%s Hard  drive with %d gb is pricing about %g rupees'%(item,size,price))

print('{1} hard drive {0} gb is priging about{2} rupees'.format(item,size,price))

print(f'{item} hard disk {size} gb is priging about {price} rupees')