
""" Task 29 - Capstone - OOP """
# ========The beginning of the class==========


class Shoe:

    # Class Variable applicable to all instance variables
    header = ["Country", "Code", "Product", "Cost", "Quantity"]
    """This created quiet a bit of complication with me writing the
    header to the shoe_list and resulting in errors when trying to
    computer and write to txt file. I forgot the header was appended
    separately. Then I wrote the header to a separate list container
    which worked and that reminded me again of the purpose of the class.
    Needed to go back on the notes to get this solution working. I also
    learnt courtesy of google to use a new class method to act upon the
    class variable we defined above and use a cls argument instead of
    self because we can then use that class method and variable
    independently of having an instance of the shoe altogether. So I've
    hardcoded the header for use later via the class method below.
    """

    def __init__(self, country, code, product, cost, quantity):
        """Shoe constructor to initialise the object variables. Included
        are the methods, to evaluate object cost, quantity, display
        string and string format for the external txt file.
        I have added 2 methods directly to the initialization to ensure
        the attached methods intercept the incoming object data from the
        user and casts it to the the required data type.
        """
        self.country = country
        self.code = code
        self.product = product
        self.set_cost(cost)  # Initializing the method with attribute instance
        self.set_quantity(quantity)  # ""

    def set_cost(self, cost):
        """ Intercepting the data and casting or setting it to float.
        It can be received as a string or int to0 but will be converted
        to a float
        Args:
            cost (_float_): User input
        """
        self.cost = float(cost)

    def get_cost(self) -> float:
        """Return the value of the object cost
      Args:
            self (float): _object float_
    Returns:
            str: _object float_
        """
        return (self.cost)

    def set_quantity(self, quantity):
        """ Intercepting the data and casting or setting it to integer.
        It can be received as a string or int to0 but will be converted
        to a float.
        Args:
            cost (_int_): User input
        """
        self.quantity = int(quantity)

    def get_quantity(self) -> int:
        """_Return the value of the object quantity
      Args:
            self (str): _object string_
    Returns:
            str: _object string_
        """
        return (f"{self.quantity}")

    def __str__(self: str) -> str:
        """_return all variables as string outputs with pretext_
        Args:
            self (str): _variables as strings_
        Returns:
            str: _string_
        """
        return (
            f"Country:\t {self.country}\n"
            f"Code:\t\t {self.code}\n"
            f"Product:\t {self.product}\n"
            f"Cost:\t\t R {self.cost:.2f}\n"
            f"Quantity:\t {self.quantity}"
            )

    def txt_file_str(self: str) -> str:
        """_return all variables as string outputs for external txt
        file._
        Args:
            self (str): _variables as strings_
        Returns:
            str: _string_
        """
        return (f"{self.country},{self.code},{self.product},"
                f"{self.cost},{self.quantity}")

    @classmethod  # Defining the class method
    def get_header_string(cls):  # Using instance of class "cls" as argument
        """Act upon the class variable and set the desired output for
        printing
        back to the txt file."""
        return ",".join(cls.header) + "\n"


#  =============Shoe list===========

shoe_list = []  # List of objects

#  ==========Functions outside the class==============


def print_bold(text: str) -> None:
    """
    Emboldens given text and returns
    as string.
    :param text: Given text.
    """
    print(f"\033[1m{text}\033[0m")


def read_shoes_data():
    """Read, clean and strip txt data, initialise through the string
    class and append top the global list for use. I also miss teh 0
    index with using index splicing on the loop. Courtesy of Google.
    Returns:
        list[object]: _list containing class objects.
    """
    try:
        with open("inventory.txt", "r") as file:
            raw_data = file.readlines()[1:]
            for item in raw_data:
                cleaned_data = item.strip().split(",")
                shoe_list.append(Shoe(cleaned_data[0], cleaned_data[1],
                                      cleaned_data[2], cleaned_data[3],
                                      cleaned_data[4]))
    except FileNotFoundError:
        print("File inventory.txt not found, please check your"
              "directories.")


# Start and import data.


def capture_shoes():
    """Initialise user objects, append to the object list and prints
    to txt
    file.
    """
    print("CAPTURE YOUR SHOE DETAILS:\n ")
    country = input("Enter the country: ")
    sku = input("Enter the SKU code: SKU")
    product = input("Enter the product detail: ")
    while True:
        try:
            price = float(input("Enter the price: "))
            break
        except ValueError:
            print("Invalid entry, try again.")
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            break
        except Exception:
            print("Invalid entry, try again.")
    shoe_list.append(Shoe(country, sku, product, price, quantity))
    with open("inventory.txt", "a") as file:
        file.writelines(f"\n{country},SKU{sku},{product},{(price)},"""
                        f"{(quantity)}")


def view_all():
    """Access updated object list and display contents for the user
    using the
    __str__ method inside the class scope.
    """
    for count, item in enumerate(shoe_list, 1):
        print_bold(f"SHOE NO:\t {count}")
        print(f"{item}\n")


def re_stock():
    """Loops though to object list quantity element and determines the
    lowest value. This opens the user option to update that object's
    quantity with the same value as the returned value and return the
    updated value back to the object list and update the txt file.
    Solution of /n without adding a to the end of the file courtesy of
    Sulaiman using a generative declaration.
    """
    quantities = []
    for item in range(len(shoe_list)):
        quantities.append(int(shoe_list[item].quantity))
        min_item = min(quantities)
        if min_item == shoe_list[item].quantity:
            lowest_item = shoe_list[item]
    print("The lowest stock item is:\n", lowest_item)
    user = int(input("How many shoes do you want to add to this"
                     " range? "))
    update_item = min_item + user
    lowest_item.quantity = update_item
    with open("inventory.txt", "w") as file:
        file.write(Shoe.get_header_string())
        file.writelines("\n".join(item.txt_file_str()
                        for item in shoe_list))


def search_shoe():
    """Takes in the user SKU input and matches to the object list and
    displays
    to the user.
    """
    while True:
        user = input("Enter the shoe code: \n")
        for i in range(len(shoe_list)):
            if user == "" or user == " ":
                print("PLease enter the code correctly")
                user = input("Enter the shoe code: \n")
            elif user == shoe_list[i].code:
                print(shoe_list[i])
        break


def value_per_item():
    """Calculated the value of each's object's shoe based on the cost
    and the quantity.
    """
    for item in range(len(shoe_list)):
        value = shoe_list[item].cost * shoe_list[item].quantity
        print(f"The value for "
              f"{shoe_list[item].product} is R {value:.2f}.")


def highest_qty():
    """Determine the highest quantity amount in the object list
    and return
    the item as a sale item
    """
    quantities = []
    for item in range(len(shoe_list)):
        quantities.append(int(shoe_list[item].quantity))
        max_item = max(quantities)
        if max_item == shoe_list[item].quantity:
            highest_item = shoe_list[item]
    print(f"This item is for sale:\n\n{highest_item}")


def test():
    print("Hi")

# Start


# Call the function to import the data.
read_shoes_data()

#  ==========Main Menu=============


def menu():
    """Start menu to encapsulate the user menu and corresponding
    functions.
    """
    while True:
        menu = input("""
Select an option:

A : View Total Inventory
B : Search for a shoe
C : Add a shoe entry
D : Show lowest stock item
E : Show sale items
F : Show item value
G : Exit

""").lower()
        if menu == "a":
            view_all()
        elif menu == "b":
            search_shoe()
        elif menu == "c":
            capture_shoes()
        elif menu == "d":
            re_stock()
        elif menu == "e":
            highest_qty()
        elif menu == "f":
            value_per_item()
        elif menu == "g":
            exit()
        else:
            print("Please make sure you entered the correct option")


menu()
