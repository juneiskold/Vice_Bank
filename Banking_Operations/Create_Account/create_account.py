import random
from Banking_Database.database_create import create_connection

def generate_account_number():

    """ generates a unique account number """
    return f"ACCT{random.randint(1000000, 999999)}"