import streamlit as st
import pandas as pd
import sqlite3

st.header("📦 Remaining Material Inventory")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Inventory.")
    st.stop()

conn = sqlite3.connect("company.db")

df = pd.read_sql_query('''
    SELECT 
        site_id,
        material_name,
        SUM(material_qty) AS total,
        SUM(used_qty) AS used,
        (SUM(material_qty) - SUM(used_qty)) AS left
    FROM Materials
    GROUP BY site_id, material_name
''', conn)
conn.close()

st.dataframe(df)


