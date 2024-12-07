import login

def main():
    while True:
        print("1. Login\n2. Exit\n")
        select_menu = input("Select an option: ").strip()

        if select_menu == "1":
            usrname = input("Enter your username: ").strip()
            login.login_process(usrname)

        elif select_menu == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

main()
