from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from transform import drop_col, change_col_name, convert_kelvin_to_celsius
from get_weather_data_from_OpenWeatherMap import get_current_weather_data_from_OpenWeatherMap, write_weather_data_in_json_file

# if statement for create db if no db exists
filename = write_weather_data_in_json_file(get_current_weather_data_from_OpenWeatherMap())
new_df_to_sql = convert_kelvin_to_celsius(change_col_name(drop_col(convert_dict_to_df(filename))))

update_db(new_df_to_sql)
