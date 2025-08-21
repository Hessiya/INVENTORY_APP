import configparser
import mysql.connector
from mysql.connector import Error

class DBConnection:
    """Singleton class for DB connection"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DBConnection, cls).__new__(cls)
            cls.__instance.__initialize()
        return cls.__instance

    def __initialize(self):
        """Initialize DB connection"""
        self.connection = None   # ensure attribute always exists
        try:
            config = configparser.ConfigParser()
            config.read("db_config.ini")

            self.connection = mysql.connector.connect(
                host=config.get("mysql", "host"),
                user=config.get("mysql", "user"),
                password=config.get("mysql", "password"),
                database=config.get("mysql", "database")
            )

            if self.connection.is_connected():
                print("Connected to MySQL Database..")

        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def get_connection(self):
        return self.connection
