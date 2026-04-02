import os

FILE_NAME = "shared_code.txt"

# Create file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("# Start coding here...\n")

# Read code from file
def read_code():
    with open(FILE_NAME, "r") as f:
        return f.read()

# Write code to file
def write_code(new_code):
    with open(FILE_NAME, "w") as f:
        f.write(new_code)

# Basic conflict handling (simple version)
def is_code_changed(old_code, new_code):
    return old_code != new_code