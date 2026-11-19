
import pandas as pd

# 1. Load the raw CSV
df = pd.read_csv(
    "data/raw/pakistan_cities.csv",
    encoding="latin1"
)

print("Raw data (first rows):")
print(df.head())

# 2. Rename columns to simpler names
df = df.rename(columns={
    "City": "city",
    "Pop (2023 Census)": "population_2023",
    "Pop (2017 Census)": "population_2017",
    "Pop (1998 Census)": "population_1998",
    "Pop (1981 Census)": "population_1981",
    "Pop (1972 Census)": "population_1972",
    "Province": "province"
})

# 3. Extract only the population numbers
population_columns = ["population_2023", "population_2017","population_1998","population_1981","population_1972"]

for column in population_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.replace(r"\s*\n.*", "", regex=True)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# 4. Remove rows with missing important values
df = df.dropna(subset=[
    "city",
    "population_2023",
    "population_2017",
    "population_1998",
    "population_1981",
    "population_1972",
    "province"
])

# 5. Convert population values to integers
for column in population_columns:
    df[column] = df[column].astype(int)

# 6. Remove duplicate rows
df = df.drop_duplicates()

# 7. Save cleaned data
df.to_csv(
    "data/processed/pakistan_cities_clean.csv",
    index=False
)

print("\nCleaned data saved successfully!")
print("Number of cities:", len(df))
print("\nCleaned data preview:")
print(df.head())
