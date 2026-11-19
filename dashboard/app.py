from pathlib import Path
import streamlit as st
import pandas as pd

st.title("Pakistan Cities Population")
# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Define CSV path
DATA_PATH = BASE_DIR / "data" / "processed" / "pakistan_cities_clean.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)
st.subheader("Cleaned City Population Data")
st.dataframe(df)  # Displays table in app

# Create a simple bar chart of population_2017 by city
st.subheader("Top Cities by Population (2017)")
chart_data = df.set_index('city')['population_2017']
st.bar_chart(chart_data)  # Displays bar chart
