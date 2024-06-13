from database.connection import get_db_connection

class Menu:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @staticmethod
    def create(description, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menus (description, user_id) VALUES (?, ?)", (description, user_id))
        conn.commit()
        menu_id = cursor.lastrowid
        conn.close()
        return Menu(menu_id, description)

    @staticmethod
    def get_menus_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, description FROM menus WHERE user_id = ?", (user_id,))
        menus = [Menu(id, description) for id, description in cursor.fetchall()]
        conn.close()
        return menus

    @staticmethod
    def delete_menu(menu_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menus WHERE id = ?", (menu_id,))
        conn.commit()
        conn.close()
