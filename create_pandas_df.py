import pandas as pd

def create_pandas_df_from_API(response):
    copied_dict = {'temp': response.main.temp, 'temp_min':response.main.temp_min, 'temp_max':response..temp_max, 'pressure':response.pressure, 'humidity':response.humidity, 'wind_speed': response.wind.speed, 'wind_deg':response.wind.deg}

    pandas_df = pd.DataFrame(copied_dict, columns=[
                             'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'wind_deg'])
    return pandas_df

