menus = []


def addMenu():
  menu = input("Please enter a menu: ")
  menus.append(menu)
  print(f"Menu '{menu}' added to the list.")


def listMenus():
  if not menus:
    print("There are no menus currently.")
  else:
    print("Current Menus:")
    for index, menu in enumerate(menus):
      print(f"Menu #{index}. {menu}")


def deleteMenu():
  listMenus()
  try:
    menuToDelete = int(input("Enter the # to delete: "))
    if menuToDelete >= 0 and menuToDelete < len(menus):
      menus.pop(menuToDelete)
      print(f"Menu {menuToDelete} has been removed.")
    else:
      print(f"Task #{menuToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  ### Create a loop to run the app
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

    if (choice == "1"):
      addMenu()
    elif (choice == "2"):
      deleteMenu()
    elif (choice == "3"):
      listMenus()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("Thank you")