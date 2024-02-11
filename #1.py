#1
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2
    
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior Citizen")


#3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("Larger number:", num1)
else:
    print("Larger number:", num2)

#4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)
print("Maximum:", maximum)
print("Minimum:", minimum)

#5
score = float(input("Enter your exam score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#6
    
unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))
total_cost = unit_price * quantity
if total_cost > 1000:
    total_cost *= 0.9  
print("Total cost:", total_cost)


#7

temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 20:
    print("You should wear a jacket.")
else:
    print("You don't need to wear a jacket.")


#8
    
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


#9
    
pin = input("Enter your PIN: ")
correct_pin = "1234"
balance = 1000
if pin == correct_pin:
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN.")

#10
month = int(input("Enter the month (as a number): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month")











   


