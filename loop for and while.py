# Exercise 1
for i in range(1, 11):
    print(i)

# Exercise 2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Exercise 3
num = int(input("Enter a number: "))
sum_of_numbers = 0
while num > 0:
    sum_of_numbers += num
    num -= 1
print(f"The sum of natural numbers is: {sum_of_numbers}")

# Exercise 4
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)

# Exercise 5
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"The factorial is: {factorial}")

# Exercise 6
num_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b

# Exercise 7
num = int(input("Enter a number: "))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(f"The reversed number is: {reverse_num}")

# Exercise 8
string = "Hello World"
vowels = "AEIOUaeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"The number of vowels is: {count}")

# Exercise 9
num = int(input("Enter a number: "))
original_num, reversed_num = num, 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# Exercise 10
sum_of_squares = 0
for i in range(1, 6):
    sum_of_squares += i**2
print(f"The sum of squares is: {sum_of_squares}")
