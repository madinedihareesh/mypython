# import statements
import re as Regex



# Regex Methods
# match
print(Regex.match('abc','abcghefabc'))

# fullmatch
print(Regex.fullmatch('Python is easy','Python is easy'))
# search
print(Regex.search('can','i can do this thing').span())
# findall
print(Regex.findall('can','can can a can is a cancer'))
# split
print(Regex.split(' ','My name is Amardeep'))
# group
# span

# Quantifiers
# + 1 or more
# * 0 or more
# ? 0 or 1
# {m} not less or not more
# {m,n} from m to any point in between n {10,20}

# 0-9
# a-z
# A-Z


# Special Charaters
# [] [0-9a-zA-Z]
print(Regex.fullmatch('[0-9a-zA-Z]+','098765432asdfghjklASDFGH'))
# [^]
print(Regex.fullmatch('[^a-z0-9 ]*','HIMYNAMEISHAREESH@#$%&*'))
# .
print(Regex.fullmatch('[a-zA-Z0-9$#. ]*','Hi my name is Ganesh \nmy age is 21yrs old'))
# ^[]
print(Regex.fullmatch('^[A-z]{1}[a-z]*','Ganesh Bala'))
# $
# email=input('Enter your emailID: ')
# print(Regex.fullmatch('[a-z0-9_\.]*@{1}[a-z]{5}\.com{1}',email))
# R|S
print(Regex.fullmatch('gmail|yahoo','ganesh'))



# sequence
'''
\d [0-9]
\D ^[0-9]
\w  Alphanumaric
\W  Non-AlphaNumaric(specialCharecters)
\s  whitespaces
\S  
\A  starting
\Z  ending
'''
print(Regex.fullmatch('[\w.]*@(gmail|yahoo|outlook){1}\.com{1}','achieversit@gmail.com'))

