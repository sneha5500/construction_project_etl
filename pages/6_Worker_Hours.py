import streamlit as st
import sqlite3
import pandas as pd

st.title("👷 Worker Hours & Salary Report")

# Connect to DB
conn = sqlite3.connect("company.db")

# Run SQL JOIN to combine Workers and WorkHours
query = '''
SELECT 
    w.worker_id, 
    w.worker_name, 
    w.job_role, 
    w.salary_per_day, 
    wh.month, 
    wh.total_days_worked, 
    wh.total_hours_worked,
    (w.salary_per_day * wh.total_days_worked) AS total_salary
FROM Workers w
JOIN WorkHours wh ON w.worker_id = wh.worker_id
ORDER BY wh.month, w.worker_id
'''

df = pd.read_sql(query, conn)
conn.close()

# Display
st.dataframe(df)

# Optional: Monthly summary
st.subheader("📊 Monthly Total Salaries")
summary = df.groupby("month")["total_salary"].sum().reset_index()
st.bar_chart(summary.set_index("month"))

