import streamlit as st

def signup():
    st.title("Signup Page")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    confirm_password = st.text_input("Confirm Password:", type="password")

    if st.button("Signup"):
        if password == confirm_password:
            # Perform signup logic (e.g., store user credentials in a database)
            st.success("Signup successful! You can now login.")
            st.session_state.is_authenticated = True
            st.session_state.username = username
        else:
            st.error("Password and Confirm Password do not match.")

def login():
    st.title("Login Page")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        # Perform login logic (e.g., check credentials against a database)
        if username == "example_user" and password == "example_password":
            st.success("Login successful!")
            st.session_state.is_authenticated = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password.")

# Initialize session state variables
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False

# Display appropriate page based on authentication status
if st.session_state.is_authenticated:
    st.title(f"Welcome, {st.session_state.username}!")
    # Your main page content goes here
else:
    # Display either the signup or login page
    page_selection = st.radio("Select a page:", ["Signup", "Login"])

    if page_selection == "Signup":
        signup()
    elif page_selection == "Login":
        login()
