import pandas as pd
import sqlite3

# Read the cleaned city data
df = pd.read_csv("data/processed/pakistan_cities_clean.csv")

# Connect to (or create) the SQLite database in data/pakistan_data.db
conn = sqlite3.connect("data/pakistan_data.db")
cursor = conn.cursor()

# (Optional) Drop the table if it already exists to start fresh
cursor.execute("DROP TABLE IF EXISTS cities;")

# Write the DataFrame to a new table named 'cities'
# This creates the table and inserts all rows.
df.to_sql(name="cities", con=conn, index=False)

conn.commit()
conn.close()
print(f"Loaded {len(df)} rows into table 'cities' in SQLite database.")
