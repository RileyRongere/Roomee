# Author: Nick Peters, Riley Rongere
# from insert_query_DB import *

# functions = mySQL()


# For use of the DB team to manually test insert and query functions, expand as needed
def main():
    user_input = "R"
    # connection = SQLite("http://localhost:9906/")
    while user_input != "Q":
        user_input = input("Input a character\n").upper()

        # insert_user function
        if user_input == "IU":
            Email = input("Email\n").lower()
            Passcode = input("Passcode\n").lower()
            functions.insert_user(Email, Passcode)

        #         # insert_user function
        #         if user_input == "IU":
        #             Email = input("Email\n").lower()
        #             Passcode = input("Passcode\n").lower()
        #             functions.insert_user(Email, Passcode)

        #         # insert_question function
        #         if user_input == "IQ":
        #             Question = input("Question\n").lower()
        #             functions.insert_question(Question)

        #         # insert_answer function
        #         if user_input == "IA":
        #             QuestionID = input("QuestionID\n").lower()
        #             UserID = input("UserID\n").lower()
        #             Answer = input("Answer\n").lower()
        #             functions.insert_answer(QuestionID, UserID, Answer)

        #         # insert_match function
        #         if user_input == "IM":
        #             UserID_1 = input("UserID_1\n").lower()
        #             UserID_2 = input("UserID_2\n").lower()
        #             PercentMatch = input("PercentMatch\n").lower()
        #             functions.insert_match(UserID_1, UserID_2, PercentMatch)

        #         # query_user_by_id function
        #         elif user_input == "QUE":
        #             Email = input("Email\n").lower()
        #             print(functions.query_user_by_email(Email))

        #         # query_user_by_email function
        #         elif user_input == "QUI":
        #             u_id = input("ID\n").lower()
        #             print(functions.query_user_by_id(u_id))

        #         # query_question function
        #         elif user_input == "QQ":
        #             q_id = input("question id\n")
        #             print(functions.query_question(q_id))

        #         # query_all_questions function
        #         elif user_input == "QAQ":
        #             print(functions.query_all_questions())

        #         # query_answer function
        #         elif user_input == "QA":
        #             u_id = input("user_id\n")
        #             print(functions.query_answer(u_id))

        #         # query_matches function
        #         elif user_input == "QM":
        #             u_id = input("user_id\n")
        #             print(functions.query_matches(u_id))

        # query_user_by_id function
        elif user_input == "QUE":
            Email = input("Email\n").lower()
            print(functions.query_user_by_email(Email))

        # query_user_by_email function
        elif user_input == "QUI":
            u_id = input("ID\n").lower()
            print(functions.query_user_by_id(u_id))

        # query_question function
        elif user_input == "QQ":
            q_id = input("question id\n")
            print(functions.query_question(q_id))

        # query_all_questions function
        elif user_input == "QAQ":
            print(functions.query_all_questions())

        # query_answer function
        elif user_input == "QA":
            u_id = input("user_id\n")
            print(functions.query_answer(u_id))

        # query_matches function
        elif user_input == "QM":
            u_id = input("user_id\n")
            print(functions.query_matches(u_id))


if __name__ == "__main__":
    main()
