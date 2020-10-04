from create_db import create_DB_connection, close_connection
from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from transform import drop_col, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from get_weather_data_from_OpenWeatherMap import get_current_weather_data_from_OpenWeatherMap, write_weather_data_in_json_file

returned_connection = create_DB_connection()
filename = write_weather_data_in_json_file(
    get_current_weather_data_from_OpenWeatherMap())
new_df_to_sql = set_datetime_col_as_row_index(convert_kelvin_to_celsius(
    change_col_name(drop_col(convert_dict_to_df(filename)))))

update_db(new_df_to_sql, returned_connection)

close_connection(returned_connection)
