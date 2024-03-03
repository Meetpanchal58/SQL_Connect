import mysql.connector
import pandas as pd

class MySQLOperation:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to the MySQL database")
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the MySQL database")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            records = cursor.fetchall()
            df = pd.DataFrame(records)
            return df
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    def insert_record(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Record inserted successfully")
        except mysql.connector.Error as e:
            print(f"Error inserting record: {e}")

    def update_record(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Record updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating record: {e}")

    def delete_record(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Record deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting record: {e}")

    def execute_alter(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Alter executed successfully")
        except mysql.connector.Error as e:
            print(f"Error executing alter: {e}")

    def execute_drop(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Drop executed successfully")
        except mysql.connector.Error as e:
            print(f"Error executing drop: {e}")

    def execute_truncate(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Truncate executed successfully")
        except mysql.connector.Error as e:
            print(f"Error executing truncate: {e}")

    def execute_modify(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Modify executed successfully")
        except mysql.connector.Error as e:
            print(f"Error executing modify: {e}")
