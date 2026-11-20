import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# -- Page configuration -------------------------------------------------------
st.set_page_config(
    page_title="Pakistan Data Intelligence",
    page_icon="🇵🇰",
    layout="wide"
)

# -- Title / Header -----------------------------------------------------------
st.title("🇵🇰 Pakistan Data Intelligence Platform")
st.markdown("Explore Pakistan city population data with interactive charts and KPIs.")

# -- Load data (SQLite with CSV fallback) -------------------------------------
try:
    conn = sqlite3.connect("data/pakistan_data.db")
    # Read all columns from the 'cities' table:
    df = pd.read_sql_query("SELECT * FROM cities", conn)
    conn.close()
except Exception:
    # Fallback: read cleaned CSV from data/processed
    df = pd.read_csv("data/processed/pakistan_cities.csv")

# Normalize column names (lowercase, no spaces):
df.columns = df.columns.str.strip().str.lower()
if 'population 2017 census' in df.columns:
    df.rename(columns={'population 2017 census':'population_2017'}, inplace=True)
# -- Sidebar filters ----------------------------------------------------------
st.sidebar.header("Filters")
provinces = sorted(df['province'].unique())
selected_provs = st.sidebar.multiselect("Province", provinces, default=provinces)
search_text = st.sidebar.text_input("Search city (contains):")

# Apply filters to dataframe
df_filtered = df.copy()
if selected_provs:
    df_filtered = df_filtered[df_filtered['province'].isin(selected_provs)]
if search_text:
    df_filtered = df_filtered[df_filtered['city'].str.contains(search_text, case=False, na=False)]
# -- KPI Metrics --------------------------------------------------------------
city_count = len(df_filtered)
total_pop = int(df_filtered["population_2017"].sum())
prov_count = df_filtered["province"].nunique()
if city_count > 0:
    largest_city = df_filtered.loc[df_filtered["population_2017"].idxmax(), "city"]
else:
    largest_city = "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cities", city_count)
col2.metric("Total Population (2017)", total_pop)
col3.metric("Provinces Represented", prov_count)
col4.metric("Largest City", largest_city)
# -- Charts -------------------------------------------------------------------
st.subheader("Population by Province")
prov_df = df_filtered.groupby("province")["population_2017"].sum().reset_index()
fig1 = px.bar(prov_df, x="province", y="population_2017",
              title="Population by Province",
              color="province")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top 10 Cities by Population")
top_cities = df_filtered.nlargest(10, "population_2017")
fig2 = px.bar(top_cities, x="population_2017", y="city",
              orientation="h", title="Top 10 Cities (2017)",
              color="province")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Distribution of City Populations")
fig3 = px.histogram(df_filtered, x="population_2017", nbins=20,
                    title="Histogram of City Populations")
st.plotly_chart(fig3, use_container_width=True)
# -- Data table ---------------------------------------------------------------
st.subheader("Data Table")
st.dataframe(df_filtered)

# -- Data source / notes -----------------------------------------------------
st.markdown("""
**Data Source:** Pakistan Bureau of Statistics (2017 Census) – figures are illustrative.
Population values are from the 2017 census (shown in millions or as provided). Current actual populations may differ.
""")
