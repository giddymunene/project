from database.connection import get_db_connection
from models.menu import Menu

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return User(user_id, name)

    @staticmethod
    def get_user_by_name(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1])
        else:
            return None

    def add_menu(self, menu_description):
        menu = Menu.create(menu_description, self.id)
        print(f"Menu '{menu.description}' added to {self.name}'s list.")

    def list_menus(self):
        menus = Menu.get_menus_by_user(self.id)
        if not menus:
            print(f"{self.name} has no menus currently.")
        else:
            print(f"{self.name}'s Current Menus:")
            for index, menu in enumerate(menus):
                print(f"Menu #{index}. {menu}")

    def delete_menu(self):
        menus = Menu.get_menus_by_user(self.id)
        if not menus:
            print(f"{self.name} has no menus to delete.")
            return

        for index, menu in enumerate(menus):
            print(f"Menu #{index}. {menu.description}")

        try:
            menu_to_delete = int(input("Enter the # to delete: "))
            if 0 <= menu_to_delete < len(menus):
                menu = menus[menu_to_delete]
                Menu.delete_menu(menu.id)
                print(f"Menu '{menu.description}' has been removed from {self.name}'s list.")
            else:
                print(f"Menu #{menu_to_delete} was not found.")
        except ValueError:
            print("Invalid input.")
