import streamlit as st
import sqlite3
import pandas as pd

st.title("👷 Worker Info")

conn = sqlite3.connect("company.db")

# Using the correct columns from your table
df = pd.read_sql_query('''
    SELECT worker_id, worker_name, site_id, job_role AS role, salary_per_day
    FROM Workers
''', conn)

st.dataframe(df)
conn.close()

