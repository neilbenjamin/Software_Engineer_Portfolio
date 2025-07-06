"""Task 27 - OOP - Classes - Compulsory Task 2."""
class Adult:
    """Parent class to define the object attribute and class properties.
    """
# Class variable
    legal_driver = True
    
# Constructor method with instance variables
    def __init__(self, name, age, hair_colour, eye_colour):
        """Adult class Constructor method.
        Args:
            name (_string_): user name
            age (_int_): user age
            hair_colour (_string_): user hair colour
            eye_colour (_string_): user eye colour
        """
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        
# Parent method 
    def can_drive(self):
        """Method to output class variable
        """
        print(self.name, "Is allowed to drive: ", self.legal_driver)

# Child Class inheriting Parent data
class Child(Adult):

# No new instances required as we are using the Adult class constructor.

# Method to determine boolean of user input.
    def can_drive(self):
        """Check if user input is > 18 and output corresponding boolean.
        """
        if self.age < 18:
            self.legal_driver = False
            print(self.name, "is too young to drive.")
        else:
            print(self.name, "is old enough to drive.")
        # Exit class
            

def main():
    """Start programme, enter user data, initialise object and call object
    method.
    """
    user_name = input("Enter your name: ")
    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please select an integer and try again. ")
    user_hair = input("What colour hair do you have? ")
    user_eyes = input("What colour eyes do you have? ")
    # Initialise object
    child = Child(user_name, user_age, user_hair, user_eyes)
    # Call object
    child.can_drive()

main()