# Authors: Riley Rongere, Emma Gerdeman

from backend_py_objects import *
import sqlite3

# For use by the API team to query and insert objects to the DB

def insert_user(email,password):
   # Sql insert containing email and password
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()
   curr.execute("INSERT INTO user (email, password) VALUES (?, ?)", (email, password))
   connection.commit()
   connection.close()


def insert_question(question):
   # Sql insert containing question
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()
   curr.execute("INSERT INTO question (question) VALUES (?)", (question))
   connection.commit()
   connection.close()


def insert_answer(question_id,user_id,answer):
   # Sql insert containing the username, user_id, and password
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()
   curr.execute("INSERT INTO answer (question_id, user_id, answer) VALUES (?, ?, ?)", (question_id, user_id, answer))
   connection.commit()
   connection.close()


def insert_match(user1,user2,percent_match):
   # Sql insert containing user1, user2, percent_match
   connection = sqlite3.connect('setup.sql')
   curr = connection.cursor()
   curr.execute("INSERT INTO matches (user1, user2, percent_match) VALUES (?, ?, ?)", (user1, user2, percent_match))
   connection.commit()
   connection.close()


def query_user(user_id):
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


def query_answer(answer_id):
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


def query_match(match_id):
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