""" This file is extracting, transforming and loading the weather data.
"""
import pandas as pd

# Trnasforming the data stored in pandas


def drop_col(pandas_df):
    """ Drop unnecessary columns from the data frame
    """
    return pandas_df.drop(['coord.lon', 'coord.lat', 'weather', 'base', 'main.feels_like', 'visibility', 'clouds.all', 'sys.type', 'sys.id', 'sys.country', 'sys.sunrise', 'sys.sunset', 'timezone', 'id', 'cod'], axis=1)


def change_col_name(pandas_df_dropped):
    """ Change columns names to  match the SQL database.
    """
    return pandas_df_dropped.rename(columns={"main.temp": "temp", "main.temp_min": "temp_min", "main.temp_max": "temp_max", "main.pressure": "pressure", "main.humidity": "humidity", "wind.speed": "wind_speed", "wind.deg": "wind_deg"})


# Loading to the database
