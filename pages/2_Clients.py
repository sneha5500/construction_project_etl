import streamlit as st
import sqlite3
import pandas as pd

st.title("👥 Client Details")

conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT * FROM Customers", conn)
conn.close()

st.dataframe(df)
