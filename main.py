from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from TransformLoad import drop_col, change_col_name

# if statement for create db if no db exists
# call function from current_weather file, and get the response

# (convert_json_to_python(response))
# print(create_pandas_df_from_API(response))
# call update_db function
convert_dict_to_df()
print(change_col_name(drop_col(convert_dict_to_df())))
# update_db(weather_df)
