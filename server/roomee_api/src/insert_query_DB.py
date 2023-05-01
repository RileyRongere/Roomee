# Authors: Riley Rongere, Emma Gerdeman, Lane Affield, Nick Wharff, Nick Peters

# For use by the API team to query and insert objects to the DB
from backend_py_objects import *
import mysql.connector

class mySQLdatabase:
   def __init__(self):
      pass

class mySQL(mySQLdatabase):
    def __init__(self):
        super().__init__() 
        self.user = "MYSQL_USER"
        self.password = "MYSQL_PASSWORD"
        self.host = "localhost"
        self.port = "9906"
        self.database = "roomee"


    def insert_user(self, Email, Passcode):
    # Sql insert containing Email and Passcode
        query = (
            "INSERT INTO USER "
            "(Email, Passcode) "
            "VALUES (%s, %s)"
        )
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                curr.execute(query, (Email, Passcode))
            conn.commit()
        conn.close()

    #TODO: CURRENTLY DOES NOT WORK!
    def insert_question(self, Question):
    # Sql insert containing Question
        query = (
            "INSERT INTO QUESTION "
            "(Question) "
            "VALUES (%s)"
        )
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                curr.execute(query, (Question,))
            conn.commit()
        conn.close()


    def insert_answer(self, QuestionID, UserID, Answer):
    # Sql insert containing the QuestionID, UserID, Answer
        query = (
            "INSERT INTO ANSWER "
            "(QuestionID, UserID, Answer) "
            "VALUES (%s, %s, %s)"
        )
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                curr.execute(query, (QuestionID, UserID, Answer))
            conn.commit()
        conn.close()


    def insert_match(self, UserID_1, UserID_2, PercentMatch):
    # Sql insert containing UserID_1, UserID_2, PercentMatch
        query = (
            "INSERT INTO MATCHES "
            "(UserID_1, UserID_2, PercentMatch) "
            "VALUES (%s, %s, %s)"
        )
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                curr.execute(query, (UserID_1, UserID_2, PercentMatch))
            conn.commit()
        conn.close()



    # takes in a string Email and returns a corresponding dict containing User information
    def query_user_by_email(self, Email):
        # connect to database
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                # sql query that returns a row from USER
                query = (
                    "Select * "
                    "FROM USER "
                    "WHERE Email = (%s)"
                )
                curr.execute(query, (Email,))
                result = curr.fetchone()
                conn.close()
                if result is not None:
                    return User(
                        result[0], result[1], result[2]
                    ).return_dict()
                else:
                    return {}
                

    # takes in an int UserID and returns a corresponding dict containing User information
    def query_user_by_id(self, UserID):
        # connect to database
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                # sql query that returns a row from USER
                query = (
                    "Select * "
                    "FROM USER "
                    "WHERE UserID = (%s)"
                )
                curr.execute(query, (UserID,))
                result = curr.fetchone()
                conn.close()
                if result is not None:
                    return User(
                        result[0], result[1], result[2]
                    ).return_dict()
                else:
                    return {}


    # takes in an int QuestionID and returns a corresponding dict containing Question information
    def query_question(self, QuestionID):
        # connect to database
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                query = (
                    "Select * "
                    "FROM QUESTION "
                    "WHERE QuestionID = (%s)"
                )
                curr.execute(query, (QuestionID,))
                result = curr.fetchone()
                conn.close()
                if result is not None:
                    # return a dictionary containing the question information (QuestionID, Question)
                    return Question(result[0], result[1]).return_dict()
                else:
                    return {}


    # takes in an int UserID and returns a corresponding list of Answer dicts
    def query_answer(self, UserID):
        # connect to database
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                query = (
                    "Select * "
                    "FROM ANSWER "
                    "WHERE UserID = (%s)"
                )
                curr.execute(query, (UserID,))
                result = curr.fetchall()
                conn.close()
                if result is not None:
                    # build a list of Answer dictionaries to return
                    return_list = []
                    for i in range(len(result)):
                        # put a dictionary containing answer information (AnswerID, UserID, QuestionID, Answer) in the list
                        curr_answer = result[i]
                        new_element = Answers(
                            curr_answer[0], curr_answer[1], curr_answer[2], curr_answer[3]
                        )
                        return_list.append(new_element.return_dict())
                    return return_list
                else:
                    return {}


    # takes in an int UserID and returns a corresponding list of Match dicts
    def query_matches(self, UserID):
        # connect to database
        with mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database,
        ) as conn:
            with conn.cursor() as curr:
                query = (
                    "Select * "
                    "FROM MATCHES "
                    "WHERE UserID_1 = (%s)"
                )
                curr.execute(query, (UserID,))
                result = curr.fetchall()
                conn.close()
                if result is not None:
                    # build a list of Matches dictionaries to return
                    return_list = []
                    for i in range(len(result)):
                        # put a dictionary containing match information (MatchID, UserID_1, UserID_2, PercentMatch) in the list
                        curr_answer = result[i]
                        new_element = Matches(
                            curr_answer[0], curr_answer[1], curr_answer[2], curr_answer[3]
                        )
                        return_list.append(new_element.return_dict())
                    return return_list
                else:
                    return {}