import os

# Generate 'pixdata' file with Versioning feature
versioning_feature = "Support for different versions of the 'pixdata' file format."
file_content = f"Feature: Versioning\nDescription: {versioning_feature}"

# Create 'tmp' directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the generated file in the 'tmp' directory
file_path = './tmp/pixdata.txt'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"'pixdata' file with Versioning feature generated and saved at: {file_path}")