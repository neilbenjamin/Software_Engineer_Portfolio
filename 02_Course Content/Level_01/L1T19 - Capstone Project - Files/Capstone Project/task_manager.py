""" Task 19 - Capstone Project - Task 1 & 2 - File Management"""
from datetime import datetime
# I managed to refactor the code to a modular function as recommended by the
# task resubmission request and it makes way more sense 100%.
# I'm sorry if this has caused unnecessary
# work for you if you have already started reviewing the previous resubmission.

# I got assistance with the dictionary function from a mentor and another
# mentor assisted me with guidance as well as very useful refactoring
# methods, which is actually insane.
# The rest of the work is all my own. No generative AI was used at all. I also
# used w3schools and GeeksforGeeks and FreeCodeCamp for assistance on some of
# the string, list and looping concepts.

# ====Login Section====
USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"
# Login Code

# Read, validate and assign users to variables
with open(USER_FILE, "r", encoding='utf-8') as user_doc:
    usernames = []
    passwords = []
    logged_in_user = []
    user_dict = {}

    # User Containers
    # User Login
    for line in user_doc:
        user_list = line.strip().split(", ")
        usernames.append(user_list[0])
        passwords.append(user_list[1])
        user_dict[user_list[0]] = user_list[1]
    while True:
        input_username = input("Enter a username: ")
        input_password = input("Enter a password: ")
        if input_username in user_dict:
            if input_password == user_dict[input_username]:
                logged_in_user.append(input_username)
                logged_in = " ".join(logged_in_user)
                print(f"\nWelcome. {logged_in}")
                break
        else:
            print("Incorrect username or password. Please try again")
# Functions - Modular menu items

# New User - 'r' - Only available to admin user menu


def register_user():
    register_new_user = []
    register_new_password = []
    register_new_user = input("Please enter a new user : ").lower()
    register_new_password = input("Please choose a password : ")
    validate_password = input("Please confirm your password : ")
    while validate_password not in register_new_password:
        print("Incorrect. Please type your password carefully.")
        validate_password = input("Please confirm your "
                                  "password : ")
    else:
        with open(USER_FILE, "a",
             encoding='utf-8')as user_doc:
            user_doc.write(f"\n{register_new_user}, "
                           f"{register_new_password}")


# Assign new task - Got assistance with the date time mechanism and validation
# from geeksforgeeks


def assign_task():
    res = True
    format = ("%d/%m/%Y")
    current_date = datetime.today()
    new_task_status = ["No"]
    new_task_user = input("Enter "
                          "the user responsible for the task : ")
    new_task_title = input("Please enter the task title : ")
    new_task_description = input("Please enter the task "
                                 "description : ")
    new_date_assigned = current_date.strftime("%d-%m-%Y")
    new_task_deadline = str(input("Enter deadline dd/mm/yyyy : "))
    while True:
        try:
            res = bool(datetime.strptime(new_task_deadline, format))
            break
        except ValueError:
            res = False
        if res is False:
            print("Please enter your date exactly in the correct format")
        new_task_deadline = str(input("Enter deadline dd/mm/yyyy : "))

    due_date = datetime.strptime(new_task_deadline, "%d/%m/%Y")
    new_task_status = "No"
    # Open Task File
    with open(TASK_FILE, "a", encoding='utf-8') as task_doc:
        task_doc.write(f"\n{new_task_user}, {new_task_title}, "
                       f"{new_task_description}, "
                       f"{new_date_assigned}, "
                       f"{due_date.strftime("%d-%m-%Y")}, "
                       f"{new_task_status}")


# View all tasks -  Read and display all task info.


def view_all_tasks():
    task_counter = 0
    task_details = []
    with open(TASK_FILE, "r+",
              encoding='utf-8') as task_doc:
        for line in task_doc:
            task_counter += 1
            new_char = line.strip().split(", ")
            task_details.append(f"\nTASK {task_counter}\n\n"
                                f"Task:\t\t\t{new_char[1:2]}\n"
                                f"Assigned to:\t\t"
                                f"{new_char[0:1]}\n"
                                f"Date Assigned:\t\t"
                                f"{new_char[3:4]}\n"
                                f"Due Date:\t\t{new_char[4:5]}\n"
                                f"Task Description: \t"
                                f"{new_char[2:3]}\n"
                                f"Task Complete:\t\t"
                                f"{new_char[5:6]}\n")
        final_task = "".join(task_details)
        print("".join(final_task.replace("[", "").replace("]", "").
                      replace("'", "")))


# View own tasks - View specific logged in user task


def view_own_tasks():
    counter = 0
    logged_in
    user_task_details = []
    with open(TASK_FILE, "r+", encoding='utf-8') as task_doc:
        for line in task_doc:
            if logged_in in line:  # This is the line that filter the user.
                counter += 1
                new_char = line.strip().split(", ")
                user_task_details.append(f"\n"
                                         f"{logged_in.upper()} "
                                         f"TASK"
                                         f" {counter}\n\n"
                                         f"Task:\t\t\t"
                                         f"{new_char[1:2]}\n"
                                         f"Assigned to:\t\t"
                                         f"{new_char[0:1]}\n"
                                         f"Date Assigned:\t\t"
                                         f"{new_char[3:4]}\n"
                                         f"Due Date:\t\t"
                                         f"{new_char[4:5]}\n"
                                         f"Task Description:"
                                         f"\t{new_char[2:3]}\n"
                                         f"Task Complete:\t\t"
                                         f"{new_char[5:6]}\n")
            final_user_task = "".join(user_task_details)
        print("".join(final_user_task
                      .replace("[", "").replace("]", "").
                      replace("'", "")))


# Super User Option - Read and display all user and task totals


def superuser():
    task_details = []
    with open(TASK_FILE, "r+", encoding='utf-8') as task_doc:
        for line in task_doc:
            new_char = line.strip().split(", ")
            task_details.append(new_char)
        print(f"\nTOTAL TASKS: {len(task_details)}\n")
        # Display All Users
        user_detail_database = []
        with open(USER_FILE, "r", encoding='utf-8') as user_doc:
            for user in user_doc:
                clean_user = user.strip().split(", ")
                user_detail_database.append(clean_user)
        print(f"\nTOTAL USERS : {len(user_detail_database)}")


def exit_programme():
    print('Goodbye!!!')
    exit()

# Control flow to check which user. Outer loop is normal user and inner loop
# is admin user.


while True:  # Normal User Menu
    if logged_in == "admin":
        while True:  # Admin Menu
            # print("Inner Loop")
            logged_in
            menu = input('''
Superuser Menu - Select one of the following options:\n
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view-all
e - exit
: ''').lower()
            if menu == 'r':
                register_user()  # calling functions
            elif menu == 'a':
                assign_task()  # calling functions
            elif menu == "va":
                view_all_tasks()  # calling functions
            elif menu == 'vm':
                view_own_tasks()  # calling functions
            elif menu == 's':
                superuser()  # calling functions
            elif menu == 'e':
                exit_programme()  # calling functions
            else:
                print("You have entered an invalid input. Please try again")
    menu = input('''
Select one of the following options:

a - add a  task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    if menu == 'a':
        assign_task()
    elif menu == "va":
        view_all_tasks()
    elif menu == 'vm':
        view_own_tasks()
    elif menu == 's':
        superuser()
    elif menu == 'e':
        exit_programme()
    else:
        print("You have entered an invalid input. Please try again")
