import sqlite3
import pandas as pd
from current_weather_by_city_ID_API import response
from create_db import connection, cursor


def update_db(pandas_df,table_name=str):
    pandas_df.to_sql(table_name, connection, if_exists='replace', index=False)


weather_data = [['Jerusalem', 'Israel', 29.0], [
    'Madrid', 'Spain', 26.8], ['Beirut', 'Lebanon', 28.3]]

# Create the pandas DataFrame
weather_df = pd.DataFrame(weather_data, columns=['City', 'Country', 'Temp'])

if __name__ == "__main__":
    import doctest
    doctest.testmod()