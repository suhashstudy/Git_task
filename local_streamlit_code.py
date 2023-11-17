
import streamlit as st
from Git_module import calling_function

def main():
    st.title("Your Streamlit App")

    
    output = calling_function()
    st.write("Output:", output)

if __name__ == "__main__":
    main()