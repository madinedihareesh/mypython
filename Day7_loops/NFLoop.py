
for i in range(1,101):
    count=0
    for j in range(1,i+1):
       if i%j==0:
        count+=1
    if count==2:
      print(i, 'is  a prime numbe')

print('---------------------') 

for i in range(1,6):
   for j in range(1,6):
      if i==j:
       print('$',end=' ')
      else:
        print('*',end=' ') 
   print(' ')  

print('---------------------')

for i in range(1,6):
  for j in range(1,6):
    if i>=j:
      print('*',end=' ')
  print(' ')    

print('-----------------')


for i in range(1,6):
  for j in range(1,6):
    if i>j:
      print(' ',end=' ')
    else:
      print('*',end=' ')  
  print(' ') 

print('-------------------')

for i in range(1,6):
  print('* '*i)

print('-------------------')

for i in range(5,0,-1):
  print('* '*i)


