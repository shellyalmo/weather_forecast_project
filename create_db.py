import sqlite3
import pandas as pd

connection = sqlite3.connect('TestDB.db')
cursor = connection.cursor()

# create table
cursor.execute('''CREATE TABLE Weather
                ([name] text, [temp] decimal(5,2), [temp_max] decimal(5,2), [temp_min] decimal(5,2), [humidity] decimal(5,2), [pressure] decimal(5,2), [wind_speed] decimal(5,2), [wind_deg] decimal(5,2))''')

connection.commit()
