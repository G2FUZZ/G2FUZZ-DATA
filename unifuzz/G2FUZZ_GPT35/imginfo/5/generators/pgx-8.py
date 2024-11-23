import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'pgx' file with embedded fonts
sample_pgx_content = "Embedded Fonts: 'pgx' files may embed fonts to ensure proper display of text elements."
with open('./tmp/sample.pgx', 'w') as file:
    file.write(sample_pgx_content)