from create_pandas_df import convert_json_to_python
from update_db import weather_df, update_db

# from update_db import
# if statement for create db if no db exists
# call function from current_weather file, and get the response

# (convert_json_to_python(response))
# print(create_pandas_df_from_API(response))
# call update_db function

update_db(weather_df)
