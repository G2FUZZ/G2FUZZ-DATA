import os
from datetime import datetime

# Define the directory to save the PGX file
directory = './tmp/'
os.makedirs(directory, exist_ok=True)

# Define the filename
filename = 'example.pgx'
file_path = os.path.join(directory, filename)

# PGX file content - simplicity for demonstration, not actual image data
pgx_content = """
PG ML
Width = 256
Height = 256
Depth = 8
MaxVal = 255
Creator = PythonScript
"""

# Metadata to embed (for demonstration, actual PGX does not support this natively)
metadata = f"""
Metadata:
    Creation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Author: Example Author
    Copyright: Copyright 2023 by Example Author
    Camera Settings: ISO 100, f/1.8, 1/1000s
"""

# Combine the PGX content and the metadata
combined_content = pgx_content + metadata

# Write the combined content to a file
with open(file_path, 'w') as file:
    file.write(combined_content)

print(f"PGX file with embedded metadata created at: {file_path}")