import pandas as pd 
from postgresql import pgConnect, pgEngine

df = pd.read_csv('global_superstore.csv')
print(df.head())

# Initiate PostgreSQL connection to DB
conn = pgConnect()
cur = conn.cursor()

# PostgreSQL connection doesn't work with Pandas so have initiated this engine as well with SQLAlchemy
engine = pgEngine()

df.to_sql('global_superstore',engine, schema='prototyping',if_exists='replace')
print('Successfully loaded data')