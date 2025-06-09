import streamlit as st
import sqlite3
import pandas as pd

st.title("👷 Worker Info")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Worker Info.")
    st.stop()

conn = sqlite3.connect("company.db")
df = pd.read_sql_query('''
    SELECT worker_id, worker_name, site_id, job_role AS role, salary_per_day
    FROM Workers
''', conn)
conn.close()

st.dataframe(df)



