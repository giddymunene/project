import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('menus.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS menus (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             menu TEXT NOT NULL)''')

conn.commit()

def addMenu():
    menu = input("Please enter a menu: ")
    c.execute("INSERT INTO menus (menu) VALUES (?)", (menu,))
    conn.commit()
    print(f"Menu '{menu}' added to the database.")

def addPrice():
    price = input("Please enter price: ")
    c.execute("INSERT INTO menus (price) VALUES (?)", (price,))
    conn.commit()
    print(f"Menu '{price}' added to the database.")


def listMenus():
    c.execute("SELECT id, menu FROM menus")
    rows = c.fetchall()
    if not rows:
        print("There are no menus currently.")
    else:
        print("Current Menus:")
        for row in rows:
            print(f"Menu #{row[0]}. {row[1]}")

def deleteMenu():
    listMenus()
    try:
        menuToDelete = int(input("Enter the # to delete: "))
        c.execute("DELETE FROM menus WHERE id = ?", (menuToDelete,))
        conn.commit()
        if c.rowcount > 0:
            print(f"Menu {menuToDelete} has been removed.")
        else:
            print(f"Menu #{menuToDelete} was not found.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to My FOOD APP :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new menu")
        print("2. Add menu price")
        print("3. Delete a menu")
        print("4. List menus")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addMenu()
        elif choice == "2":
            addPrice()
        elif choice == "3":
            deleteMenu()    
        elif choice == "4":
            listMenus()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    # Close the database connection before exiting
    conn.close()
    print("Thank you")
