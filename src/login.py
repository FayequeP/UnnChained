import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load the configuration file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)



# Create a login form
with st.form("login_form"):
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")

name, authentication_status, username = authenticator.login()

# Authenticate the user
if submit_button:
    if authentication_status:
        st.write(f"Welcome *{name}*")
        st.session_state["name"] = name
        st.session_state["username"] = username
        st.session_state["authentication_status"] = True
    elif authentication_status is False:
        st.error("Username/password is incorrect")
    elif authentication_status is None:
        st.warning("Please enter your username and password")