#1
def word_counter(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word = word.strip(".,!?;:\"")
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
def main():
    sentence = input("Enter a sentence: ")
    counts = word_counter(sentence)
    print("Word Counts:")
    for word, count in counts.items():
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()

#2

num_subjects = int(input("num of subjects: "))
total_score = 0
max_score = num_subjects * 100
for i in range(num_subjects):
    score = float(input(f" score for subject {i + 1}: "))
    total_score += score
percentage = (total_score / max_score) * 100
if 90 <= percentage <= 100:
    overall_grade = "A"
elif 80 <= percentage < 90:
    overall_grade = "B"
elif 70 <= percentage < 80:
    overall_grade = "C"
elif 60 <= percentage < 70:
    overall_grade = "D"
else:
    overall_grade = "F"
print(f"Overall Grade: {overall_grade}")


#3
shopping_list = {}

while True:
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check off item")
    print("4. View shopping list")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list[item] = False
        print(f"'{item}' added to the shopping list.")
    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            del shopping_list[item]
            print(f"'{item}' removed from the shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")
    elif choice == '3':
        item = input("Enter the item to check off: ")
        if item in shopping_list:
            shopping_list[item] = True
            print(f"'{item}' checked off.")
        else:
            print(f"'{item}' is not in the shopping list.")
    elif choice == '4':
        print("\nShopping List:")
        for item, checked in shopping_list.items():
            status = " (Done)" if checked else " (Pending)"
            print(f"- {item}{status}")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


#4

movie_ratings = {}
while True:
    print("\nMovie Rating Tracker")
    print("1. Add movie rating")
    print("2. View movie ratings")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        movie = input("Enter the movie title: ")
        rating = float(input("Enter your rating (1-5): "))
        if 1 <= rating <= 5:
            if movie in movie_ratings:
                movie_ratings[movie][0] += rating
                movie_ratings[movie][1] += 1
            else:
                movie_ratings[movie] = [rating, 1]
            print(f"Rating '{rating}' added for '{movie}'.")
        else:
            print("Invalid rating.")
    elif choice == '2':
        if movie_ratings:
            print("\nMovie Ratings:")
            for movie, (total_rating, num_ratings) in movie_ratings.items():
                average_rating = total_rating / num_ratings
                print(f"- {movie}: Average rating = {average_rating:.2f} ({num_ratings} ratings)")
        else:
            print("No movie ratings yet.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")


#5


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
conversion_factors = {
    "celsius_to_fahrenheit": celsius_to_fahrenheit,
    "fahrenheit_to_celsius": fahrenheit_to_celsius
}
while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = conversion_factors["celsius_to_fahrenheit"](celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = conversion_factors["fahrenheit_to_celsius"](fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



#6
    
phonebook = {}
while True:
    print("\nPhonebook Organizer")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number
        print(f"Contact '{name}' with number '{number}' added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"Name: {name}, Number: {phonebook[name]}")
        else:
            print(f"Contact '{name}' not found in the phonebook.")
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in phonebook:
            new_number = input("Enter new number: ")
            phonebook[name] = new_number
            print(f"Contact '{name}' updated with new number '{new_number}'.")
        else:
            print(f"Contact '{name}' not found in the phonebook.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


#7


menu = {}
menu_file = input("Enter the path to the menu file: ")
with open(menu_file, 'r') as file:
    for line in file:
        if line.strip():  
            item, category, price = line.strip().split(',')
            menu.setdefault(category, []).append((item, float(price)))
while True:
    print("\nOptions:")
    print("1. Browse by category")
    print("2. Search for item")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        for category, items in menu.items():
            print(f"\n{category}:")
            for item, price in items:
                print(f"{item} - ${price:.2f}")
    elif choice == '2':
        item_name = input("Enter item name to search: ")
        found = False
        for category, items in menu.items():
            for item, price in items:
                if item_name.lower() in item.lower():
                    print(f"{item} - ${price:.2f} ({category})")
                    found = True
        if not found:
            print(f"Item '{item_name}' not found in the menu.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    

#8
        
import random
import string
password_constraints = {
    'length': 12,
    'lowercase': True,
    'uppercase': True,
    'numbers': True,
    'symbols': True
}
def generate_password(constraints):
    characters = ''
    if constraints['lowercase']:
        characters += string.ascii_lowercase
    if constraints['uppercase']:
        characters += string.ascii_uppercase
    if constraints['numbers']:
        characters += string.digits
    if constraints['symbols']:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(constraints['length']))
    return password
print("Generated Password:", generate_password(password_constraints))

#9 ............................

#10
expenses = {}

while True:
    print("\nTravel Budget Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        print("Expense added successfully.")
    elif choice == '2':
        if expenses:
            total = 0
            print("\nTravel Expenses:")
            for category, amount in expenses.items():
                print(f"{category}: ${amount:.2f}")
                total += amount
            print(f"Total: ${total:.2f}")
        else:
            print("No expenses recorded yet.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

