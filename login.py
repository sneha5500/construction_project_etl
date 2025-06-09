import streamlit as st
from credentials import users

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Construction Business Login")

# Logout handler
if st.session_state.get("authenticated"):
    st.success("✅ Already logged in!")
    if st.button("Go to Dashboard"):
        st.switch_page("dashboard.py")
    st.sidebar.button("🚪 Logout", on_click=lambda: st.session_state.update({"authenticated": False}))
    st.stop()

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username] == password:
        st.session_state["authenticated"] = True
        st.success("✅ Login successful!")
        st.switch_page("dashboard.py")
    else:
        st.error("❌ Invalid credentials")


