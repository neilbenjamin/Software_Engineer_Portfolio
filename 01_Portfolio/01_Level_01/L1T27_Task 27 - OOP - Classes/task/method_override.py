class Adult:

    legal_driver = True
    
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        
    
    def can_drive(self):
        print(self.name, "Is allowed to drive: ", self.legal_driver)

class Child(Adult):

    def can_drive(self):
        if self.age < 18:
            self.legal_driver = False
            print(self.name, "is too young to drive.")
        else:
            print(self.name, "is old enough to drive.")
            

def main():
    user_name = input("Enter your name: ")
    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please select an integer and try again. ")
    user_hair = input("What colour hair do you have? ")
    user_eyes = input("What colour eyes do you have? ")
    child = Child(user_name, user_age, user_hair, user_eyes)
    child.can_drive()

main()