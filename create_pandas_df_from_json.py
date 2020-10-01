"""
>>> convert_json_to_dict("data1600689959.json")
{'coord': {'lon': 34.78, 'lat': 32.08}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 303.84, 'feels_like': 303.4, 'temp_min': 302.04, 'temp_max': 305.37, 'pressure': 1010, 'humidity': 52}, 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 310}, 'clouds': {'all': 0}, 'dt': 1600689959, 'sys': {'type': 1, 'id': 6845, 'country': 'IL', 'sunrise': 1600658915, 'sunset': 1600702755}, 'timezone': 10800, 'id': 293397, 'name': 'Tel Aviv', 'cod': 200}

>>> convert_dict_to_df("data1600689959.json")

"""


import pandas as pd
import json
from pandas.io.json import json_normalize


def convert_json_to_dict(filename):
    """ Convert json file to python dictionary
    """
    with open(filename, 'r') as JSON:
        json_dict = json.load(JSON)
    return json_dict


def convert_dict_to_df(filename):
    """ Convert python dictionary to pandas dataframe
    """
    return pd.json_normalize(convert_json_to_dict(filename))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
