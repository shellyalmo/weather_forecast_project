from current_weather_by_city_ID_API import response
from create_pandas_df import create_pandas_df_from_API
# from update_db import
# if statement for create db if no db exists
# call function from current_weather file, and get the response


print(create_pandas_df_from_API(response))
# call update_db function
