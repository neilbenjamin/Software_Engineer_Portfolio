"""Task 27 - OOP - Classes - Compulsory Task 1."""


class Course:  # Parent class
    """Course class to encapsulate all the details for a software course.
    """
    # Class 'global' variables related to all instances
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"

    def print_head_office(self):
        print("\nHead office location: ", self.head_office)

    def contact_details(self):
        """Method to call website details from the class variables.
        Args:
            self (str): returns website
        """
        print("\nPlease contact us by visiting", self.contact_website)


class OOPCourse(Course):  # Child Class
    # Class Variable
    course_id = 12345

    def __init__(self):
        """Constructor method to create or instantiate the values of the
        objects that are submitted
        """
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        """Method to print the two instance variables in the constructor.
        """
        print("\nCourse content: ", self.description)
        print("\nCourse Trainer: ", self.trainer)

    def show_course_id(self):
        """Method to print the class variable course id. """
        print("\nThe course ID is: ", self.course_id, "\n")


course_1 = OOPCourse()  # Creating the object as an instance of the class.
course_1.contact_details()  # Calling the object and it's methods
course_1.trainer_details()
course_1.show_course_id()
