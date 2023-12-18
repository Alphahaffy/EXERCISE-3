#QUESTION1

num1=int(input("ENTER A NUMBER:"))
num2=int(input("ENTER A NUMBER:"))
if num1%2!=0 and num2%2!=0:
    sum=num1+num2
    print("THE SUM IS:",sum)
else:
    print("YOU HAVE ENTERED A WRONG NUMBER")

#QUESTION2
num1=int(input("ENTER A NUMBER:"))
multiply=1
i=1
while i<=num1:
    multiply*=i
    i+=1
print("THE ANS IS",num1,multiply)



#QUESTION3


import random

for i in range(5):
    num = random.randint(1, 100)
    n = int(input("ENTER A NUMBER: "))
    
    if num == n:
        print("YOU WON")
        break
    elif num > n:
        print("YOU HAVE CHOSEN A LOW NUMBER :)")
    elif num < n:
        print("YOU HAVE CHOSEN A HIGH NUMBER :)")
        
print("NEXT TIME :)")


#QUESTION4

people=int(input("ENTER TOTAL NUMBER OF PEOPLES:"))
cost=int(input("ENTER TOTAL COST:"))
tax=float(input("ENTER TOTAL TAX IN %:"))
tip=float(input(("ENTER TIP IN %:")))

t_cost=people*cost
t_tax=(t_cost*tip)/100
t_tip=(t_cost*tip)/100
t_bill=(t_cost+t_tax+t_tip)
t_per_person=(t_cost+t_tax+t_tip)/people

print("TOTAL COST:",t_cost, "TOTAL TAX IS:",t_tax, "TOTAL TIP IS",t_tip,"TOTAL BILL IS:",t_bill)
print("TOTAL BILL AMOUNT PER PERSON IS:)",t_per_person)
    