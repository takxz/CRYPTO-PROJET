# import modules
import streamlit as st
import requests

# Title
st.title("Running Python from the Browser")

# Taking user input
user_input = st.text_input("Enter a site URL to scrape (include https://)")

# your script
if user_input:
    try:
        # Add 'https://' if the user forgot
        if not user_input.startswith(('http://', 'https://')):
            user_input = 'https://' + user_input
        
        r = requests.get(user_input, timeout=10)
        
        st.success(f"Status Code: {r.status_code}")
        
        if r.status_code == 200:
            st.subheader("Page Content (First 500 characters):")
            st.code(r.text[:500])  # Display the first 500 characters
        else:
            st.warning("The site responded, but not with a 200 OK.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
