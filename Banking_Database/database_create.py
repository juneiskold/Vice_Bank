import sqlite3
import os

database_path = './Banking_Database/banking.db'

def create_connection():

    """ creates and returns a connection to the SQLite database """
    connection = None

    try:
        connection = sqlite3.connect(database_path)
        return connection

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    return connection
