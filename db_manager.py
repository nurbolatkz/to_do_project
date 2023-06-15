import sqlite3

class DatabaseManager(object):
    """sqlite3 database class that holds testers jobs"""
    __DB_LOCATION = "appDataBase.db"

    
    def __init__(self):
        self.__db_connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.connection.cursor()
        # ...
    def __del__(self):
        self.__db_connection.close()
        
    def execute(self, new_data):
        self.cur.execute(new_data)
    def get_user(self, username):
        query = '''SELECT user from users where username = {username}'''
        self.cur.execute(query)
        return self.cur.fetchone()
    def create_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES({username}, {email}, {password})"
        self.cur.execute(query)
        
    def commit(self):
        self.cur.commit()