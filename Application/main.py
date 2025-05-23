import streamlit as st
st.title("Cold Email Generator")
url_input = st.text_input("Enter a URL: ", value = " ")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring manager, I am Moksha", language = 'markdown')