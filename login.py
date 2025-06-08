import streamlit as st
from credentials import users
import streamlit_extras.switch_page_button as spb

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Construction Business Login")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("✅ Login successful")
            st.switch_page("dashboard.py")
        else:
            st.error("❌ Invalid credentials")
