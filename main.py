from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from TransformLoad import drop_col, change_col_name

# if statement for create db if no db exists

new_df_to_sql =change_col_name(drop_col(convert_dict_to_df()))

update_db(new_df_to_sql)
