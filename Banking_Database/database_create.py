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

def initialize_database():

    """ initializes the database and creates the tables """
    connection = create_connection()

    if connection:

        try:
            cursor = connection.cursor()

            # create account table with the account number and account type
            cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                account_number TEXT UNIQUE NOT NULL,
                                name TEXT NOT NULL,
                                account_type TEXT NOT NULL,
                                balance REAL NOT NULL DEFAULT 0.0
                              );''')

            # create transactions table
            cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            account_id INTEGER NOT NULL,
                                            amount REAL NOT NULL,
                                            transaction_type TEXT NOT NULL,
                                            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                            FOREIGN KEY (account_id) REFERENCES accounts (account_id)
                                          );''')

            connection.commit()
            print("Database initialized successfully.")

        except sqlite3.Error as e:
            print(f"Error initializing tables: {e}")

        finally:
            connection.close()

