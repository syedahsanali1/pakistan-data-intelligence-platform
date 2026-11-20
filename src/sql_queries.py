import sqlite3

conn = sqlite3.connect("data/pakistan_data.db")
cursor = conn.cursor()

# Query 1: count cities
cursor.execute("SELECT COUNT(*) FROM cities")
count = cursor.fetchone()[0]
print("Total cities in database:", count)

# Query 2: largest city by population
cursor.execute("SELECT city, population_2017 FROM cities ORDER BY population_2017 DESC LIMIT 1")
largest = cursor.fetchone()
print(f"Largest city: {largest[0]} with population {largest[1]}")

# Query 3: group by province (sum of population)
cursor.execute("SELECT province, SUM(population_2017) FROM cities GROUP BY province")
print("\nPopulation by province:")
for province, popsum in cursor.fetchall():
    print(f"  {province}: {popsum}")

conn.close()
