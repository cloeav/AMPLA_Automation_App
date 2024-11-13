import streamlit as st
import subprocess

import subprocess
import sys

# List of packages you need to install
required_packages = [
    'selenium',
    'pandas',
    'pdfplumber',
    'openpyxl',
    'openai',
    'docx',
]

def install_packages():
    for package in required_packages:
        try:
            # Use subprocess to run the pip install command
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")

install_packages()

# Streamlit button to run the script
if st.button('Run Another Script'):
    # Use subprocess to run the other script
    result = subprocess.run(['python', 'AMPLA_automation_git.py'], capture_output=True, text=True)
    
    # Display the output of the script in the Streamlit app
    st.write(result.stdout)
    st.write(result.stderr)
