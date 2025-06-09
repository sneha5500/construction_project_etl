import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Worker Hours & Salary", layout="wide")
st.title("🕒 Worker Hours & Salary Report")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access this page.")
    st.stop()

conn = sqlite3.connect("company.db")

query = '''
    SELECT w.worker_id, w.worker_name, w.job_role, w.salary_per_day,
           wh.month, wh.total_days_worked, wh.total_hours_worked,
           (w.salary_per_day * wh.total_days_worked) AS total_salary
    FROM Workers w
    JOIN WorkHours wh ON w.worker_id = wh.worker_id
    ORDER BY wh.month, w.worker_id
'''

df = pd.read_sql(query, conn)
conn.close()

st.dataframe(df)



