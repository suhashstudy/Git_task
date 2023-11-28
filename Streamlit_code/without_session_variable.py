import streamlit as st
import mysql.connector
from without_session_variable_1 import calling_function

placeholder = st.empty()

st.cache_resource()
def authenticate_user(username, password):
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'employees',
    }

    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()

    query = "SELECT * FROM login_users WHERE user_name = %s"
    cursor.execute(query, (username,))

    # Fetch the first result (if any)
    user_data = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    if user_data and user_data[1] == username and user_data[2] == password:
        return True
    else:
        return False

st.cache_resource()
def login():
    with placeholder.form("login"):
        st.title("Login Page")
        st.markdown("#### Enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        # Check if the username and password are correct (for demonstration purposes)
        if authenticate_user(username, password):
            st.success("Logged in as {}".format(username))
            placeholder.empty()
            return True
        else:
            st.error("Invalid username or password")


if __name__ == "__main__":
    if login():
        calling_function()