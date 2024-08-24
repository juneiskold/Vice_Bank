import random
import sqlite3

from Banking_Database.database_create import create_connection

def generate_account_number():

    """ generates a unique account number """
    return f"ACCT{random.randint(1000000, 999999)}"

def create_account(name, account_type):

    """ creates a new account with the given name and account type """

    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()

            # generate a unique account number
            account_number = generate_account_number()

            # insert new account into the account table
            cursor.execute("INSERT INTO accounts (account_number, name, account_type) VALUES (?, ?, ?)",
                           (account_number, name, account_type))

            conn.commit()

            # retrieve the auto-generated account_id
            cursor.execute("SELECT account_id, account_number FROM accounts WHERE account_number = ?",
                           (account_number,))

            account_number = cursor.fetchone()

            print(f"Account created successfully for {name}. Account number: {account_number[1]}")

        except sqlite3.Error as e:
            print(f"Error creating account: {e}")

        finally:
            conn.close()