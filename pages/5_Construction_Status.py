import streamlit as st
import sqlite3
import pandas as pd

st.title("🚧 Update Construction Status")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Please login to access Construction Status.")
    st.stop()

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

df = pd.read_sql("SELECT site_id, location, area_name, status FROM Sites", conn)
st.dataframe(df)

selected_site = st.selectbox("🏗️ Select Site to Update", df["site_id"])
new_status = st.selectbox("🔄 New Status", ["Not Started", "In Progress", "Completed", "On Hold"])

if st.button("✅ Update Status"):
    cursor.execute("UPDATE Sites SET status = ? WHERE site_id = ?", (new_status, selected_site))
    conn.commit()
    st.success(f"Updated site {selected_site} to status: {new_status}")
    st.rerun()

conn.close()



