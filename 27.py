import random

def find_cheapest_flight(destination="Bali", flexibility_days=3, budget=2000, preferred_airlines=None):
    airlines = ["Garuda Indonesia", "Singapore Airlines", "AirAsia", "Lion Air", "Cathay Pacific"]
    cheapest_flights = []

    for _ in range(10):
        departure_date = random.randint(1, 30)
        return_date = departure_date + random.randint(5, 15)
        airline = random.choice(airlines)
        price = random.randint(500, 1500)
        cheapest_flights.append({"departure_date": departure_date, "return_date": return_date,
                                 "airline": airline, "price": price})

    filtered_flights = [flight for flight in cheapest_flights
                        if flight["price"] <= budget
                        and (departure_date - flexibility_days <= flight["departure_date"] <= departure_date + flexibility_days)
                        and (return_date - flexibility_days <= flight["return_date"] <= return_date + flexibility_days)]

    sorted_flights = sorted(filtered_flights, key=lambda x: x["price"])

    if preferred_airlines:
        preferred_flights = [flight for flight in sorted_flights if flight["airline"] in preferred_airlines]
        other_flights = [flight for flight in sorted_flights if flight["airline"] not in preferred_airlines]
        sorted_flights = preferred_flights + other_flights

    return sorted_flights[:3]


if __name__ == "__main__":
    destination = input("Enter your destination: ")
    flexibility_days = int(input("Enter flexibility in days: "))
    budget = float(input("Enter your budget: "))
    preferred_airlines = input("Enter preferred airlines (comma-separated, leave blank for any): ").split(',')

    cheapest_options = find_cheapest_flight(destination, flexibility_days, budget, preferred_airlines)

    for i, option in enumerate(cheapest_options, start=1):
        print(f"Option {i}:")
        print(f"Airline: {option['airline']}")
        print(f"Price: ${option['price']}")
        print(f"Departure Date: Day {option['departure_date']}")
        print(f"Return Date: Day {option['return_date']}")
        print()
