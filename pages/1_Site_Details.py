import streamlit as st
import sqlite3
import pandas as pd

st.title("📍 Site Details")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Site Details.")
    st.stop()

conn = sqlite3.connect("company.db")
df = pd.read_sql("""
    SELECT site_id,
           location AS city,
           area_name,
           site_size_sqft AS area_sqft,
           cost_per_sqft,
           status
    FROM Sites
""", conn)
conn.close()

st.dataframe(df)


