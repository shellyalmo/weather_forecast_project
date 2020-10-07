"""
>>> convert_kelvin_to_celsius(df_test)
      country   temp  temp_min  temp_max  pressure  humidity  wind_speed  wind_deg radiation
ITA     Italy  71.85     16.85     69.85        12        56         110       180      high
ESP     Spain  15.85     24.85     59.85        13        67          90       189       low
GRC    Greece  59.85     25.85     60.85        14        64          98       178    medium
FRA    France  38.85    -55.15     71.85        15        63          99       177   average
PRT  Portugal  35.85     14.85    -41.15        11        62         100       190       low

>>> keep_col(df_test)
      temp  temp_min  temp_max  pressure  humidity  wind_speed  wind_deg
ITA  71.85     16.85     69.85        12        56         110       180
ESP  15.85     24.85     59.85        13        67          90       189
GRC  59.85     25.85     60.85        14        64          98       178
FRA  38.85    -55.15     71.85        15        63          99       177
PRT  35.85     14.85    -41.15        11        62         100       190
"""

import pandas as pd

# Fake data for testing
data_for_test = {'country': ['Italy', 'Spain', 'Greece', 'France', 'Portugal'],
                         'temp': [345, 289, 333, 312, 309],
                         'temp_min': [290, 298, 299, 218, 288],
                         'temp_max': [343, 333, 334, 345, 232],
                         'pressure': [12,13,14,15,11],
                         'humidity': [56,67,64,63,62],
                         'wind_speed': [110,90,98,99,100],
                         'wind_deg': [180,189,178,177,190],
                         'radiation':['high','low','medium','average','low']}

df_test = pd.DataFrame(data_for_test, index=[
                               'ITA', 'ESP', 'GRC', 'FRA', 'PRT'])


def keep_col(pandas_df):
    """ Keep only the necessary columns of the dataframe
    """
    return pandas_df[['temp','temp_min','temp_max','pressure','humidity','wind_speed','wind_deg']]


def change_col_name(pandas_df_kept):
    """ Change columns names to  match the SQL database.
    """
    return pandas_df_kept.rename(columns={"main.temp": "temp", "main.temp_min": "temp_min", "main.temp_max": "temp_max", "main.pressure": "pressure", "main.humidity": "humidity", "wind.speed": "wind_speed", "wind.deg": "wind_deg"})


def convert_kelvin_to_celsius(pandas_df_kept_changed):
    """ Convert the temp, temp_min, temp_max measurement unit from Kelvin to Celsius.
    """
    columns = ["temp", "temp_min", "temp_max"]
    for column in columns:
        pandas_df_kept_changed[column] = pandas_df_kept_changed[column] - 273.15
    return pandas_df_kept_changed


def set_datetime_col_as_row_index(pandas_df_kept_changeded):
    """ Set the datetime column to be the dataframe row index.
    """
    return pandas_df_kept_changeded.set_index('dt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
