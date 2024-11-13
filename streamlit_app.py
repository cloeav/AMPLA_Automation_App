import streamlit as st
import subprocess

# Streamlit button to run the script
if st.button('Run Another Script'):
    # Use subprocess to run the other script
    result = subprocess.run(['python', 'AMPLA_automation_git.py'], capture_output=True, text=True)
    
    # Display the output of the script in the Streamlit app
    st.write(result.stdout)
    st.write(result.stderr)
