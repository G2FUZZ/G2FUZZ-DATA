import os

# Create a directory if it does not exist
os.makedirs('./tmp', exist_ok=True)

# Generate pgx files
compatibility_feature = "Compatibility: 'pgx' files may have specific compatibility requirements with certain software applications."

# Save the generated file
file_path = './tmp/compatibility_feature.pgx'
with open(file_path, 'w') as file:
    file.write(compatibility_feature)

print(f"File saved successfully at {file_path}")