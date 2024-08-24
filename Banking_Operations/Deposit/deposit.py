import sqlite3

from Banking_Database.database_create import create_connection

def deposit(account_id, amount):

    """ deposits the specified amount into the account."""
    if amount <= 0:
        print("Deposit amount must be a positive.")
        return

    conn = create_connection()
    if conn:

        try:
            cursor = conn.cursor()

            # update account balance
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
                           (amount, account_id))

            # record transaction
            cursor.execute("INSERT INTO transactions (account_id, amount, transaction_type) VALUES (?, ?, 'DEPOSIT')",
                           (account_id, amount))

            conn.commit()
            print(f"Deposited {amount} into the account {account_id}.")

        except sqlite3.Error as e:
            print("Error depositing the amount.", e)

        finally:
            conn.close()