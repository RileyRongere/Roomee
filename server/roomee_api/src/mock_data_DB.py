# Authored by priscilla Tuazon
from backend_py_objects import *
from insert_query_DB import *
import mysql.connector

db = mySQL()


def main():
    # (Email, Password)
    # insert some users
    db.insert_user("alice@email.com", "alice")  # ID = 9
    db.insert_user("bob@email.com", "bob")  # ID = 10
    db.insert_user("maddie@email.com", "maddie")  # ID = 11

    # (question)
    # insert some questions
    db.insert_question("How often do you smoke?")
    db.insert_question("Are you a procrastinator?")
    db.insert_question("How neat are you?")

    # (Question_ID, User_ID, Answer)
    # insert some answers
    db.insert_answer(9, 9, 3)
    db.insert_answer(9, 10, 1)
    db.insert_answer(9, 11, 4)

    db.insert_answer(10, 9, 5)
    db.insert_answer(10, 10, 4)
    db.insert_answer(10, 11, 4)

    db.insert_answer(11, 9, 2)
    db.insert_answer(11, 10, 3)
    db.insert_answer(11, 11, 3)

    # (User1, User2, Percent_Match)
    # insert some matches
    db.insert_match(9, 10, 75)
    db.insert_match(9, 11, 40)
    db.insert_match(10, 11, 10)


if __name__ == "__main__":
    main()
