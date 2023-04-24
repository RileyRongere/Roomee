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