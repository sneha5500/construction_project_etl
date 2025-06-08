import streamlit as st
import pandas as pd
import sqlite3

st.header("📦 Remaining Material Inventory")

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

st.dataframe(df)

conn.close()
