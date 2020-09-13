"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> convert_json_to_python(response)
120
"""
import pandas as pd
import json
def convert_json_to_python(response):
    return json.dumps(response)

# def create_pandas_df_from_API(convert_json_to_python()):
#     copied_dict = {'temp': response[['temp']], 'temp_min':response[['temp_min']], 'temp_max':response[['temp_max']], 'pressure':response['pressure'], 'humidity':response['humidity'], 'wind_speed': response['speed'], 'wind_deg':response['deg']}

#     pandas_df = pd.DataFrame(copied_dict, columns=[
#                              'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'wind_deg'])
#     return pandas_df

if __name__ == "__main__":
    import doctest
    doctest.testmod()