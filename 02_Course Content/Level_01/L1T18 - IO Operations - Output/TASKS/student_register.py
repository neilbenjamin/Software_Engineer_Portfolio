""" Task 18 - IO Operations - Output - TASK """

#  Use the with/as method to ensure each call is closed.
#  Save external doc as variable "exam"
#  Create lines variable and empty list for saving inputs
with open("L1T18 - IO Operations - Output/TASKS/reg_form.txt", "w") as exam:
    dots = "..............."
    id_numbers = []
    #  For loop to loop the number entered by the user.
    name = int(input("""
Enter the number of students you are registering for the exam?
The maximum number the venue can accommodate is 30 students: """))
    #  Loop the entered integer value
    for student in range(name):
        # Accept a string value as the id number. Append to list and
        # concatenate with dots string.
        student_id = (input("Please enter the student ID Number: "))
        stars = " ..........................."
        id_numbers.append(student_id + stars)
    #  Join back to a string with a newline separator
    sign_line = "\n".join(id_numbers)
    #  Write final output to new external doc
    exam.write("PLEASE SIGN NEXT TO YOUR ID NUMBER\n")
    exam.write("\n")
    exam.write(sign_line)
