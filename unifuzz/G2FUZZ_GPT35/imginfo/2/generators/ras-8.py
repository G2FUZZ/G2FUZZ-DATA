import os

# Create the directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the 'ras' file
content = """
8. Platform Compatibility: Originally designed for Sun systems but can be viewed on other platforms with appropriate software.
"""

# Write the content to the 'ras' file
with open('./tmp/file.ras', 'w') as file:
    file.write(content)