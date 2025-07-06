""" Task 12 - Level 2 - Capstone
Found the input validation quite challenging and need to book another
call with a mentor to gain a deeper understanding with the uses of the
try/except and while True loops. I also got caught a few times with the
not adding the trailing , to indicate the use of the tuple and not the
individual characters in the string leading to incorrect binding errors.
I tested all the outputs with db browser as well. Relied quite heavily on the
2 previous task notes to assist with db entries and correct syntax.

"""
import sqlite3
try:
    db = sqlite3.connect("ebookstore.db")
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE book(id INTEGER PRIMARY KEY, title TEXT, author TEXT,
                   qty INTEGER)
    """)
    db.commit()
    # name variables
    id1 = 3001
    title1 = 'A Tale of Two Cities '
    author1 = 'Charles Dickens'
    qty1 = 30
    id2 = 3002
    title2 = 'Harry Potter and the Philosopher\'s Stone'
    author2 = 'J.K. Rowling'
    qty2 = 40
    id3 = 3003
    title3 = 'The Lion, the Witch and the Wardrobe'
    author3 = 'C. S. Lewis '
    qty3 = 25
    id4 = 3004
    title4 = 'The Lord of the Rings'
    author4 = 'J.R.R Tolkien'
    qty4 = 37
    id5 = 3005
    title5 = 'Alice in Wonderland '
    author5 = 'Lewis Carroll'
    qty5 = 12
    inventory_data = [(id1, title1, author1, qty1), (id2, title2, author2,
                      qty2), (id3, title3, author3, qty3), (id4, title4,
                      author4, qty4), (id5, title5, author5, qty5)]
    # INSERT table
    cursor.executemany("""
    INSERT INTO book(id, title, author, qty)
                VALUES(?, ?, ?, ?)""", inventory_data)
    print("Book data inserted")
    db.commit()
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()


def insert_book():
    try:
        # Form inputs
        # while True:
        #     try:
        #         user_id = int(input("Please enter a numerical ID: "))
        #         break
        #     except ValueError:
        #         print("Please ensure that you only use numerical inputs")
        while True:
            user_title = input("Enter the book title: ")
            if user_title == "":
                print("Please enter the book's title.")
            else:
                user_title
                break
        while True:
            user_author = input("Enter the author: ")
            if user_author == "":
                print("Please enter the author's details.")
            else:
                user_author
                break
        while True:
            try:
                user_qty_str = input("Please enter a numerical quantity: ")
                user_qty = int(user_qty_str)
                break
            except ValueError:
                print("Please ensure that you only use numerical inputs")
        # db_commands
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        # Auto ID Increment courtesy of Google pass None as a parameter for id.
        cursor.execute("""
        INSERT INTO book(id, title, author, qty)
                    VALUES(?, ?, ?, ?)""", (None, user_title,
                                            user_author, user_qty))
        print("New book record added to the database")
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_book_data():
    try:
        # db_commands
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM book
        """)
        book_db = cursor.fetchall()
        for index, record in enumerate(book_db, 1):
            print(f"{index} {record}\n")
        while True:
            try:
                select_index = int(input("Select a book index no. to "
                                         "update the book record: "))
                break
            except ValueError:
                print("Please enter a integer to select the correct record.\n")
        selected_index = book_db[select_index - 1]
        print(f"You selected: {selected_index}: ")
        selected_id = selected_index[0]
        while True:
            user_title = input("Update the book title: ")
            if user_title == "":
                print("Please update the book's title.")
            else:
                user_title
                break
        while True:
            user_author = input("Update the author: ")
            if user_author == "":
                print("Please update the author's details.")
            else:
                user_author
                break
        while True:
            try:
                user_qty_str = input("Please update the numerical quantity: ")
                user_qty = int(user_qty_str)
                break
            except ValueError:
                print("Please ensure that you only use numerical inputs")
                # db_commands
        cursor.execute("""
        UPDATE book SET title = ?,
                        author = ?,
                        qty = ?
                        WHERE id = ?""", (user_title,
                                          user_author, user_qty,
                                          selected_id))
        print("Book record updated on the database")
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def search_data():
    try:
        user_search = input("Please enter the book title: ")
        # db_commands
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM book WHERE title = ?""",
                       (user_search,))
        display_search = cursor.fetchall()
        if not display_search:
            print("Sorry, this book does not exist in our database.")
        else:
            print(f"Your search returned: \n{display_search}")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_book():
    try:
        # db_commands
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM book
        """)
        book_db = cursor.fetchall()
        for index, record in enumerate(book_db, 1):
            print(f"{index} {record}\n")
        while True:
            try:
                select_index = int(input("Select a book index to delete: "))
                break
            except ValueError:
                print("Please enter a integer to select the correct record.\n")
        selected_index = book_db[select_index - 1]
        selected_id = selected_index[0]
        # db_commands
        cursor.execute("""
        DELETE FROM book WHERE id = ?""", (selected_id,))
        print(f"Successfully deleted {selected_index}")
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def menu_start():
    while True:
        menu = input("""
            1. Enter book
            2. Update book
            3. Delete book
            4. Search books
            0. Exit
            """)
        if menu == '1':
            insert_book()
        elif menu == '2':
            update_book_data()
        elif menu == '3':
            delete_book()
        elif menu == '4':
            search_data()
        elif menu == '0':
            exit()
        else:
            print("Please ensure you've entered the correct number")


menu_start()
