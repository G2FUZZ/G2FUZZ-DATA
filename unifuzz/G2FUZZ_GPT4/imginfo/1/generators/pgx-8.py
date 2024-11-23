import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be written into the PGX file
text_content = """
Wide Application Range: Due to their high quality and flexibility, PGX files are used in a range of applications, 
from digital archiving and medical imaging to digital cinema and online image distribution. Their ability to maintain 
high image fidelity makes them suitable for professional and archival purposes.
"""

# Path to the new file
file_path = './tmp/feature_description.pgx'

# Writing the text to the file
with open(file_path, 'w') as file:
    file.write(text_content)

print(f"File saved to {file_path}")