-- Count total cities
SELECT COUNT(*) AS num_cities FROM cities;

-- Total population by province
SELECT province, SUM(population_2017) AS total_pop 
FROM cities 
GROUP BY province 
ORDER BY total_pop DESC;

-- Top 5 cities by population
SELECT city, population_2017 
FROM cities 
ORDER BY population_2017 DESC 
LIMIT 5;
