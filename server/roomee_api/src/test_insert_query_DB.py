#Authored by Lane Affield, Emma Gerdeman, Nick Wharff

from src.roomee_api import app
import pytest
import mysql.connector
from backend_py_objects import *
from insert_query_DB import mySQL
from insert_query_DB import mySQLdatabase
from backend_py_objects import *
import mysql.connector


def test_init_db():
    my_db = mySQLdatabase()
    assert isinstance(my_db, mySQLdatabase)
        

def test_init():
    my_sql = mySQL()
    assert isinstance(my_sql , mySQL)
    assert my_sql.user == "MYSQL_USER"
    assert my_sql.password == "MYSQL_PASSWORD"
    assert my_sql.host == "localhost"
    assert my_sql.port == "9906"
    assert my_sql.database == "roomee"

    
    
def test_insert_user():
    my_sql = mySQL()
    email = "test_email@example.com"
    passcode = "test_password"
    my_sql.insert_user(email, passcode)
    user_dict = my_sql.query_user_by_email(email)
    assert isinstance(user_dict, dict)
    assert user_dict['email'] == email
    assert user_dict['password'] == passcode
    
def test_insert_question():
    my_sql = mySQL()
    question = "test_question"
    my_sql.insert_question(question)
    question_dict = my_sql.query_question(9)
    assert isinstance(question_dict, dict)
    assert question_dict['question'] == question
    
def test_insert_answer():
    my_sql = mySQL()
    question_id = 1
    user_id = 1
    answer = 5
    my_sql.insert_answer(question_id, user_id, answer)
    answer_list = my_sql.query_answer(user_id)
    assert isinstance(answer_list, list)
    assert answer_list[0]['question_id'] == question_id
    assert answer_list[0]['user_id'] == user_id
    assert answer_list[0]['answer'] == answer
    
def test_insert_matches():
    my_sql = mySQL()
    user_1 = 1
    user_2 = 2
    percent_match = 50.0
    my_sql.insert_match(user_1, user_2, percent_match)
    match_dict = my_sql.query_matches(user_1)
    assert isinstance(match_dict, list)
    assert match_dict[0]['user1_id'] == user_1
    assert match_dict[0]['user2_id'] == user_2
    assert match_dict[0]['percent_match'] == percent_match

   
def test_query_user_by_email():
    my_sql = mySQL()
    email = "test_email@example.com"
    user_dict = my_sql.query_user_by_email(email)
    assert isinstance(user_dict, dict)
    assert user_dict['email'] == email 
    assert user_dict['password'] == "test_password" 

    
def test_query_user_by_id():
    my_sql = mySQL()
    user_id = 1
    user_dict = my_sql.query_user_by_id(user_id)
    assert isinstance(user_dict, dict)
    assert user_dict == {}
    
def test_query_question():
    my_sql = mySQL()
    question_id = 1
    question_dict = my_sql.query_question(question_id)
    assert isinstance(question_dict, dict)
    assert question_dict == {}
    
def test_query_answer():
    my_sql = mySQL()
    user_id = 1
    answer_list = my_sql.query_answer(user_id)
    assert isinstance(answer_list, list)
    #the 0 is necessary so that it will only check to see if the first instance is correct
    assert answer_list[0] == {'answer': 5, 'id': 9, 'question_id': 1, 'user_id': user_id}

