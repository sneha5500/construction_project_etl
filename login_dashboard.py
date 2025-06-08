import streamlit as st
import pandas as pd
import sqlite3
from credentials import users

# --- LOGIN LOGIC ---
st.title("Construction Business Dashboard")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username", placeholder="Enter username")
    password = st.text_input("Password", type="password", placeholder="Enter password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful ✅")
        else:
            st.error("Invalid username or password ❌")

# --- AFTER LOGIN ---
if st.session_state.logged_in:
    st.header("Welcome, Business Owner 👷‍♂️")

    conn = sqlite3.connect("company.db")
    df = pd.read_sql("SELECT site_id, location AS city, area_name, area_sqft, cost_per_sqft, status FROM Sites", conn)

    st.subheader("All Site Status")

    # Filters
    city_filter = st.selectbox("Filter by City", ["All"] + sorted(df["city"].dropna().unique()))
    area_filter = st.selectbox("Filter by Area Name", ["All"] + sorted(df["area_name"].dropna().unique()))

    if city_filter != "All":
        df = df[df["city"] == city_filter]
    if area_filter != "All":
        df = df[df["area_name"] == area_filter]

    st.dataframe(df)
    conn.close()
