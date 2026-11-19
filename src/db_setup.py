import sqlite3
import pandas as pd

# 1. Connect (or create) SQLite DB
conn = sqlite3.connect("data/pakistan.db")
cur = conn.cursor()
print("SQLite database 'pakistan.db' ready.")

# 2. Create table for cities
create_table_sql = """
CREATE TABLE IF NOT EXISTS cities (
    city TEXT,
    population_2023 INTEGER,
    population_2017 INTEGER,
    population_1998 INTEGER,
    population_1981 INTEGER,
    population_1972 INTEGER,
    province TEXT
);
"""
cur.execute(create_table_sql)
print("Table 'cities' created.")

# 3. Load cleaned data into DataFrame
df_clean = pd.read_csv("data/processed/pakistan_cities_clean.csv")

# 4. Insert data into the table
rows = df_clean.to_records(index=False)
cur.executemany("INSERT OR REPLACE INTO cities VALUES (?, ?, ?, ?, ?,?,?);", rows)
conn.commit()
print("Imported {} records into 'cities' table.".format(len(rows)))

# 5. Close connection
conn.close()
