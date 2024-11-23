import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the 'ras' file with the specified feature
file_content = "8. Editing Software Compatibility: 'ras' files are compatible with various image editing software applications."

with open('./tmp/file1.ras', 'w') as file:
    file.write(file_content)

with open('./tmp/file2.ras', 'w') as file:
    file.write(file_content)

print("Files generated successfully.")