import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Construction Project Dashboard", layout="wide")
st.title("🏗️ Construction ETL Project Dashboard")

conn = sqlite3.connect("company.db")

tab1, tab2, tab3 = st.tabs(["🧱 Materials", "👷 Workers Salary", "🔁 Ownership"])

with tab1:
    st.header("Materials Used Per Site")
    materials = pd.read_sql_query('''
        SELECT site_id, material_name, SUM(quantity_needed) AS total_quantity
        FROM Materials
        GROUP BY site_id, material_name
    ''', conn)
    st.dataframe(materials)

with tab2:
    st.header("Total Salary Paid Per Site")
    salaries = pd.read_sql_query('''
        SELECT site_id, SUM(salary) AS total_salary
        FROM Workers
        GROUP BY site_id
    ''', conn)
    st.dataframe(salaries)

with tab3:
    st.header("Site Ownership Info")
    ownership = pd.read_sql_query('''
        SELECT s.site_id, s.location, c.customer_name, o.transfer_date, o.price_paid
        FROM Sites s
        JOIN OwnershipTransfers o ON s.site_id = o.site_id
        JOIN Customers c ON o.customer_id = c.customer_id
    ''', conn)
    st.dataframe(ownership)

conn.close()

