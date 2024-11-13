import streamlit as st
import subprocess

# Title of the Streamlit app
st.title("Run Python Script on Streamlit Cloud")


# Button to trigger the execution of the script
if st.button("Run Python Script"):
    # Construct the command to run the Python script with any arguments
    command = 'AMPLA_automation_git.py'
        
    # Run the Python script using subprocess
    result = subprocess.run('python',command, shell=True, capture_output=True, text=True)
    
