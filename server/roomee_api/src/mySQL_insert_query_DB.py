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
      self.user="MYSQL_USER"
      self.password="MYSQL_PASSWORD"
      self.host="localhost"
      self.port="9906"
      self.database="roomee"


   def insert_user(self, Email, Passcode):
   # Sql insert containing Email and Passcode
      query = (
         "INSERT INTO USER "
         "(Email, Passcode) "
         "VALUES (%s, %s)"
      )
      with mysql.connector.connect(
         self.user,
         self.password,
         self.host,
         self.port,
         self.database,
      ) as conn:
         with conn.cursor() as curr:
               curr.execute(query, (Email, Passcode))
         conn.commit()
      conn.close()


   def insert_question(self, Question):
   # Sql insert containing Question
      query = (
         "INSERT INTO QUESTION "
         "(Question) "
         "VALUES (%s)"
      )
      with mysql.connector.connect(
         self.user,
         self.password,
         self.host,
         self.port,
         self.database,
      ) as conn:
         with conn.cursor() as curr:
               curr.execute(query, (Question))
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
         self.user,
         self.password,
         self.host,
         self.port,
         self.database,
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
         self.user,
         self.password,
         self.host,
         self.port,
         self.database,
      ) as conn:
         with conn.cursor() as curr:
               curr.execute(query, (UserID_1, UserID_2, PercentMatch))
         conn.commit()
      conn.close()




   def query_user_by_id(self , User_id): # cahnge to username
      # connect to database
      with sqlite3.connect(self.db_file) as conn:   # create the query string containing user_id
         query = "SELECT * FROM USER WHERE UserID = (?);"
         with conn.cursor() as curr:
            curr.execute(query, (User_id))
            result = curr.fetchone()
            if result is not None:
               # return a dictionary containing the user information (user_id,email,pasword)
                  return User(result[0], result[1], result[2]).return_dict()
            else:
                  return {}
 
   def query_user_by_email(self , email): # cahnge to username
      # connect to database
      with sqlite3.connect(self.db_file) as conn:   # create the query string containing user_id
         query = "SELECT * FROM USER WHERE Email = (?);"
         with conn.cursor() as curr:
            curr.execute(query, (email))
            result = curr.fetchone()
            if result is not None:
               # return a dictionary containing the user information (user_id,email,pasword)
                  return User(result[0], result[1], result[2]).return_dict()
            else:
                  return {}
 


   def query_question(self,question_id):
      # connect to database
      with sqlite3.connect(self.db_file) as conn:
         query = 'SELECT *  FROM QUESTION WHERE QuestionID = (?);'
         with conn.cursor() as curr:
            curr.execute(query, (question_id))
            result = curr.fetchone()
            if result is not None:
            # return a dictionary containing the question information (question_id,question)
               return Question(result[0], result[1]).return_dict()
            else:
                return {}

      # c reate the query string containing question_id
      

   # sql query that returns a row from QUESTION



   def query_answer(self, user_id): #change to user id
      # connect to database
      with sqlite3.connect( self.db_file) as conn:
         query = 'SELECT * FROM ANSWER WHERE UserID = (?);'
         with conn.cursor() as curr:
            # create the query string containing answer_id
            # sql query that returns a row from ANSWER
            curr.execute(query,(user_id))
            result = curr.fetchall()
            if result is not None:
               # return a dictionary containing the question information (answer_id, user_id, question_id, answer)
                  return_list = []
     # return a dictionary containing the question information (match_id, user1_id, user2_id, percent_match)
                  for i in range(len(result[0])):
                     new_element = Answers(result[0], result[1], result[2], result[3])[i]
                     return_list.append(new_element.return_dict())
                  return return_list
            else:
               return {}


   def query_match(self, user_id): #change to user id
      # connect to database
      with sqlite3.connect( self.db_file) as conn:
         # create the query string containing user_id
         query = 'SELECT * FROM MATCHES WHERE User_1 = (?);'
         with conn.cursor() as curr:
            # sql query that returns a row from Matches
            curr.execute(query,(user_id))
            result = curr.fetchone()
            if result is not None:
               # return a dictionary containing the question information (match_id, user1_id, user2_id, percent_match)
                  return_list = []
     # return a dictionary containing the question information (match_id, user1_id, user2_id, percent_match)
                  for i in range(len(result[0])):
                     new_element = Matches(result[0], result[1], result[2], result[3])[i]
                     return_list.append(new_element.return_dict())
                  return return_list
            else:
               return {}
