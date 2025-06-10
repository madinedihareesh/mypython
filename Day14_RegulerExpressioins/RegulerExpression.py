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
# .

# Special Charaters
# [] [0-9a-zA-Z]
print(Regex.fullmatch('[0-9a-zA-Z]+','098765432asdfghjklASDFGH'))
# [^]
# .
# ^[]
# $
# R|S
