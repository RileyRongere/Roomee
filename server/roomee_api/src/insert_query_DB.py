# Authors: Riley Rongere, Emma Gerdeman, Lane Affield 

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
   '''
   def insert_question(question):
      # Sql insert containing question
      connection = sqlite3.connect('setup.sql')
      curr = connection.cursor()
      curr.execute("INSERT INTO QUESTION (question) VALUES (?)", (question))
      connection.commit()
      connection.close()
   '''

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



   #THE BELOW IS A POTENTIAL PARTIAL IMPLEMENTATION OF THE GET_USER FUNCTION. FEEL FREE TO CHANGE COMPLETELY
   def query_user(user_id): # may need to change from 'user_id' to 'username'
      # connect to database
      #TODO: code for above


      # create the query string containing user_id
      #TODO: I don't know if this query is correct so please
      #       verify and adjust as needed
      query = '''
               select *
               from USER
               where Username = {};
               '''.format(user_id)
      

      # sql query that returns a row from USER
      #TODO: call the db using 'query' 
      
      
      # return a dictionary containing the user information (username, password, potentially user_id if api team needs it)
      return User(user_id,username,password).return_dict()

      # THE BELOW IS AN ALTERNATE OF THE ABOVE LINE. Not sure if the above will work. RR
      # user = User(user_id,username,password)
      # return user.return_dict
      pass

   def query_question(question_id):
      pass

   def query_answer(question_id):
      pass

   def query_match(question_id):
      pass