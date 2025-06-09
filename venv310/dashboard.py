import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Construction Project Dashboard", layout="wide")

# Check authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Logout handler
def logout():
    st.session_state["authenticated"] = False
    st.experimental_rerun()

# If not logged in, redirect to login
if not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access the dashboard.")
    st.stop()

# Dashboard content
st.title("🏗️ Construction ETL Project Dashboard")

# 🔘 Logout button (top-right corner)
st.sidebar.button("🚪 Logout", on_click=logout)

conn = sqlite3.connect("company.db")

tab1, tab2, tab3 = st.tabs(["🧱 Materials", "👷 Workers Salary", "🔁 Ownership"])

with tab1:
    st.header("Materials Used Per Site")
    materials = pd.read_sql_query('''
        SELECT site_id, material_name,
               SUM(material_qty) AS total_qty,
               SUM(used_qty) AS used_qty,
               SUM(material_qty - used_qty) AS quantity_left
        FROM Materials
        GROUP BY site_id, material_name
    ''', conn)
    st.dataframe(materials)

with tab2:
    st.header("Total Salary Paid Per Site")
    salaries = pd.read_sql_query('''
        SELECT site_id, SUM(salary_per_day * total_days_worked) AS total_salary
        FROM Workers
        JOIN WorkHours ON Workers.worker_id = WorkHours.worker_id
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

