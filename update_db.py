import sqlite3
import pandas as pd
from current_weather_by_city_ID_API import response

weather_data = [['Jerusalem', 'Israel', 29.0], [
    'Madrid', 'Spain', 26.8], ['Beirut', 'Lebanon', 28.3]]

# Create the pandas DataFrame
weather_df = pd.DataFrame(weather_data, columns=['City', 'Country', 'Temp'])

# insert to db
weather_df.to_sql('Weather', connection, if_exists='replace', index=False)

# cursor.execute('''
#                 INSERT INTO Weather(City, Country, Temp)''')

# connection.commit()
