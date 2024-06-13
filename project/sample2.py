import sqlite3

class MenuManager:
    def __init__(self, db_name='menus.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS menus (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          menu TEXT NOT NULL,
                          price REAL)''')
        self.conn.commit()

    def add_menu(self):
        # Input menu name
        menu = input("Please enter a menu: ")
        
        # Input menu price
        while True:
            try:
                price = float(input("Please enter the price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price.")
        
        # Insert into database
        self.c.execute("INSERT INTO menus (menu, price) VALUES (?, ?)", (menu, price))
        self.conn.commit()
        print(f"Menu '{menu}' with price ${price:.2f} added to the database.")

    def list_menus(self):
        self.c.execute("SELECT id, menu, price FROM menus")
        rows = self.c.fetchall()
        if not rows:
            print("There are no menus currently.")
        else:
            print("Current Menus:")
            for row in rows:
                print(f"Menu #{row[0]}. {row[1]} - ${row[2]:.2f}")

    def delete_menu(self):
        self.list_menus()
        try:
            menu_to_delete = int(input("Enter the # to delete: "))
            self.c.execute("DELETE FROM menus WHERE id = ?", (menu_to_delete,))
            self.conn.commit()
            if self.c.rowcount > 0:
                print(f"Menu {menu_to_delete} has been removed.")
            else:
                print(f"Menu #{menu_to_delete} was not found.")
        except ValueError:
            print("Invalid input.")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    manager = MenuManager()
    print("Welcome to My FOOD APP :)")
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
            manager.add_menu()
        elif choice == "2":
            manager.delete_menu()
        elif choice == "3":
            manager.list_menus()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

    manager.close()
    print("Thank you")
