""" Task 27 - OOP - Classes. Enjoyable task but got stuck for a long time 
not correctly pointing to the correct user i who resulted in only the 1st 
email updating to 'read'. 12 hours later...
"""
class Email:
    """Class to filter email headers and and update the read/unread status.
    1 class variable and 3 instance variables and 3 methods.

    Returns:
        str: Returns the corresponding values based on the users input
    """
    # Class Variable
    """Default boolean for unread/read mails
    """
    has_been_read = False

    def __init__(self, address, subject, content):
        """Instantiate or assign the values passed in by the user to each
        instance variable. Constructor method

        Args:
            address (_string_): _email address_
            subject (_string_): _Subject heading_
            content (_string_): _Body content_
        """
        self.email_address = address
        self.subject_line = subject
        self.email_content = content
        return

    def mark_as_read(self):
        """_switch the boolean from False to True.
        """
        self.has_been_read = True

    def __str__(self):
        """_Returns all the associated elements to string
        Returns:
            _str_: _Readable string formats_
        """
        return (
            f"FROM:\t\t {self.email_address} \n"
            f"SUBJECT:\t {self.subject_line} \n"
            f"CONTENT:\t {self.email_content}"
            )

# Global scope


inbox = []  # Store all emails


# Create objects
def populate_inbox():
    """Starter function that creates the email objects with the Email
    class and appends each object as an element to the inbox list.
    """
    email1 = Email("neil@digitalblend.co.za", "Projects delivery",
                   "Content\n")
    email2 = Email("neil@capedjco.co.za", "Petal events",
                   "Content\n")
    email3 = Email("neilbenjaminmusic@gmail.com", "inn8 agreements",
                   "Content")
    inbox.extend([email1, email2, email3])
    return

# read_emails


def read_email(i: int):
    """Selects email index and email object value based on user input then
    invokes mark_as_read() changing the boolean from False to True.

    Args:
        i (_int_): _suser menu choice
    """
    print("\nREAD EMAIL\n")
    for email in inbox:
        print(inbox[i])
        inbox[i].mark_as_read()
        print(f"HAS BEEN READ:\t {inbox[i].has_been_read}")
        break
    return


# unread_emails()


def unread_emails():
    """_List the unread emails per subject line with number/value display
    """
    print("UNREAD EMAILS\n")
    for count, email in enumerate(inbox, 1):
        if email.has_been_read is False:
            print(count, email.subject_line, ": Unread")
        # elif email.has_been_read is True:
        #     print(email.subject_line, ": has been read.")


# list_emails()


def list_emails():
    """_List the emails per subject line with number/value display
    """
    print("\nYOUR INBOX\n")
    while True:
        for count, value in enumerate(inbox, 1):
            print(f"{count} : {value.subject_line}")
        try:
            menu = int(input("\nSelect the email number to read it:\n\n"))
            if menu is menu:
                read_email(menu - 1)
                break
        except Exception:
            print("Please enter the correct number to read the mail\n")
    return


populate_inbox()


while True:
    menu = input("""
1. Read an email
2. View unread emails
3. Quit the application\n
""").lower()
    if menu == "1":
        list_emails()
    elif menu == "2":
        unread_emails()
    elif menu == "3":
        exit()
    else:
        print("\nPlease check your input and try again.")
