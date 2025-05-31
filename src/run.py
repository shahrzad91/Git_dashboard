import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

login_option = st.sidebar.radio("Login / Sign up", ("Login", "Sign up"))
if login_option=="Login" :
    with st.sidebar.form("Login"):
        st.write("Login here")
        username = st.sidebar.text_input("Enter your Username")
        password = st.sidebar.text_input("Enter your Password" , type="password")
        
        submitted = st.form_submit_button("Login")
        if submitted:
            st.success("Login successful!")
else:

    with st.sidebar.form("Sign Up"):
        st.write("Sign Up here")
        username = st.sidebar.text_input("Enter your Username")
        password = st.sidebar.text_input("Enter your Password" , type="password")
        email_address = st.sidebar.text_input("email_address" , )
        
        submitted = st.form_submit_button("Sign Up")
        if submitted:
            st.success("Sign up successful!")




banner = Image.open("./banner.jpg")
st.image(banner)
st.title(" :zap: Git_Dashboard")

with st.expander("User Profile"):
    col1,col2 = st.columns(2)
    col1.text_input("Enter Your Name")
    col2.text_input("Enter Your Location")
    img_file_buffer = st.camera_input("Take a picture")
    
    if img_file_buffer is not None:
        
       
        img = Image.open(img_file_buffer)
        img_array = np.array(img)
        st.write(type(img_array))
        st.write(img_array.shape)

with st.expander("Upload json file"):
    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)



with st.expander("Plot"):
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)
    




        