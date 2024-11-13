import streamlit as st
import subprocess

# Title of the Streamlit app
st.title("Run Python Script on Streamlit Cloud")


# Button to trigger the execution of the script
if st.button("Run Python Script"):
        subprocess.run(['python', 'AMPLA_automation_git.py'], shell=True, capture_output=True, text=True)

    
