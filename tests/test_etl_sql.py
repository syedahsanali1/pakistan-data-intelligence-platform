import sqlite3
import unittest

class TestCityData(unittest.TestCase):
    def setUp(self):
        # Open the database connection
        self.conn = sqlite3.connect("data/pakistan_data.db")
        self.cursor = self.conn.cursor()
    def tearDown(self):
        # Clean up
        self.cursor.close()
        self.conn.close()

    def test_table_exists(self):
        # Check that 'cities' table exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cities'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "The 'cities' table should exist in the database")

    def test_row_count(self):
        # Check that there is at least one row
        self.cursor.execute("SELECT COUNT(*) FROM cities")
        count = self.cursor.fetchone()[0]
        self.assertGreater(count, 0, "The cities table should have at least 1 row")

    def test_known_city(self):
        # Optionally, check that a known city (e.g. Karachi) appears
        self.cursor.execute("SELECT city FROM cities WHERE city = 'Karachi'")
        karachi = self.cursor.fetchone()
        self.assertIsNotNone(karachi, "Karachi should be present in the data")

if __name__ == "__main__":
    unittest.main()
