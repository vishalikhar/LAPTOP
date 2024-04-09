import webbrowser
import streamlit as st
import pandas as pd

url = "https://bhendi.streamlit.app/"
df = pd.read_csv("user_credentials.csv") 
# Function to authenticate users
def authenticate(username, password): # Load user credentials from CSV file
    if (df['Username'] == username).any() and (df['Password'] == password).any():
        return True
    else:
        return False

def main():
    st.title("Login and Registration")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Login", "Register"])

    if page == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.success("Login successful!")
                st.write("Redirecting to Predicktor...")
                # Launch
                st.markdown("[Redirect to https://bhendi.streamlit.app/](https://bhendi.streamlit.app/)")

            else:
                st.error("Invalid username or password")

    elif page == "Register":
        st.subheader("Register")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")

        if st.button("Register"):
            df = pd.read_csv("user_credentials.csv")  # Load user credentials
            if (df['Username'] == new_username).any():
                st.error("Username already exists")
            else:
                new_user = pd.DataFrame({"Username": [new_username], "Password": [new_password]})
                df = pd.concat([df, new_user], ignore_index=True)

                df.to_csv("user_credentials.csv", index=False)
                st.success("Registration successful! You can now login.")

if __name__ == "__main__":
    main()
