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
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)