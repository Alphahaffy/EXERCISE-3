# Assignment
#CLASS TASK
#EXERCISE 1

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#EXERCISE 2

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


#EXERCISE 3
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#EXERCISE 4
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")

#EXERCISE 5
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


#EXERCISE 6
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
max_number = max(num1, num2, num3)
print("The maximum number is:", max_number)


#EXERCISE 7
score = float(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


#EXERCISE 8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")

#EXERCISE 9 SAME AS EXERCISE 2
#EXERCISE 10
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The larger number is:", num1)
elif num1 < num2:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal.")
    #COMPLETED KINDLY GIVE ME FEEDBACK 03077330099 HAFEEZ REHMAN AI27

