import sqlite3
import pandas as pd

connection = sqlite3.connect('TestDB.db')
cursor = connection.cursor()

# create table
cursor.execute('''CREATE TABLE Weather
                ([City] text, [Country] text, [Temp] integer)''')

connection.commit()
