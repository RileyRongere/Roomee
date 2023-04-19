# Authors: Riley Rongere

# objects should only be created when api requests information

# COMMENTED OUT FUNCITONS CAN BE USER IF NEED BE. IF NOT NEEDED DELETE RR

class Question:
    '''
    python object that serves as the format for questions to be stored in the database
    '''
    def __init__(self, id, question):
        self.__id = id
        self.__question = question

        self.__dictionary = {
            'id' : self.__id,
            'email' : self.__question,
        }

    def return_dict(self):
        return self.__dictionary

    # def get_id(self):
    #     return self.__id

    # def get_question(self):
    #     return self.__question
    
    # def update_question(self,new_question):
    #     self.__question = new_question


class User:
    '''
    python object that serves as the format for Users to be stored in the database
    '''
    def __init__(self, id, email, password):
        self.__id = id
        self.__email = email
        self.__password = password

        self.__dictionary = {
            'id' : self.__id,
            'email' : self.__email,
            'password' : self.__password,
        }

    def return_dict(self):
        return self.__dictionary

    # def get_id(self):
    #     return self.__id

    # def get_first_name(self):
    #     return self.__password

    # def get_first_name(self):
    #     return self.__first_name
    
    # def get_last_name(self):
    #     return self.__last_name
    
    # def get_gender(self):
    #     return self.__gender
    
    # def update_first_name(self,new_first_name):
    #     self.__first_name = new_first_name

    # def update_last_name(self,new_last_name):
    #     self.__last_name = new_last_name

    # def update_gender(self,new_gender):
    #     self.__gender = new_gender


class Matches:
    '''
    python object that serves as the format for Matches to be stored in the database
    '''
    def __init__(self, id, user1, user2, percent_match):
        self.__id = id
        self.__user1 = user1
        self.__user2 = user2
        self.__percent_match = percent_match

        self.__dictionary = {
            'id' : self.__id,
            'email' : self.__user1,
            'password' : self.__user2,
            'percent_match' : self.__percent_match,
        }

    def return_dict(self):
        return self.__dictionary

    # def get_id(self):
    #     return self.__id

    # def get_user1(self):
    #     return self.__user1

    # def get_user2(self):
    #     return self.__user2
    
    # def get_percent_match(self):
    #     return self.__percent_match
    
    # def update_user1(self,new_user):
    #     self.__user1 = new_user

    # def update_user2(self,new_user):
    #     self.__user2 = new_user

    # def update_percent_match(self,new_percent_match):
    #     self.__percent_match = new_percent_match

class Answers:
    '''
    python object that serves as the format for Answers to be passed to API
    '''
    def __init__(self, id, user_id, question_id, answer):
        self.__id = id
        self.__user_id = user_id
        self.__question_id = question_id
        self.__answer = answer

        self.__dictionary = {
            'id' : self.__id,
            'email' : self.__user_id,
            'password' : self.__question_id,
            'answer' : self.__answer
        }

    def return_dict(self):
        return self.__dictionary

    # def get_id(self):
    #     return self.__id

    # def get_user_id(self):
    #     return self.__user_id

    # def get_question_id(self):
    #     return self.__question_id
    
    # def get_answer(self):
    #     return self.__answer
    
    # def update_user_id(self,new_user_id):
    #     self.__user_id = new_user_id

    # def update_question_id(self,new_question_id):
    #     self.__question_id = new_question_id

    # def update_answer(self,new_answer):
    #     self.__answer = new_answer