import sqlite3

from Banking_Database.database_create import create_connection

def withdraw(account_id, amount):
    """Withdraws the specified amount from the account."""
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Check if balance is sufficient
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
            balance = cursor.fetchone()

            if balance and balance[0] >= amount:
                # Update account balance
                cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))

                # Record transaction
                cursor.execute("INSERT INTO transactions (account_id, amount, transaction_type) VALUES (?, ?, 'WITHDRAW')", (account_id, amount))

                conn.commit()
                print(f"Withdrew {amount} from account {account_id}.")
            else:
                print("Insufficient balance.")

        except sqlite3.Error as e:
            print(f"Error withdrawing money: {e}")
        finally:
            conn.close()
