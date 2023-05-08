# # Authored by Kali Zerwas

# from matching_algorithm import *
# from pytest import fixture
# from unittest.mock import patch


def test():
    pass


# def test_distance():
#     answer_list = [(1, 1, 1, 4), (2, 1, 2, 2), (3, 2, 1, 3), (4, 2, 2, 3)]
#     user1 = 1
#     user2 = 2
#     question = 1
#     expected_score = 2
#     assert distance(user1, user2, question, answer_list) == expected_score


# def test_remove():
#     user_list = [(1, "alice@email.com", "Alice"), (2, "bob@email.com", "Bob")]
#     answer_list = [(1, 11, 1, 1), (2, 12, 2, 0)]
#     user = (2, "bob@email.com", "Bob")
#     user1 = 1
#     user2 = 2
#     q1 = 11
#     q2 = 12
#     remove(user1, user2, q1, q2, user_list, user, answer_list)
#     assert user_list == [(1, "alice@email.com", "Alice")]


# def test_gender():
#     user_list = [(1, "alice@email.com", "Alice"), (2, "bob@email.com", "Bob")]
#     answer_list = [(1, 23, 1, 1), (1, 24, 1, 3), (2, 23, 2, 0), (2, 24, 2, 3)]
#     user1 = 1
#     user2 = 2
#     user = (2, "bob@email.com", "Bob")
#     gender(user1, user2, user_list, user, answer_list)
#     assert user_list == [(1, "alice@email.com", "Alice"), (2, "bob@email.com", "Bob")]


# def test_match():
#     user_list = [(1, "Alice"), (2, "Bob")]
#     answer_list = [
#         (1, 1, 1, 4),
#         (2, 1, 2, 2),
#         (3, 2, 1, 3),
#         (4, 2, 2, 3),
#         (1, 23, 1, 1),
#         (1, 24, 1, 3),
#         (2, 23, 2, 0),
#         (2, 24, 2, 3),
#         (1, 11, 1, 1),
#         (2, 12, 2, 1),
#         (1, 11, 2, 1),
#         (2, 12, 1, 1),
#         (1, 14, 1, 1),
#         (2, 15, 2, 1),
#         (1, 14, 2, 1),
#         (2, 15, 1, 1),
#     ]
#     user1 = (1, "Alice")
#     user = (2, "Bob")
#     expected_score = [3, 0]
#     final_score = match(user1, user_list, answer_list)
#     assert final_score == expected_score
