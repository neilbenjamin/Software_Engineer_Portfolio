""" Task 11 - Level 2 - SQLite
The task requirements did not stipulate whether or not if the commands had to
written in the python file or in the db browser application, so I did both.
Below are the python commands and I have also included all the screen shots and
results for each command as well as teh commands written in the DB Browser.
"""
import sqlite3
try:
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                   grade INTEGER)
    """)
    db.commit()
    # name variables
    id1 = 55
    name1 = 'Carl Davis'
    grade1 = 61
    id2 = 66
    name2 = "Dennis Fredrickson"
    grade2 = 88
    id3 = 77
    name3 = "Jane Richards"
    grade3 = 78
    id4 = 12
    name4 = "Peyton Sawyer"
    grade4 = 45
    id5 = 2
    name5 = "Lucas Brooke"
    grade5 = 99
    student_data = [(id1, name1, grade1), (id2, name2, grade2),
                    (id3, name3, grade3), (id4, name4, grade4),
                    (id5, name5, grade5)]
    # INSERT table
    cursor.executemany("""
    INSERT INTO python_programming(id, name, grade)
                VALUES(?, ?, ?)""", student_data)
    print("Student data inserted")
    db.commit()
    # Question 1 - SELECT Data
    lower_value = 60
    higher_value = 80
    cursor.execute('SELECT * FROM python_programming WHERE grade > ? '
                   'AND grade < ?', (lower_value, higher_value))
    student_average = cursor.fetchone()
    print(student_average)
    # Question 2 - UPDATE Data
    grade = 65
    change_name = 'Carl Davis'
    cursor.execute("""UPDATE python_programming SET grade = ?
                   WHERE name = ?""", (grade, change_name))
    update_grade = cursor.fetchone()
    db.commit()
    print(update_grade)
    # Question 3  - DELETE record
    id = 66
    cursor.execute("""DELETE FROM python_programming WHERE id = ?""",
                   (id,))
    db.commit()
    # Question 4 - DROP Table
    cursor.execute("""DROP TABLE python_programming""")
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
