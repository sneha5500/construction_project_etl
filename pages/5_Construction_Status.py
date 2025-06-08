import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Construction Progress")

conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT site_id, status FROM Sites", conn)
conn.close()

# Simple chart
progress_chart = df['status'].value_counts().reset_index()
progress_chart.columns = ['Status', 'Count']

st.bar_chart(data=progress_chart, x="Status", y="Count")
