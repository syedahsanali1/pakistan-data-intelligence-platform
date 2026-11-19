import pandas as pd

# Load Pakistan province data
df = pd.read_csv("data/raw/pakistan_provinces.csv")

# Display the complete dataset
print("\nPAKISTAN PROVINCE DATA")
print(df)

# Show basic information
print("\nDATASET INFORMATION")
print(df.info())

# Calculate total population
total_population = df["population_millions"].sum()

print("\nTOTAL POPULATION (MILLIONS)")
print(total_population)

# Find the province with the highest population
largest = df.loc[df["population_millions"].idxmax()]

print("\nHIGHEST POPULATION")
print(largest["province"])