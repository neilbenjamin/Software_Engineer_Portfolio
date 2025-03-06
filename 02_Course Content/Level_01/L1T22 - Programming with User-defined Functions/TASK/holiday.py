""" Task 22 - Programming with User-defined Functions - Task"""

# Travel options

destinations = {
    "rome": 9500,
    "new york": 18000,
    "london": 16000
 }

# Input Totals

holiday_costs = []

# Functions


def hotel_cost(num_nights):
    # Calculates the user's input cost and returns the total & appends
    # total for additional usage
    hotel_total = num_nights * 3500
    print(f"Your hotel cost for {num_nights} nights "
          f"is : R {hotel_total:.2f}\n")
    holiday_costs.append(hotel_total)
    return hotel_total


def plane_cost(city_flight):
    # Retrieves the key from the dictionary to map to the user input's
    # associated cost, instead of the if/else suggestion & appends
    # total for additional usage

    while city_flight in destinations:
        flight_cost = destinations[city_flight]
        print(f"The ticket price to {city_flight} is : R {flight_cost:.2f}\n")
        holiday_costs.append(flight_cost)
        return flight_cost
    else:
        print(f"We don't have {city_flight} on the flight manifesto. "
              "Please choose Rome, New York or London. Try again:  ")


def car_rental(rental_days):
    # Takes teh user's input and calculates the rental total & appends
    # total for additional usage
    rental_total = rental_days * 950
    print(f"Your car rental cost for {rentals_days}days "
          f"is : R {rental_total:.2f}\n")
    holiday_costs.append(rental_total)
    return rental_total


def holiday_cost(holiday_costs):
    # Using the sum() function to total the costs.
    total_holiday_cost = sum(holiday_costs)
    print(f"The total holiday cost is: R {total_holiday_cost:.2f}")
    return total_holiday_cost


def options(x="y", y="n"):
    # exit or try again.
    if user_option == y:
        exit()


# Control Flow & User Inputs

while True:
    num_nights = int(input("How many nights are you staying at "
                           "the hotel?  "))
    hotel_cost(num_nights)

    city_flight = str(input("Which city are you flying to? Rome, New York "
                      "or London?  ")).lower()
    plane_cost(city_flight)

    rentals_days = int(input("How many days will you require car-hire?  "))
    car_rental(rentals_days)

    holiday_cost(holiday_costs)

    user_option = str(input("""
Would you like to choose new options?
Select: Y to try again
Select: N to exit
""")).lower()
    options(user_option)
