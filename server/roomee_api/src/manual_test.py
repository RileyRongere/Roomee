#from insert_query_DB import *
from other_insert import *

def main():
    user_input = "R"
    #connection = SQLite("http://localhost:9906/")
    while (user_input != "Q"):
        user_input = input("Input a character\n").upper()
        if(user_input == "U"):
            ema = input("email\n").lower()
            passw = input("password\n").lower()
            first = input("firstname\n").lower()
            last = input("lastname\n").lower()
            # gender = input("gender\n").lower()
            
            insert_user(ema, passw, first, last)
            #connection.insert_user(ema, passw)
        
        
if __name__ == "__main__":
    main()