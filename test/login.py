import os
import json
import getpass

# Set File Path
usrlist_path = os.path.join("usr_list.jsonl")

# Create New Account
def create_account():
    new_name = input("Enter your new user name: ")
    
    try:
        with open(usrlist_path, 'r') as file:
            ids = json.load(file)

        # Make IDs List
        id_list = []
        for id in ids:
            id_list.append(id['userId'])
        
        # Create New ID
        max_id = max(id_list)
        new_id_pre = int(max_id) + 1
        new_id = "0" * (10 - len(str(new_id_pre))) + str(new_id_pre)

        print(f"Account ID is {new_id}\nAccount name is \"{new_name}\"")

        # Set Password
        setpass = True
        while setpass:
            get_password = getpass.getpass("Enter your new password: ")
            check_pass = getpass.getpass("Enter the password again: ")

            if get_password == check_pass:
                print("Password saved.")
                setpass = False
            else:
                print("Wrong password.")

        new_account_entry = {
            "name": new_name,
            "userId": new_id,
            "password": get_password
        }

        # write_date = json.dumps(new_account_entry,indent=2)
        # print(write_date)

        # Enter to JSON File
        with open(usrlist_path, 'r', encoding='utf-8') as f:
            usrdata = []
            for line in f:
                try:
                    usrdata.append(json.loads(line.strip()))
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid line: {line.strip()}\n{e}")


        with open(usrlist_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(new_account_entry, ensure_ascii=False) + "\n")

    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
        print(f"Error was happened: {e}")

def login_process(usrlist, usrname):

    try:
        with open(usrlist, 'r', encoding= 'utf-8') as file:
            usrs = []
            for line in file:
                try:
                    usrs.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    print(f"Error decoding line: {line.strip()}")

        for item in usrs:
            if item.get("name") == usrname:
                passw = item.get("password")

                passbool = True
                while passbool:
                    enter_pass = getpass.getpass("Enter password: ")
                    if enter_pass == passw:
                        passbool = False
                        return "Logged in correctly."
                    else:
                        print("Incorrect password.")
                return

            print(f"Account name \"{usrname}\" not found.\nDo you want create new account[y/N]: ")
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

