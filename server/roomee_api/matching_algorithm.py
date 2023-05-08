# Matching Algorithm
# Authored by Kali Zerwas
import mysql.connector
from insert_query_DB import *

# Load Data:
cnx = mysql.connector.connect(
    user="MYSQL_USER",
    password="MYSQL_PASSWORD",
    host="localhost",
    database="roomee",
    port="9906",
)


query = "SELECT * FROM USER"

db = mySQL()
# Execute query
with cnx.cursor() as cursor:
    cursor.execute(query)

    # Print each row of results
    user_data2 = []
    for row in cursor:
        user_data2.append(row)
        user1 = row  # IDK how to actually get the user that had signed in yet

query2 = "SELECT * FROM ANSWER"

with cnx.cursor() as cursor:
    cursor.execute(query2)

    # Print each row of results
    answer_data = []
    for row in cursor:
        answer_data.append(row)


# New plan


def distance(user1, user2, question, answer_list):
    for answer in answer_list:
        if answer[2] == user1 and answer[1] == question:
            user1_answer = answer[3]
        if answer[2] == user2 and answer[1] == question:
            user2_answer = answer[3]
    score = abs(user1_answer - user2_answer)
    return score


def remove(user1, user2, q1, q2, user_list, user, answer_list):
    for answer in answer_list:
        if answer[2] == user1 and answer[1] == q1:
            user1_1 = answer[3]
        if answer[2] == user2 and answer[1] == q2:
            user2_2 = answer[3]
    if user1_1 == 1 and user2_2 == 0:
        user_list.remove(user)


def gender(user1, user2, user_list, user, answer_list):
    for answer in answer_list:
        if answer[2] == user1 and answer[1] == 23:
            user1_gender_answer = answer[3]
        if answer[2] == user2 and answer[1] == 23:
            user2_gender_answer = answer[3]
        if answer[2] == user1 and answer[1] == 24:
            user1_pref_answer = answer[3]
        if answer[2] == user2 and answer[1] == 24:
            user2_pref_answer = answer[3]
    if (
        user1_gender_answer != user2_pref_answer
        and user2_gender_answer != user1_pref_answer
    ):
        user_list.remove(user)
    if user1_pref_answer == 3 and user2_pref_answer == 3:
        user_list.append(user)


def match(user1, user_list, answer_list2):
    final_list = []
    answer_list3 = answer_list2.copy()
    answer_list = [
        answer for answer in answer_list2 if answer[1] not in [11, 12, 14, 15, 24]
    ]

    for user in user_list:
        if user in user_list:
            gender(user1[0], user[0], user_list, user, answer_list3)
        if user in user_list:
            remove(user1[0], user[0], 11, 12, user_list, user, answer_list3)
        if user in user_list:
            remove(user[0], user1[0], 11, 12, user_list, user, answer_list3)
        if user in user_list:
            remove(user1[0], user[0], 14, 15, user_list, user, answer_list3)
        if user in user_list:
            remove(user[0], user1[0], 14, 15, user_list, user, answer_list3)
    final_score_list = []
    for user in user_list:
        final_score = 0
        for answer in answer_list:
            if user[0] == answer[2]:
                if user in user_list:
                    score = distance(user1[0], user[0], answer[1], answer_list)
                    final_score = final_score + score
        final_score_list.append(final_score)
        db.insert_match(user1[0], user[0], final_score)
    return final_score_list


final_score = match(user1, user_data2, answer_data)

cnx.close()
