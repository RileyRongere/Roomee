# Authors: Riley Rongere, Emma Gerdeman, Lane Affield
# For use by the API team to query and insert objects to the DB
from backend_py_objects import *
import sqlite3
import mysql.connector


def insert_user_version_2(username, passw, firstname, lastname):
    query = (
        "INSERT INTO USER "
        "(UserName, Passcode, FirstName, LastName) "
        "VALUES (%s, %s, %s, %s)"
    )
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            curr.execute(query, (username, passw, firstname, lastname))
        conn.commit()
    conn.close()


class database:
    def __init__(self):
        pass


class SQLite(database):
    def __init__(self, db_file):
        super().__init__()
        # connection = sqlite3.connect(db_file)
        # curr = connection.cursor()
        self.db_file = db_file

    # For use by the db team to convert info from the API to sql queries and inserts

    def insert_user(self, email, password):
        # Sql insert containing email and password
        query = "INSERT INTO USER (Email, Passcode) VALUES (?, ?)"
        with sqlite3.connect(self.db_file) as conn:
            with conn.cursor as curr:
                curr.execute(query, (email, password))
            conn.commit()
        conn.close()

    # NOT NECESSARY
    def insert_question(question):
        # Sql insert containing question
        connection = sqlite3.connect("setup.sql")
        curr = connection.cursor()
        curr.execute("INSERT INTO QUESTION (question) VALUES (?)", (question))
        connection.commit()
        connection.close()

    def insert_answer(self, question_id, user_id, answer):
        # Sql insert containing the username, user_id, and password
        query = "INSERT INTO ANSWER (Question_ID, User_ID, Answer) VALUES (?, ?, ?)"
        with sqlite3.connect(self.db_file) as conn:
            with conn.cursor as curr:
                curr.execute(query, (question_id, user_id, answer))
            conn.commit()
        conn.close()

    def insert_match(self, user1, user2, percent_match):
        # Sql insert containing user1, user2, percent_match
        with sqlite3.connect(self.db_file) as conn:
            query = "INSERT INTO MATCHES (User1, User2, Percent_Match) VALUES (?, ?, ?)"
            with conn.cursor as curr:
                curr.execute(query, (user1, user2, percent_match))
            conn.commit()
        conn.close()


# takes in a string email and returns a corresponding dict containing User information
def query_user(email):
    # connect to database
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            # sql query that returns a row from USER
            query = "Select * " "FROM USER " "WHERE UserName = (%s)"
            curr.execute(query, (email,))
            result = curr.fetchone()
            conn.close()
            if result is not None:
                return User(
                    result[0], result[1], result[2], result[3], result[4]
                ).return_dict()
            else:
                return {}
             

# takes in an int user_id and returns a corresponding dict containing User information
def query_user_by_id(user_id):
    # connect to database
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            # sql query that returns a row from USER
            query = "Select * " "FROM USER " "WHERE UserID = (%s)"
            curr.execute(query, (user_id,))
            result = curr.fetchone()
            conn.close()
            if result is not None:
                return User(
                    result[0], result[1], result[2], result[3], result[4]
                ).return_dict()
            else:
                return {}


# takes in an int question_id and returns a corresponding dict containing Question information
def query_question(question_id):
    # connect to database
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            query = "Select * " "FROM QUESTION " "WHERE QuestionID = (%s)"
            curr.execute(query, (question_id,))
            result = curr.fetchone()
            conn.close()
            if result is not None:
                # return a dictionary containing the question information (question_id,question)
                return Question(result[0], result[1]).return_dict()
            else:
                return {}


# takes in an int user_id and returns a corresponding list of Answer dicts
def query_answer(user_id):
    # connect to database
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            query = "Select * " "FROM ANSWER " "WHERE UserID = (%s)"
            curr.execute(query, (user_id,))
            result = curr.fetchall()
            conn.close()
            if result is not None:
                # build a list of Answer dictionaries to return
                return_list = []
                for i in range(len(result)):
                    # put a dictionary containing answer information (answer_id, user_id, question_id, answer) in the list
                    curr_answer = result[i]
                    new_element = Answers(
                        curr_answer[0], curr_answer[1], curr_answer[2], curr_answer[3]
                    )
                    return_list.append(new_element.return_dict())
                return return_list
            else:
                return {}


# takes in an int user_id and returns a corresponding list of Match dicts
def query_matches(user_id):
    # connect to database
    with mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    ) as conn:
        with conn.cursor() as curr:
            query = "Select * " "FROM MATCHES " "WHERE User_1 = (%s)"
            curr.execute(query, (user_id,))
            result = curr.fetchall()
            conn.close()
            if result is not None:
                # build a list of Matches dictionaries to return
                return_list = []
                for i in range(len(result)):
                    # put a dictionary containing match information (match_id, user1_id, user2_id, percent_match) in the list
                    curr_answer = result[i]
                    new_element = Matches(
                        curr_answer[0], curr_answer[1], curr_answer[2], curr_answer[3]
                    )
                    return_list.append(new_element.return_dict())
                return return_list
            else:
                return {}
             