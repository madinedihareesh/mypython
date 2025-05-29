#if condition
'''
if condition:
    statement
'''

marks=int(input("Enter the marks"))
if marks>=35:
    print("the above entered marks is pass",marks)

#if elase
'''
  if condtion:
      statement
  else:
      statement    
'''

flip=input("Enter the flip side")

if flip=='head':
    print("The flip side is head")
else:
    print("the flip side tails")    


#elif

BillAmount=int(input("Enter your billing amount with in 5000"))

if BillAmount>1000 and BillAmount<1500:
    discount=BillAmount*0.1
    print("final priceis",(BillAmount-discount))
elif BillAmount>=1500 and BillAmount<2000:
    discount=BillAmount*0.15
    print("final price is:",(BillAmount-discount))
elif BillAmount>=2000 and BillAmount<5000:
    discount=BillAmount*0.25 
    print("final price is ",(BillAmount-discount))
else:
    print("No discount")
 

#Nested if
'''
 if condition:
    if condition:
       statement
    else:
        statement
else:
    if condition:
       statement
    else:
        statement           
'''
natural=int(input("Enter natural number"))

if natural>0:
    if natural%2==0:
        print("the NUmber you have entered is:",natural,"is a even")
    else:
         print("the NUmber you have entered is:",natural,"is a odd")    
else:
    print("please enter a valid natural number")         

#Match
'''
 match input:
    case o:
         print("")
    case 1:
         print("")     
'''    

dayno=int(input("Enter the number in betwen 1-7"))

match dayno:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuseday")
    case 4:
        print("wed") 
    case 5:
        print("Thrus") 
    case 6:
        print("Fri")
    case 7:
        print("sat")
    case _:
        print("Enter a number between 1-7")                          