# Author: Nick Peters
from insert_query_DB import *


# For use of the DB team to manually test insert and query functions, expand as needed
def main():
    user_input = "R"
    # connection = SQLite("http://localhost:9906/")
    while user_input != "Q":
        user_input = input("Input a character\n").upper()
        if user_input == "IU":
            ema = input("email\n").lower()
            passw = input("password\n").lower()
            first = input("firstname\n").lower()
            last = input("lastname\n").lower()
            insert_user_version_2(ema, passw, first, last)

        elif user_input == "SU":
            ema = input("email\n").lower()
            print(query_user(ema))

        elif user_input == "SQ":
            q_id = input("question id\n")
            print(query_question(q_id))

        elif user_input == "SA":
            u_id = input("user_id\n")
            print(query_answer(u_id))


if __name__ == "__main__":
    main()
