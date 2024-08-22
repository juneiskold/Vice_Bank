import sqlite3
import os

database_path = './Banking_Database/banking.db'

def create_connection():

    """ creates and returns a connection to the SQLite database """