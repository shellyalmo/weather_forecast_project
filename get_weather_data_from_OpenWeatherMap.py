from dotenv import load_dotenv
import os
import requests
import json

def get_current_weather_data_from_OpenWeatherMap(id="293397"):
    """ Returns current weather data by city id (Tel Aviv by default)
    """
    load_dotenv()
    json_data = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?id="+id+"&appid="+os.environ.get("api-token")).json()
    return json_data


def write_weather_data_in_json_file(json_data):
    """ Save current weather data to a json file.
        Name the file by the Unix Timestamp.
    """
    name = 'data' + str(json_data['dt'])
    filename = "%s.json" % name
    with open(filename, 'w') as f:
        json.dump(json_data, f)
    return filename


