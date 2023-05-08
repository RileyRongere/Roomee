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
    # db.insert_question("How often do you smoke?")
    # db.insert_question("Are you a procrastinator?")
    # db.insert_question("How neat are you?")
    db.insert_question("When do you go to sleep?")
    db.insert_question("When do you wake up?")
    db.insert_question("Do you have any pets?")
    db.insert_question("Are you open to living with pets?")
    db.insert_question("How often do you like to invite friends over?")
    db.insert_question("Do you smoke?")
    db.insert_question("Are you comfortable with your roommate smoking?")
    db.insert_question("Are you introverted or extroverted")
    db.insert_question("How clean do you keep your space?")
    db.insert_question("How loud do you like your space?")
    db.insert_question("How often are you in your space?")
    db.insert_question("How busy are you during the week?")
    db.insert_question("How busy are you during the weekend?")
    db.insert_question("What is your age?")
    db.insert_question("What is your gender?")
    db.insert_question("What is your preferred gender to live with?")
    # (Question_ID, User_ID, Answer)
    # insert some answers
    # Sleep
    db.insert_answer(9, 9, 3)
    db.insert_answer(9, 10, 1)
    db.insert_answer(9, 11, 4)
    # Wake up
    db.insert_answer(10, 9, 5)
    db.insert_answer(10, 10, 4)
    db.insert_answer(10, 11, 4)
    # Pets
    db.insert_answer(11, 9, 1)
    db.insert_answer(11, 10, 0)
    db.insert_answer(11, 11, 0)
    # ok with pets
    db.insert_answer(12, 9, 1)
    db.insert_answer(12, 10, 1)
    db.insert_answer(12, 11, 0)
    # friends
    db.insert_answer(13, 9, 4)
    db.insert_answer(13, 10, 3)
    db.insert_answer(13, 11, 2)
    # smoking
    db.insert_answer(14, 9, 0)
    db.insert_answer(14, 10, 0)
    db.insert_answer(14, 11, 0)
    # ok with smoking
    db.insert_answer(15, 9, 0)
    db.insert_answer(15, 10, 0)
    db.insert_answer(15, 11, 0)
    # into or extro
    db.insert_answer(16, 9, 1)
    db.insert_answer(16, 10, 0)
    db.insert_answer(16, 11, 1)
    # clean
    db.insert_answer(17, 9, 5)
    db.insert_answer(17, 10, 2)
    db.insert_answer(17, 11, 5)
    # noise
    db.insert_answer(18, 9, 0)
    db.insert_answer(18, 10, 2)
    db.insert_answer(18, 11, 4)
    # how often in space
    db.insert_answer(19, 9, 1)
    db.insert_answer(19, 10, 1)
    db.insert_answer(19, 11, 4)
    # busy during week
    db.insert_answer(20, 9, 2)
    db.insert_answer(20, 10, 2)
    db.insert_answer(20, 11, 4)
    # busy during weekend
    db.insert_answer(21, 9, 1)
    db.insert_answer(21, 10, 3)
    db.insert_answer(21, 11, 4)
    # age
    db.insert_answer(22, 9, 2)
    db.insert_answer(22, 10, 2)
    db.insert_answer(22, 11, 3)
    # gender
    db.insert_answer(23, 9, 0)
    db.insert_answer(23, 10, 0)
    db.insert_answer(23, 11, 0)
    # pref gender
    db.insert_answer(24, 9, 3)
    db.insert_answer(24, 10, 3)
    db.insert_answer(24, 11, 3)

    # (User1, User2, Percent_Match)
    # insert some matches
    db.insert_match(9, 10, 75)
    db.insert_match(9, 11, 40)
    db.insert_match(10, 11, 10)


if __name__ == "__main__":
    main()
