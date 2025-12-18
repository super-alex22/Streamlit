import streamlit as st
st.title("My first project")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")
want_to_visit_exhibition = st.text_input("Do you want to visit zoo")
if name:
    st.write(f"Hello {name}")
    if age:
        st.write(f"You are {age} years old")
        if age>17:
            st.write("You are of legal age")
        else:
            st.write("You are not old enough to vote")
        if want_to_visit_exhibition == "yes":
            if age<1:
                st.write("You were not born yet")
            elif age>=1 and age<=10:
                st.write("The ticket price for you will be 5 usdt")
            elif age>=11 and age<=18:
                st.write("The ticket price for you will be 10 usdt")
            elif age>18 and age<=64:
                st.write("The ticket price for you will be 15 usdt")
            elif age>64 and age<=75:
                st.write("The ticket price for you will be 10 usdt")
            else:
                st.write("Wow. You are still alive. The entrance is free for you!")
