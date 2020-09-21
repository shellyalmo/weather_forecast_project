import sqlite3
import pandas as pd
from create_db import connection


def update_db(pandas_df):
    pandas_df.to_sql('Weather', connection, if_exists='replace', index=False)


# weather_data = [['Tel Aviv', 1599661762, 333, 334, 324, 65, 1003, 23, 325], [
#     'Tel Aviv', 1599661762, 457, 765, 224, 68, 1034, 67, 324], ['Tel Aviv', 1599661762, 335, 338, 312, 45, 1007, 22, 329]]

# # Create the pandas DataFrame
# weather_df = pd.DataFrame(weather_data, columns=[
#                           'name', 'date_time', 'temp', 'temp_max', 'temp_min', 'humidity', 'pressure', 'wind_speed', 'wind_deg'])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
