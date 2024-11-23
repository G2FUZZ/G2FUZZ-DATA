import os

# Define the content of the 'pgx' file
pgx_content = """
Format: The 'pgx' file format is a proprietary format used for storing graphical data.
"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the content to a 'pgx' file
with open('./tmp/file1.pgx', 'w') as file:
    file.write(pgx_content)