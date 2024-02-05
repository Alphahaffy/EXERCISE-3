#1
def calculator(expression):
    try:
        result = eval(expression)
        return result, expression
    except Exception as e:
        return "Error: " + str(e), expression
def main():
    calculations = []
    while True:
        expression = input("Enter an expression (or 'y' to exit): ")      
        if expression == 'y':
            break      
        result, expression_used = calculator(expression)
        calculations.append((expression_used, result))      
        print("Result:", result)
main()


#2
"""Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps,
distance walked, and calories burned. Write expressions to calculate average steps per week
and total distance covered in a month.
"""

daily_steps = []
for day in range(1, 8):
    steps = int(input("DAILY STEPS{}: ".format(day)))
    daily_steps.append(steps)
while True:
 dis_per_step = 0.7 
 cal_per_step = 0.05  
 weekly_ave_steps = sum(daily_steps) / len(daily_steps)
 total_dis_month = weekly_ave_steps * dis_per_step * 4 * 7
 total_cal_month = weekly_ave_steps * cal_per_step * 4 * 7
 print("WEEKLY AVERAGE STEPS:", weekly_ave_steps)
 print("TOTAL DIS COVERED IN A MONTH (m):", total_dis_month)
 print("TOTAL CAL BURNED IN MONTH:", total_cal_month)
 

#3
 """Shopping List: Write a program to manage a shopping list. Use variables to store item names,
quantities, and prices. Calculate the total cost of items and check if you have enough budget.
 """

num_items = int(input("TOTAL NUMBER OF ITEMS: "))
budget = float(input("YOUR BUDGET: $"))
total_cost = 0
enough_budget = True
for i in range(num_items):
    NAME = input(f"NAME OF ITEM {i + 1}: ")
    QUANTITY = int(input(f" QUANTITY OF {NAME}: "))
    PRICE = float(input(f"PRICE OF {NAME}: $"))  
    total_cost += QUANTITY * PRICE
    if total_cost > budget:
        enough_budget = False
    print(f"{NAME}: {QUANTITY} x ${PRICE:.2f} = ${QUANTITY * PRICE:.2f}")
print("TOTAL COST:", total_cost)
if enough_budget:
    print("ENOUGH BUDGET.")
else:
    print(" DO NOT HAVE ENOUGH BUDGET.")

#4
"""Recipe Calculator: Design a recipe calculator that adjusts ingredient quantities based on the
number of servings. Use variables to store recipe ingredients and amounts, and write
expressions to calculate adjusted quantities.
"""
total_ingredients = 0
num_ingredients = int(input("NUMBER OF INGREDIENTS:"))
i = 0
while i < num_ingredients:
    ingredient_name = input(f"NAME OF INGREDIENTS {i + 1}: ")
    ingredient_amount = float(input(f"AMOUNT OF {ingredient_name} (in cups, teaspoons, etc.): "))
    total_ingredients += ingredient_amount
    i += 1
num_servings = int(input("NUMBER OF SERVINGS: "))
adjusted_servings = total_ingredients * num_servings
print(f"\nADJUSTED RECIPE FOR {num_servings} SERVINGS:")
print(f"TOTAL INGREDIENTS: {adjusted_servings}")


#5
"""Movie Recommendation System: Create a program that recommends movies based on user
preferences. Use variables to store genre, rating, and release year. Write expressions to
compare movies and suggest matches.
"""

genre = input(" Urdu, Drama, Romance, Action, etc.: ")
rating = float(input("RATING (out of 10): "))
release_year = int(input("RELEASE YEAR: "))
movies = [
    {"title": "Waada", "genre": "urdu", "rating": 7.5, "release_year": 2016},
    {"title": "Load Wedding", "genre": "urdu", "rating": 8.2, "release_year": 2018},
    {"title": "Punjab Nahi Jaungi", "genre": "urdu", "rating": 8.6, "release_year": 2017},
    {"title": "Jawani Phir Nahi Ani", "genre": "urdu", "rating": 8.4, "release_year": 2015},
    {"title": "Bol", "genre": "urdu", "rating": 8.3, "release_year": 2011},
    {"title": "The Shawshank Redemption", "genre": "drama", "rating": 9.3, "release_year": 1994},
    {"title": "The Godfather", "genre": "crime", "rating": 9.2, "release_year": 1972},
    {"title": "Inception", "genre": "action", "rating": 8.8, "release_year": 2010},
    {"title": "Interstellar", "genre": "sci-fi", "rating": 8.6, "release_year": 2014},
    {"title": "Forrest Gump", "genre": "drama", "rating": 8.8, "release_year": 1994},
    {"title": "Titanic", "genre": "romance", "rating": 7.8, "release_year": 1997},
    {"title": "The Dark Knight", "genre": "action", "rating": 9.0, "release_year": 2008},
    {"title": "Pulp Fiction", "genre": "crime", "rating": 8.9, "release_year": 1994},
    {"title": "Avatar", "genre": "action", "rating": 7.8, "release_year": 2009},
    {"title": "The Matrix", "genre": "sci-fi", "rating": 8.7, "release_year": 1999}
]

recommendations = []
for movie in movies:
    if (movie["genre"] == genre or genre == "any") \
        and movie["rating"] >= rating \
        and movie["release_year"] >= release_year:
            recommendations.append(movie["title"])

if recommendations:
    print("Recommend the following movies:")
    for recommendation in recommendations:
        print(recommendation)
else:
    print("No movies match your preferences.")



#6
"""Time Management Tool: Develop a tool to track time spent on various activities. Use variables to
store task names and durations. Write expressions to calculate total time spent on each task and
identify areas for improvement.
"""

def record_time(task_name, duration):
    global tasks, total_time
    if task_name not in tasks:
        tasks[task_name] = duration
    else:
        tasks[task_name] += duration
    total_time += duration
    print(f"Successfully recorded {task_name} for {duration} minutes.")

def get_task_report(task_name):
    if task_name in tasks:
        return tasks[task_name]
    else:
        return f"Task '{task_name}' hasn't been tracked yet."

def get_total_report():
    for task_name, duration in tasks.items():
        print(f"Task: {task_name}, Duration: {duration} minutes")
    print(f"Total time spent: {total_time} minutes")

def identify_improvement_areas():
    print("\nTime Usage Analysis:")
    for task_name, duration in tasks.items():
        percentage = duration / total_time * 100
        print(f"- {task_name}: {percentage:.2f}% ({duration} minutes)")

    print("\nPotential Improvement Areas:")
    print("- Consider delegating or automating routine tasks that consume significant time.")
    print("- Evaluate if tasks align with your priorities and adjust accordingly.")
    print("- Analyze time spent on unproductive activities and seek ways to minimize them.")

tasks = {}
total_time = 0

while True:
    print("\nTime Management Tool")
    print("1. Record Time")
    print("2. Get Task Report")
    print("3. Get Total Report")
    print("4. Identify Improvement Areas")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        duration = int(input("Enter duration in minutes: "))
        record_time(task_name, duration)
    elif choice == "2":
        task_name = input("Enter task name for report: ")
        report = get_task_report(task_name)
        print(report)
    elif choice == "3":
        get_total_report()
    elif choice == "4":
        identify_improvement_areas()
    elif choice == "5":
        print("Exiting. Thank you for using the Time Management Tool!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


#THIS PROGRAM WILL HELP YOU TO COUNT THE TOTAL PAGES YOU HAVE READ
        
pages_read = 0
num_days = int(input("DAYS: "))
for day in range(1, num_days + 1):
    pages_read = int(input(f"NUMBER OF PAGAES READ ON {day}: "))
    pages_read += pages_read
print(f"YOU HAVE READ{pages_read} PAGES IN {num_days} DAYS.")



#THIS PRROGRAM WILL HELP YOU TO TRACK WEEKLY BUDGET
expenses = 0
for day in range(1, 8):
    daily_expenses = float(input(f"DAY{day} (in $): "))
    expenses += daily_expenses
av_daily_expenses = expenses / 7
print(f"TOTAL IN WEEK: ${expenses:.2f}")
print(f"AVERAGE DAILY: ${av_daily_expenses:.2f}")


#THIS PROGRAM WILL HELP YOU TO  TRACK YOUR MONTHLY SAVING

goal = float(input(" GOAL TO MONTHLY SAVINGS: $"))
savings = float(input("TOTAL SAVING: $"))
achieved = (savings / goal) * 100
print(f"ACHEIEVD : {achieved:.2f}% o OF YOUR MONTHLY GOAL")
if achieved >= 100:
    print("GOAL COMPLETED!")
else:
    remaining_goal = goal - savings
    print(f"YOU NEED TO SAVE ${remaining_goal:.2f} TO REACH THE GOAL.")
    weekly_goal = remaining_goal / 4
    daily_goal = remaining_goal / 30
    print(f"TO REACH YOUR GOAL FASTER:")
    print(f"- SAVE ${weekly_goal:.2f} /WEEK")
    print(f"- Save ${daily_goal:.2f} / DAY")
    adjust_goal = input("WOULD YOU LIKE TO ADJUST YOUR SAVING GOAL? (y/n): ")
    if adjust_goal == "y":
        new_goal = float(input("NEW GOAL: $"))
        remaining_new_goal = new_goal - savings
        print(f"YOUR NEW GOAL IS${new_goal:.2f}. YOU STILL NEED TO SAVE ${remaining_new_goal:.2f} TO REACH IT.")
    else:
        print("KEEP IT UP!")

