import streamlit as st
import sqlite3
import pandas as pd

st.title("👥 Client Details")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Client Details.")
    st.stop()

conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT * FROM Customers", conn)
conn.close()

st.dataframe(df)


