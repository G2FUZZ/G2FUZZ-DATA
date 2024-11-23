import os

# Create a directory to store the pgx files
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the pgx file
pgx_content = """
Format: The 'pgx' file format is a proprietary file format used by the software program PGX (Progressive Graphics File).
"""

# Save the content to a pgx file
with open('./tmp/sample.pgx', 'w') as file:
    file.write(pgx_content)