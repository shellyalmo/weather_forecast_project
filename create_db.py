import sqlite3

def create_new_DB():
    connection = sqlite3.connect('TestDB.db')
    cursor = connection.cursor()


