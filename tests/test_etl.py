import pandas as pd

def test_load_and_clean():
    df = pd.read_csv("data/processed/pakistan_cities_clean.csv")
    # No missing values
    assert not df.isnull().values.any(), "There are missing values"
    # No duplicate ranks
    assert df['city'].is_unique, "Duplicate rank found"
    # Required columns exist
    for col in ["city","population_2017","population_1998","province"]:
        assert col in df.columns, f"Missing column {col}"
