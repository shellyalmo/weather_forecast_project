import sqlite3


def create_DB_connection():
    """ Connect to a database and create cursor object for executing SQL statements.
    """
    connection = sqlite3.connect('CurrentWeatherDB.db', uri=True)
    print("Connection with database established ..........")
    connection.cursor()
    return connection


def close_connection(connection):
    """ Close connection with the database.
    """
    connection.commit()
    connection.close()
