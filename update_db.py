import sqlite3
import pandas as pd
from create_db import connection


def update_db(pandas_df):
    """ Upload pandas dataframe to sql database
    """
    pandas_df.to_sql('Weather', connection, if_exists='append', index=False)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
