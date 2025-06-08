import streamlit as st
import sqlite3
import pandas as pd

st.title("📍 Site Details")

conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT site_id, location AS city, area_name, area_sqft, cost_per_sqft, status FROM Sites", conn)
conn.close()

st.dataframe(df)
