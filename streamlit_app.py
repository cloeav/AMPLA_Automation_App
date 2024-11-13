import streamlit as st
import subprocess

# Title of the app
st.title('Streamlit Command Runner')

# Input for arguments
args = st.text_input("Enter Arguments for the Script", "[ARGUMENTS]")

# Button to trigger the command
if st.button('Run Streamlit Script'):
    try:
        # Construct the command
        command = f"streamlit run c:/Users/cloea/Desktop/streamlit_app.py {args}"
        
        # Run the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Display the output of the command
        st.text(result.stdout)
        st.text(result.stderr)

    except Exception as e:
        st.error(f"Error running the command: {e}")
