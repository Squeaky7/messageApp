import os
import json
import getpass

# Set File Path
usrlist_path = os.path.join("usr_list.json")

def create_account():
    new_name = input("Enter your new user name: ")
    
    try:
        with open(usrlist_path, 'r') as file:
            ids = json.load(file)

        for id in ids:
            id_list = []
            id_list.append(id['userId'])
        
        max_id = max(id_list)
        new_id_pre = int(max_id) + 1
        new_id = "0" * (10 - len(str(new_id_pre))) + str(new_id_pre)

        print(f"Account ID is {new_id}\nAccount name is \"{new_name}\"")


    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
        print(f"Error was happened: {e}")

def login_process(usrlist, usrname):

    try:
        with open(usrlist, 'r', encoding= 'utf-8') as file:
            usrs = json.load(file)

        for item in usrs:
            if item.get("name") == usrname:
                passw = item.get("password")
                enter_pass = getpass.getpass("Enter password: ")
                if enter_pass == passw:
                    return "Logged in correctly."
                else:
                    return "Incorrect password."
            
            else:
                print("Do you want create new account[y/N]: ")
                new_account = input().upper()
                
                if new_account == "Y":
                    print("Create new account")
                    create_account()
                    return "New account created"
                else:
                    print("Exiting program.")
                    return "Login process exited"

    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
        print(f"Error was happened: {e}")
        return "An error occurred"


def main():
    while True:
        print("1. Login\n2. Exit\n")
        select_menu = input("Select an option: ").strip()

        if select_menu == "1":
            usrname = input("Enter your username: ").strip()
            password = login_process(usrlist_path, usrname)
            print(password)

        elif select_menu == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

main()

