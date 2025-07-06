# pseudo solution

# Request a yes or no answer from the user. Assign the response values
# to the booleans and print the booleans.

# temp input value
temp_input = input("Is it hotter than 20 degrees? ")
temp_lower = temp_input.lower() 

if (temp_lower != "yes" or temp_lower != ("no")):
    print("Please enter only yes or no")
else:

# weekend input value
    weekend_input = input("Is it weekend yet? ")
weekend_lower = weekend_input.lower()

#Sunny or not
weather_input = input("Is it sunny? ")
weather_lower = weather_input.lower()

# Booleans
temperature = ""
weekend = ""
weather = ""

# conditionals 

# Temperature
if (temp_lower == "no"):
    temperature = "Wear a long-sleeved shirt"
else:
    temperature = ("Wear a short-sleeved shirt")

# Weekend?
if (weekend_lower == "no"):
    weekend = "jeans"
else:
    weekend = "shorts"

# Weather
if (weather_lower == "no"):
    weather = "Please also wear a raincoat."
else:
    weather = "Please also wear a cap."
    
print (f"You should wear {temperature} with {weekend}. {weather} ")


 