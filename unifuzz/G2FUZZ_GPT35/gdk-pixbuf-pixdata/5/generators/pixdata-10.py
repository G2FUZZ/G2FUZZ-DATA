import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the pixdata files with the specified features
file_structure = "File structure: How data is organized within the file, including any headers, sections, or markers."

with open('./tmp/pixdata1.txt', 'w') as file1:
    file1.write(file_structure)

with open('./tmp/pixdata2.txt', 'w') as file2:
    file2.write(file_structure)

print("pixdata files have been generated and saved in the ./tmp/ directory.")