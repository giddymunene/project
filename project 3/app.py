from database.setup import create_tables
from models.user import User
from models.menu import Menu

def main():
    create_tables()
    print("Welcome to the menu app :)")
    user_name = input("Enter your name: ")
    user = User.get_user_by_name(user_name)
    if not user:
        user = User.create(user_name)

    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new menu")
        print("2. Delete a menu")
        print("3. List menus")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            menu_description = input("Please enter a menu: ")
            user.add_menu(menu_description)
        elif choice == "2":
            user.delete_menu()
        elif choice == "3":
            user.list_menus()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye")

if __name__ == "__main__":
    main()
