import streamlit as st
st.title("My first project")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")
if name:
    st.write(f"Hello {name}")
    if age:
        st.write(f"You are {age} years old")
