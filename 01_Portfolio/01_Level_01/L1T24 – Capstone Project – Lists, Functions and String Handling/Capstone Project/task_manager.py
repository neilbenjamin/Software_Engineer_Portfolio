""" Task 24 - Capstone Project - Task Lists, Functions and String Handling
I received invaluable assistance from mentor, Chris, and have come to realize
how to structure functions and the flow of data better, but a little too
late as 80% of the layout was already done. I followed his example after our
our mentoring sessions and will continue to adapt to the new method. Managed
to find the bug that stopped the final figure update thanks to my mentor
Chris, who assisted me with with it."
"""
import copy
from datetime import datetime

# ====Login Section====

USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"
USERNAMES = []
PASSWORDS = []
LOGGED_IN_USER = []
USER_DICT = {}
CONTENT_USER_CHOICE = []
CONTENT_BALANCE = []
NEW_LIST = []

# Functions - Modular menu items

#  Print Bold function


def print_bold(text: str) -> None:
    """
    Emboldens given text and returns
    as string.
    :param text: Given text.
    """
    print(f"\033[1m{text}\033[0m")

# def clear_var(content_user_choice, content_balance):
#     content_user_choice = None

# User Over view functions & Stats

# Get file data based on parameter input.


def read_all_data(file_path: str):
    """
    Imports the file data as a string.
    :param file_path: Task file path.
    :return: Complete doc data
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def import_file_data(file_path: str):
    """
    Imports the file data as a list of
    lines.
    :param file_path: Task file path.
    :return: List of tasks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


# Compile user list to user dictionary


def compile_users(users: list[str]) -> dict[str: str]:
    """
    Compiles a dictionary of usernames and
    passwords from the user file data.

    :param users: List of user data.
    :return: Dictionary of usernames and passwords.
    """
    users_dict = {}
    for user in users:
        if len(user.split(", ")) == 2:
            username, password = user.strip().split(", ")
            users_dict[username] = password
    return users_dict


# Get user totals


def user_totals(dict: dict[int: list[str]]) -> str:
    """Counts the dict indexes to determine task total.
    Args:
        user_dict.
    Returns:
        user_totals
    """
    dict_len = len(dict)
    return dict_len


# Get user tasks and user dict and task dict and map their key and values
# to match their values and then extrapolate the various requirements from
# them.


def get_user_stats(
        users: dict[str: str],
        tasks: dict[int: str]
        ) -> dict[str: list[int]]:
    """
    Calculates user usage statistics.

    :param users: User dictionary.
    :param tasks: Task dictionary.
    :return: Prepared reporting string.
    """
    stats_data = {}
    for user in users.keys():
        # Count variables.
        assigned = 0
        pending = 0
        stats_data[user] = []
        completed = 0
        overdue = 0
        for task in tasks.values():
            if user == task[0]:
                datetime_format = "%d-%m-%Y"
                date_deadline = datetime.strptime(task[4], datetime_format)
                date_today = datetime.today()
                assigned += 1
                if task[-1] == "No":
                    pending += 1
                if task[-1] == "Yes":
                    completed += 1
                if date_today > date_deadline and task[-1] == "No":
                    overdue += 1
        percentage_ratio = (assigned / len(tasks)) * 100
        ratio_assigned = round(percentage_ratio)
        stats_data[user].extend([
            assigned,
            pending,
            ratio_assigned,
            completed,
            overdue
            ])
    return stats_data


# Display Stat Data


def display_stats(stats_data: dict[str: list[int]]) -> None:
    """
    Generate print display from stats data.
    :param stats_data: Stats data dictionary.
    """
    labels = [
        "Tasks Assigned",
        "Pending tasks",
        "Assigned percentage",
        "Total completed",
        "Overdue tasks"
    ]
    for entry in stats_data.items():
        print_bold(f"\n{entry[0]}")
        for index, stat in enumerate(entry[1]):
            print(f"{labels[index]}: {stat}")


# Task 0ver view functions

# Compile task list to a dictionary
def compile_tasks(tasks: list[str]) -> dict[int, str]:
    """
    Compiles a dictionary of indexes and list of tasks.

    :param tasks: List of all task data.
    :return: Dictionary of tasks paired with indexes.
    """
    tasks_dict = {}
    for index, task in enumerate(tasks, 1):
        if len(task.split(", ")) == 6:
            split_task = task.strip().split(", ")
            tasks_dict[index] = split_task
    return tasks_dict


# Get totals tasks


def task_totals(dict: dict[int: list[str]]) -> str:
    """Counts the dict indexes to determine task total.
    Args:
        user_dict.
    Returns:
        task_totals
    """
    dict_len = len(dict)
    return dict_len


# Get overdue tasks


def overdue_tasks(tasks_dict: dict[int: list[str]]) -> int:
    """Compare current & due dates and match to incomplete tasks.
    Args:
        tasks_dict.
    Returns:
        int: Number of overdue tasks
    """
    counter = 0
    datetime_format = "%d-%m-%Y"
    # counter = 0
    for task in tasks_dict.values():
        date_deadline = datetime.strptime(task[4], datetime_format)
        date_today = datetime.today()
        if date_today > date_deadline and task[-1] == "No":
            counter += 1
    return counter


# Get overdue and incomplete %


def overdue_task_percentage(tasks_dict: dict[int: list:[str]]) -> int:
    """Determine % of overdue tasks using for loop.
    Args:
        Task_Dict
    Returns:
        int: Percentage of overdue tasks
    """
    datetime_format = "%d-%m-%Y"
    number_overdue = 0
    total_task = 0
    for task in tasks_dict.values():
        date_deadline = datetime.strptime(task[4], datetime_format)
        date_today = datetime.today()
        if date_today > date_deadline and task[-1] == "No":
            number_overdue += 1
        if task[4]:
            total_task += 1
    overdue_percentage = float((number_overdue / total_task) * 100)
    # overdue_percentage = f"{total_task} : {number_overdue}"
    return overdue_percentage


# Get % of incomplete tasks

def incomplete_tasks_percentage(tasks_dict: dict[int: list:[str]]) -> int:
    """Determine % of incomplete tasks using for loop.
    Args:
        Task_Dict
    Returns:
        int: Percentage of incomplete tasks
    """
    number_incomplete = 0
    total_task = 0
    for item in tasks_dict.values():
        if item[-1] == "No":
            number_incomplete += 1
        if item[-1]:
            total_task += 1
    incomplete_percentage = float((number_incomplete / total_task) * 100)
    return incomplete_percentage


# Get completed tasks

def task_completed(tasks_dict: dict[int: list[str]]) -> int:
    """Loop values to determine task status.
    Args:
        User dict.s
    Returns:
        Yes or No
    """
    counter = 0
    for task in tasks_dict.values():
        if task[-1] == 'Yes':
            counter += 1
    return counter


# Get incomplete tasks

def tasks_incomplete(tasks_dict: dict[int:list[str]]) -> int:
    """Loop values to determine task status.
    Args:
        User dict.
    Returns:
        Yes or No
    """
    counter = 0
    for task in tasks_dict.values():
        if task[-1] == 'No':
            counter += 1
    return counter


# Display Reports controller


# Copy File


def copy_data():
    """Copy data from original txt files to new files.
    """
    tasks_data = read_all_data("tasks.txt")
    copy_tasks = copy.deepcopy(tasks_data)
    user_data = read_all_data("user.txt")
    copy_users = copy.deepcopy(user_data)
    with open("task_overview.txt", "w+", encoding='utf-8') as task_doc:
        task_doc.write(copy_tasks)
    with open("user_overview.txt", "w+", encoding='utf-8') as task_doc:
        task_doc.write(f"{copy_users}\n{copy_tasks}")


def generate_reports():
    """
    Main function to execute the various inner functions.
    """
    copy_data()
    print_bold("\nTASKS DISPLAY")
    tasks_data = import_file_data("task_overview.txt")
    print("")
    tasks_info = compile_tasks(tasks_data)
    print("")
    task_length = task_totals(tasks_info)
    print_bold("TRACKED DATA")
    print(f"The total number of tasks tracked: {task_length}.")
    completed_tasks = task_completed(tasks_info)
    print_bold("\nCOMPLETED TASKS")
    print(f"Total number of completed tasks: {completed_tasks}")
    incompleted_tasks = tasks_incomplete(tasks_info)
    print_bold("\nINCOMPLETED TASKS")
    print(f"Total number of completed tasks: {incompleted_tasks}")
    late_tasks = overdue_tasks(tasks_info)
    print_bold("\nLATE TASKS")
    print(f"Total number of overdue tasks: {late_tasks}")
    incomplete_percentage = incomplete_tasks_percentage(tasks_info)
    print_bold("\nINCOMPLETED TASKS PERCENTAGE")
    print(f"Total percentage of incomplete"
          f" tasks: {incomplete_percentage:.2f}%")
    overdue_percentage = overdue_task_percentage(tasks_info)
    print_bold("\nOVERDUE TASKS PERCENTAGE")
    print(f"Total percentage of overdue tasks: {overdue_percentage:.2f}%")
    return


# Display Stats controller


def display_statistics():
    copy_data()
    """Main function to call stats functions
    Returns:
        Function: Calls the functions
    """
    print_bold("\nSTATS DISPLAY\n")
    users_data = import_file_data("user_overview.txt")
    tasks_data = import_file_data("user_overview.txt")
    users_info = compile_users(users_data)
    tasks_info = compile_tasks(tasks_data)
    user_length = user_totals(users_info)
    print_bold("\nTRACKED DATA")
    print(f"The total number of users: {user_length}.")
    task_length = task_totals(tasks_info)
    print_bold("\nTRACKED DATA")
    print(f"The total number of tasks tracked: {task_length}.")
    print("")
    print_bold("Stats Info")
    stats_info = get_user_stats(users_info, tasks_info)
    print("")
    print_bold("Cleaned stats display")
    display_stats(stats_info)
    user_menu(logged_in)
    return


# Route logged in user to corresponding menu.


def user_menu(logged_in: str):
    """Verify logged in user and route to relevant menu by calling the
    correct menu function.
    Args:
        logged_in (str): logged in user value
    """
    if logged_in == "admin":
        CONTENT_USER_CHOICE.clear()
        CONTENT_BALANCE.clear()
        NEW_LIST.clear()
        admin_user(reg_user, add_task, view_all, view_mine, superuser,
                   exit_programme, generate_reports, display_statistics)
    else:
        CONTENT_USER_CHOICE.clear()
        CONTENT_BALANCE.clear()
        NEW_LIST.clear()
        normal_user(add_task, view_all, view_mine, superuser, exit_programme)


# Get, clean and separate tasks


def get_tasks() -> list:
    """retrieve and clean text and user data and update global variables
    for later use with the correct values.
    Args:
        None
    Returns:
        list: Cleaned and updated global variable values.
    """
    counter = 0
    logged_in
    with open(TASK_FILE, "r", encoding="utf-8") as task_doc:
        for line in task_doc:
            if logged_in in line:  # This is the line that filters the user.
                counter += 1
                user_choice = line.strip().split(", ")
                CONTENT_USER_CHOICE.append(user_choice)
            if logged_in not in line:
                user_choice = line.strip().split(", ")
                CONTENT_BALANCE.append(user_choice)


# Update task completion


def update_task(user_task_choice: int, logged_in: str) -> list:
    """Updates the task from No to Yes.
    Args:
        logged_in (str): Int and Str.
    Returns:
        list: Cleans containers before next call.
    """
    user_reduce = user_task_choice - 1
    task_status = ""
    if CONTENT_USER_CHOICE[user_reduce][5] == "Yes\n":
        choose_again = input("""
This task is already marked as completed.
Choose another task please. Click enter to return to the task menu""")
        while choose_again == "":
            view_mine(logged_in)
    user_update = input("\nPress \"Y\" to mark the task as complete. ").lower()
    while user_update != 'y':
        print("Please try again: ")
        user_update = input("\nPress \"Y\" to mark the "
                            "task as complete.").lower()
    else:
        task_status += 'Yes'
        CONTENT_USER_CHOICE[user_reduce][5] = task_status
        for sublist in CONTENT_BALANCE:
            NEW_LIST.append(", ".join(sublist))
        for sublist in CONTENT_USER_CHOICE:
            NEW_LIST.append(", ".join(sublist))
        print(f"This is the new_list: {NEW_LIST}")
        new_tasks = '\n'.join(NEW_LIST)
        with open(TASK_FILE, "w", encoding='utf-8') as task_doc:
            final = new_tasks.strip()
            task_doc.write(final)
        # Clear the containers
        CONTENT_USER_CHOICE.clear()
        CONTENT_BALANCE.clear()
        NEW_LIST.clear()
        return


# Update task


def update_user(user_task_choice: int) -> list:
    """Update user task is allocated to.
    Args:
        user_task_choice (int): Select the corresponding task.

    Returns:
        list: Updated list to be written to external doc.
    """
    user_reduce = user_task_choice - 1
    user_update = input("Update name:  ")
    CONTENT_USER_CHOICE[user_reduce][0] = user_update
    for sublist in CONTENT_USER_CHOICE:
        NEW_LIST.append(", ".join(sublist))
    for sublist in CONTENT_BALANCE:
        NEW_LIST.append(", ".join(sublist))
        new_tasks = '\n'.join(NEW_LIST)
    with open(TASK_FILE, "w", encoding='utf-8') as task_doc:
        task_doc.write(f"{new_tasks}")
    CONTENT_USER_CHOICE.clear()
    CONTENT_BALANCE.clear()
    NEW_LIST.clear()
    return


# Update Date Deadline


def update_deadline(user_task_choice: int) -> list:
    """Update user task deadline.
    Args:
        user_task_choice (int): Change the task from No to Yes.
    Returns:
        list: Updated list to Yes to be written to external doc.
    """
    res = True
    format = ("%d/%m/%Y")
    user_reduce = user_task_choice - 1
    update_task_deadline = str(input("Enter deadline dd/mm/yyyy : "))
    print(update_task_deadline)
    while True:
        try:
            res = bool(datetime.strptime(update_task_deadline, format))
            break
        except ValueError:
            res = False
        if res is False:
            print("Please enter your date exactly in the correct format")
        update_task_deadline = str(input("Enter deadline dd/mm/yyyy : "))
    due_date = datetime.strptime(update_task_deadline, "%d/%m/%Y")
    CONTENT_USER_CHOICE[user_reduce][4] = due_date.strftime("%d-%m-%Y")
    for sublist in CONTENT_USER_CHOICE:
        NEW_LIST.append(", ".join(sublist))
    for sublist in CONTENT_BALANCE:
        NEW_LIST.append(", ".join(sublist))
    new_tasks = '\n'.join(NEW_LIST)
    with open(TASK_FILE, "w", encoding='utf-8') as task_doc:
        task_doc.write(f"{new_tasks}")
    CONTENT_USER_CHOICE.clear()
    CONTENT_BALANCE.clear()
    NEW_LIST.clear()
    return


# Display users


def display_users(cleaned: list, count: int) -> str:
    """UX layout of the task elements.
    Args:
        cleaned (list): stripped and split data
        count (int): Add incremented int for list labelling.
    Returns:
        str: Writes the joined string to the external text file.
    """
    user_task_details = []
    user_task_details.append(
        f"\n{logged_in.upper()}\n"
        f"Task Number:\t\t{count}\n"
        f"Task Title:\t\t{cleaned[1:2]}\n"
        f"Assigned to:\t\t{cleaned[0:1]}\n"
        f"Date Assigned:\t\t{cleaned[3:4]}\n"
        f"Due Date:\t\t{cleaned[4:5]}\n"
        f"Task Description:\t{cleaned[2:3]}\n"
        f"Task Complete:\t\t{cleaned[5:6]}\n")
    final_user_task = "".join(user_task_details)
    print("".join(final_user_task.replace("[", "")
                  .replace("]", "")
                  .replace("'", "")))
    return user_task_details


# Register new user for admin users only


def reg_user():
    """Generate mew data from user prompts, update the database and checking
    for exiting user data.
    """
    register_new_user = []
    register_new_password = []
    register_new_user = input("Please enter a new user : ").lower()
    while register_new_user in USERNAMES:  # Evaluates until False
        print("This username is already in use.")
        register_new_user = input("Please enter a new user : ").lower()
    register_new_password = input("Please choose a password : ")
    validate_password = input("Please confirm your password : ")
    while validate_password not in register_new_password:
        print("Incorrect. Please type your password carefully.")
        validate_password = input("Please confirm your "
                                  "password : ")
    while validate_password == "":
        print("You've entered a blank space.")
        validate_password = input("Please confirm your "
                                  "password : ")
    with open(USER_FILE, "a",
              encoding='utf-8')as user_doc:
        user_doc.write(f"\n{register_new_user}, "
                       f"{register_new_password}")
    return


# Assign new task - Got assistance with the date time mechanism and validation
# from geeksforgeeks


def add_task():
    """Generate a new task using user prompts and
    """
    res = True
    format = ("%d/%m/%Y")
    current_date = datetime.today()
    new_task_status = ["No\n"]
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
    return


# View all tasks -  Read and display all task info.


def view_all():
    """View all the data in the task document.
    """
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
        return


# View own tasks - View specific logged in user task


def view_mine(logged_in: str) -> int:
    """
  View logged in users task data.
    """
    counter = 0
    logged_in
    # user_task_details = []
    with open(TASK_FILE, "r+", encoding='utf-8') as task_doc:
        for line in task_doc:
            if logged_in in line:  # This is the line that filters the user.
                counter += 1
                user_choice = line.strip().split(", ")
                display_users(user_choice, counter)
        get_tasks()
        while True:
            try:
                user_task_choice = int(input("""
Select a task number for more options, or ;
Select -1 to exit to the main menu: """))
            except ValueError:
                print("""
Wrong entry, please try again and enter your task number choice or -1 to exit
to the main menu:
""")
                # view_mine(logged_in)
            else:
                if user_task_choice > 0:
                    edit_or_complete(user_task_choice)
                elif user_task_choice == -1:
                    user_menu(logged_in)


def edit_or_complete(user_task_choice):
    """Router function to assist with options for the user.
    Args:
        cleaned (list): stripped and split data
    Returns:
        Chosen function outcome.
    """
    menu = input("""

A = Select A to update task, or:

B = Select B to update user and task deadline.

C = Return to main menu

""").lower()
    if menu == "a":
        update_task(user_task_choice, logged_in)
    elif menu == "b":
        update_user_deadline(user_task_choice)
    elif menu == "c":
        return

# Update the task deadline.


def update_user_deadline(user_task_choice: int) -> int:
    """Update the task deadline.
    Args:
        cleaned (list): stripped and split data
    Returns:
        str: Writes the updated date to the external text file.
    """
    user_reduce = user_task_choice - 1
    if CONTENT_USER_CHOICE[user_reduce][5] == "Yes\n":
        return_to_tasks = input("""

You can only edit an incomplete task.
Please press "R" to select a new task

""").lower()
        while True:
            if return_to_tasks == "r":
                view_mine(logged_in)
                break
            else:
                break
    menu = input("""

A = Update Username assigned to task, or;
B = Update task deadline

""").lower()
    if menu == "a":
        update_user(user_task_choice)
    elif menu == "b":
        update_deadline(user_task_choice)


# Super User Option - Read and display all user and task totals


def superuser():
    """Displays total tasks and users to the admin user.
    """
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
        return


def exit_programme():
    """Exits programme
    """
    print('Goodbye!!!')
    exit()

# Control flow to check which user. Outer loop is normal user and inner loop
# is admin user.


while True:

    def admin_user(reg_user, add_task, view_all, view_mine, superuser,
                   exit_programme, generate_reports, display_statistics):
        """Admin menu controller

        Args:
            reg_user (_type_): Invoke register new user
            add_task (_type_): Invoke add task
            view_all (_type_): _Invoke View All
            view_mine (_type_): Invoke View Mine
            superuser (_type_): Invoke superuser
            exit_programme (_type_): Invoke Exit
        """
        menu = input('''
    Superuser Menu - Select one of the following options:

    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - view-all
    gr - generate reports
    ds = display statistics
    e - exit

    : ''').lower()
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == "va":
            view_all()
        elif menu == 'vm':
            view_mine(logged_in)
        elif menu == 's':
            superuser()
        elif menu == "gr":
            generate_reports()
        elif menu == "ds":
            display_statistics()
        elif menu == 'e':
            exit_programme()
        else:
            print("\nYou have entered an invalid input. Please try again")
    break

while True:

    def normal_user(add_task, view_all, view_mine, superuser, exit_programme):
        """_summary_

        Args:
            add_task (_type_): Invoke Add Task
            view_all (_type_): Invoke View All
            view_mine (_type_): Invoke View Mine
            superuser (_type_): Invoke Superuser
            exit_programme (_type_): Invoke exit
        """
        menu = input('''
    Select one of the following options:

    a - add a  task
    va - view all tasks
    vm - view my tasks
    e - exit

    : ''').lower()
        if menu == 'a':
            add_task()
        elif menu == "va":
            view_all()
        elif menu == 'vm':
            view_mine(logged_in)
        elif menu == 's':
            superuser()
        elif menu == 'e':
            exit_programme()
        else:
            print("\nYou have entered an invalid input. Please try again")
    break

# Start Sequence


copy_data()


with open(USER_FILE, "r", encoding='utf-8') as user_doc:
    for line in user_doc:
        user_list = line.strip().split(", ")
        USERNAMES.append(user_list[0])
        PASSWORDS.append(user_list[1])
        USER_DICT[user_list[0]] = user_list[1]
    while True:
        input_username = input("Enter a username: ")
        input_password = input("Enter a password: ")
        if input_username in USER_DICT:
            if input_password == USER_DICT[input_username]:
                LOGGED_IN_USER.append(input_username)
                logged_in = "".join(LOGGED_IN_USER)
                # USER_NAME += logged_in
                print_bold(f"\nWelcome. {logged_in}")
                user_menu(logged_in)
        else:
            print("Incorrect username or password. Please try again")
