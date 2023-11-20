
import streamlit as st
from Git_module_1 import calling_function

def main():
    st.title("Your Streamlit App")

    
    output = calling_function()

if __name__ == "__main__":
    main()

    