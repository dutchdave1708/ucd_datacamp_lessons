# just a simple evidence of accessing data from sql database using Python

import pandas as pd
from sqlalchemy import create_engine

sql = ""SELECT * FROM table_name""
engine = create_engine()

df = pd.read_sql_query(sql, engine)
df.head()