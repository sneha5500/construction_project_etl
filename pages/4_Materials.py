import streamlit as st
import sqlite3
import pandas as pd

st.title("🧱 Materials by Site")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Materials.")
    st.stop()

conn = sqlite3.connect("company.db")

query = """
SELECT s.site_id, s.location, s.area_name, m.material_name, m.material_qty, m.cost
FROM Materials m
JOIN Sites s ON s.site_id = m.site_id
ORDER BY s.site_id
"""

df = pd.read_sql(query, conn)
conn.close()

if df.empty:
    st.warning("No materials data found.")
else:
    st.dataframe(df)





