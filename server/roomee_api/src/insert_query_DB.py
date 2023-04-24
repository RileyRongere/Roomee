# Authors: Riley Rongere, Emma Gerdeman, Lane Affield
# For use by the API team to query and insert objects to the DB
from backend_py_objects import *
import sqlite3

class database:
   def __init__(self):
      pass

class SQLite(database):
   def __init__(self,db_file):
      super().__init__() 
      #connection = sqlite3.connect(db_file)
      #curr = connection.cursor()
      self.db_file = db_file

class SQLite(database):
   def __init__(self,db_file):
      super().__init__() 
      #connection = sqlite3.connect(db_file)
      #curr = connection.cursor()
      self.db_file = db_file

# For use by the db team to convert info from the API to sql queries and inserts

   def insert_user(self,email,password):
   # Sql insert containing email and password
      query = "INSERT INTO USER (Email, Password) VALUES (?, ?)"
      with sqlite3.connect(self.db_file ) as conn: 
         with conn.cursor as curr:
            curr.execute(query , (email, password) )
         conn.commit()
      conn.close()


   #NOT NECESSARY
   def insert_question(question):
      # Sql insert containing question
      connection = sqlite3.connect('setup.sql')
      curr = connection.cursor()
      curr.execute("INSERT INTO QUESTION (question) VALUES (?)", (question))
      connection.commit()
      connection.close()
   

   def insert_answer(self,question_id,user_id,answer):
      # Sql insert containing the username, user_id, and password
      query = "INSERT INTO ANSWER (Question_ID, User_ID, Answer) VALUES (?, ?, ?)"
      with sqlite3.connect(self.db_file ) as conn: 
         with conn.cursor as curr:      
            curr.execute(query , (question_id, user_id, answer))
         conn.commit()
      conn.close()


   def insert_match(self, user1,user2,percent_match):
      # Sql insert containing user1, user2, percent_match
      with sqlite3.connect(self.db_file ) as conn: 
         query = "INSERT INTO MATCHES (User1, User2, Percent_Match) VALUES (?, ?, ?)"
         with conn.cursor as curr:
            curr.execute(query, (user1, user2, percent_match))
         conn.commit()
      conn.close()


def query_user(user_id): # cahnge to username
   # connect to database
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()

   # create the query string containing user_id
   query = ''' SELECT *
      FROM USER
      WHERE UserID = {};
      ''' .format(user_id)

   # sql query that returns a row from USER
   curr.execute(query)
   result = curr.fetchone()

   if result is not None:
      # return a dictionary containing the user information (user_id,email,pasword)
      return User(result[0], result[1], result[2]).return_dict()
   else:
      return {}


def query_question(question_id):
   # connect to database
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()

   # create the query string containing question_id
   query = ''' SELECT *
      FROM QUESTION
      WHERE QuestionID = {};
      ''' .format(question_id)

   # sql query that returns a row from QUESTION
   curr.execute(query)
   result = curr.fetchone()

   if result is not None:
      # return a dictionary containing the question information (question_id,question)
      return Question(result[0], result[1]).return_dict()
   else:
      return {}


def query_answer(answer_id): #change to user id
   # connect to database
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()

   # create the query string containing answer_id
   query = ''' SELECT *
      FROM ANSWER 
      WHERE AnswerID = {};
      ''' .format(answer_id)

   # sql query that returns a row from ANSWER
   curr.execute(query)
   result = curr.fetchone()

   if result is not None:
      # return a dictionary containing the question information (answer_id, user_id, question_id, answer)
      return Answers(result[0], result[1], result[2], result[3]).return_dict()
   else:
      return {}


def query_match(match_id): #change to user id
   # connect to database
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()

   # create the query string containing user_id
   query = ''' SELECT *
      FROM MATCHES
      WHERE MatchID ={};
      ''' .format(match_id)

   # sql query that returns a row from Matches
   curr.execute(query)
   result = curr.fetchone()

   if result is not None:
      # return a dictionary containing the question information (match_id, user1_id, user2_id, percent_match)
      return Matches(result[0], result[1], result[2], result[3]).return_dict()
   else:
      return {}