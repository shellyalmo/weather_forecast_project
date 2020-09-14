"""
This is the "example" module.

The example module supplies one function, factorial().  For example,
 convert_json_to_dict()
{"coord": {"lon": 34.78, "lat": 32.08}, "weather": [{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"}], "base": "stations", "main": {"temp": 303.85, "feels_like": 305.28, "temp_min": 302.59, "temp_max": 304.82, "pressure": 1006, "humidity": 62}, "visibility": 10000, "wind": {"speed": 5.1, "deg": 320}, "clouds": {"all": 20}, "dt": 1599661762, "sys": {"type": 1, "id": 6845, "country": "IL", "sunrise": 1599621680, "sunset": 1599666917}, "timezone": 10800, "id": 293397, "name": "Tel Aviv", "cod": 200}
"""
import pandas as pd
import json
from pandas.io.json import json_normalize


def convert_json_to_dict():
    """ Convert json file to dict dataframe
    """
    with open('current_weather_by_city_ID_API.json', 'r') as JSON:
        json_dict = json.load(JSON)
    return json_dict
# print(convert_json_to_dict())

def convert_dict_to_df():
    return pd.json_normalize(convert_json_to_dict())

print(convert_dict_to_df())

# def create_dict_df_from_API(convert_json_to_dict()):
#     copied_dict = {'temp': response[['temp']], 'temp_min':response[['temp_min']], 'temp_max':response[['temp_max']], 'pressure':response['pressure'], 'humidity':response['humidity'], 'wind_speed': response['speed'], 'wind_deg':response['deg']}

#     dict_df = pd.DataFrame(copied_dict, columns=[
#                              'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'wind_deg'])
#     return dict_df

if __name__ == "__main__":
    import doctest
    doctest.testmod()