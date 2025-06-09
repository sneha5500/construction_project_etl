import streamlit as st
import pandas as pd
import sqlite3

st.header("🗓️ Worker Monthly Attendance")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Attendance.")
    st.stop()

conn = sqlite3.connect("company.db")

df = pd.read_sql_query('''
    SELECT 
        wh.month,
        w.worker_name,
        w.job_role,
        wh.total_days_worked,
        wh.total_hours_worked
    FROM WorkHours wh
    JOIN Workers w ON w.worker_id = wh.worker_id
    ORDER BY wh.month, w.worker_name
''', conn)
conn.close()

st.dataframe(df)


