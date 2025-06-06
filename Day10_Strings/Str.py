# s1='Malayalam'


# print('X' not in s1)

# #find
# str1='Hi, Hello Welcome to the world'

# print(str1.find('o',15,)) 

# #rfind
# print(str1.rfind('k'))

# #index
# print(str1.rindex('H'))

# #count
# print(str1.count('o'))

# #ljust
# print(str1.ljust(40,' '))

# #rjust
# print(str1.rjust(40,'$'))

# #center
# print(str1.center(40,'*'))

# #zfill
# print(str1.zfill(40))

#strip
str2='   Welcome to Python   '
print(len(str2))

x=str2.strip()
print(len(x))
print(x)

# lstrip
str3='   welocme to python'
r=str3.replace(' ','*')
print(r)
print(len(str3))
x1=str3.lstrip()
print(len(x1))

# replace
str4='a,b,c,d'
r1=str4.replace(',','-',2)
print(r1)

# join 
s1='Ganesh'
s2='I am from tenali'
out=s1.join(s2)
print(out)

# startswith
s3='Python is simple'
out1=s3.startswith('Python is')
print(out1)

# endswith
out2=s3.endswith('e')

# removeprefix
out3=s3.removeprefix('Python ')
print(out3)
# removesufix
out4=s3.removesuffix('e')

# partisiton
s4='kireety@gmail.comsurya@gmail.com'
_1=s4.partition('@')
print(_1)
_2=s4.rpartition('@')
print(_2)

# lower
s5='ACHIEVERSIT'
print(s5.lower())

# upper
s6='achieversit'
print(s6.upper())

#captalize

s7='hi hello a very good mmorning'
print(s7.capitalize())

# title
print(s7.title())

# swapcase
s8='aChIeVeIrSiT'
print(s8.swapcase())

# isalpha
s9='BalaGanesh'
print(s9.isalpha())

# isdigit
s10='100'
print(s10.isdigit())

# isalnum
# islower
# isupper
# isspace
# istitle

# isinstance
s11=[10,11,12,13]
print(isinstance(s11,list))

# identifier oparators
# is and is not
name1='Ganesh'
name2='Ganesh1'
print(id(name1))
print(id(name2))
print(name1 is not name2)

# split
s12='john,smith,james'
print(s12.split(','))
# retuns in list
# split(char,repetation count)
print(s12.split(',',1))
