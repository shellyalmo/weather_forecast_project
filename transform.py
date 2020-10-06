"""
>>> convert_kelvin_to_celsius(df)
      country   temp  temp_min  temp_max
ITA     Italy  71.85     16.85     69.85
ESP     Spain  15.85     24.85     59.85
GRC    Greece  59.85     25.85     60.85
FRA    France  38.85    -55.15     71.85
PRT  Portugal  35.85     14.85    -41.15

"""

import pandas as pd

# Fake data for testing
data = {'country': ['Italy', 'Spain', 'Greece', 'France', 'Portugal'],
        'temp': [345, 289, 333, 312, 309],
        'temp_min': [290, 298, 299, 218, 288],
        'temp_max': [343, 333, 334, 345, 232]}

df = pd.DataFrame(data, index=['ITA', 'ESP', 'GRC', 'FRA', 'PRT'])

# dont drop but keep
def drop_col(pandas_df):
    """ Drop unnecessary columns from the data frame
    """
    return pandas_df.drop(['coord.lon', 'coord.lat', 'weather', 'base', 'main.feels_like', 'visibility', 'clouds.all', 'sys.type', 'sys.id', 'sys.country', 'sys.sunrise', 'sys.sunset', 'timezone', 'id', 'cod'], axis=1)


def change_col_name(pandas_df_dropped):
    """ Change columns names to  match the SQL database.
    """
    return pandas_df_dropped.rename(columns={"main.temp": "temp", "main.temp_min": "temp_min", "main.temp_max": "temp_max", "main.pressure": "pressure", "main.humidity": "humidity", "wind.speed": "wind_speed", "wind.deg": "wind_deg"})


def convert_kelvin_to_celsius(pandas_df_dropped_changed):
    """ Convert the temp, temp_min, temp_max measurement unit from Kelvin to Celsius.
    """
    columns = ["temp", "temp_min", "temp_max"]
    for column in columns:
        pandas_df_dropped_changed[column] = pandas_df_dropped_changed[column] - 273.15
    return pandas_df_dropped_changed


def set_datetime_col_as_row_index(pandas_df_dropped_changed_converted):
    """ Set the datetime column to be the dataframe row index.
    """
    return pandas_df_dropped_changed_converted.set_index('dt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
