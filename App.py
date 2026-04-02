import streamlit as st
import os
import time
from model import initialize_storage, get_code, save_code, save_history, has_changed
FILE_NAME = "shared_code.txt"
st.title("🧑‍💻 Real-Time Collaborative Code Editor")
# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("# Start coding here...\n")

# Load existing code
with open(FILE_NAME, "r") as f:
    code = f.read()

# Code editor (text area)
new_code = st.text_area("Edit Code:", value=code, height=300)

# Save button
if st.button("Save Changes"):
    with open(FILE_NAME, "w") as f:
        f.write(new_code)
    st.success("Code updated successfully!")
# Auto-refresh button
if st.button("Refresh"):
    st.rerun()
st.info("👉 Multiple users can edit this file. Click 'Refresh' to see updates.")
time.sleep(2)
st.rerun()