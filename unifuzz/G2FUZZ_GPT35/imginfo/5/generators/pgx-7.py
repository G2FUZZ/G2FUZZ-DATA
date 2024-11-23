import os

# Create a directory named 'tmp' if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate 'pgx' file with versioning feature
file_content = """
Name: SampleFile
Type: pgx
Versioning: Enabled
"""

file_path = './tmp/sample_file.pgx'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Generated 'pgx' file with versioning feature: {file_path}")