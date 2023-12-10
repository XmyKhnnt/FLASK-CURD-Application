import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()


class DatabaseConnection:

    def __init__(self, dbname=os.getenv('db_name'), user=os.getenv('user'), password=os.getenv('pword'), host=os.getenv('host'), port=os.getenv('port')):

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):

        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("DB Successfully Connected")
        except psycopg2.Error as e:

            print("Error connecting to the database:", e)
            print("Error connecting to the database new", e)

    def execute_query(self, sql, params=None):
        if self.cursor:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            print("Error: Database connection not established.")

    def execute_none_query(self, sql, params=None):
        if self.cursor:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
        else:
            print("Error: Database connection not established.")

    def commit_and_close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else:
            print("Error: Database connection not established.")
