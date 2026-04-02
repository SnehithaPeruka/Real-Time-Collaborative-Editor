import os
from datetime import datetime

FILE_NAME = "shared_code.txt"
HISTORY_FILE = "code_history.txt"

# Initialize main file
def initialize_storage():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("# Start coding here...\n")

# Read current code
def get_code():
    try:
        with open(FILE_NAME, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

# Save code
def save_code(new_code):
    with open(FILE_NAME, "w") as f:
        f.write(new_code)

# Save history (for version tracking)
def save_history(code):
    with open(HISTORY_FILE, "a") as f:
        f.write("\n\n--- Saved at {} ---\n".format(datetime.now()))
        f.write(code)

# Get history logs
def get_history():
    if not os.path.exists(HISTORY_FILE):
        return "No history available."
    
    with open(HISTORY_FILE, "r") as f:
        return f.read()

# Clear code (optional feature)
def clear_code():
    with open(FILE_NAME, "w") as f:
        f.write("")

# Check if code changed
def has_changed(old_code, new_code):
    return old_code.strip() != new_code.strip()