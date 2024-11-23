import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate the pixdata file with complex file structure
metadata = {
    "author": "John Doe",
    "date_created": "2021-09-15",
    "description": "This file contains pixel data for image processing."
}

sections = {
    "section1": "Section 1 content here...",
    "section2": "Section 2 content here...",
    "section3": "Section 3 content here..."
}

with open('./tmp/complex_pixdata.txt', 'w') as f:
    f.write("# Metadata\n")
    for key, value in metadata.items():
        f.write(f"{key}: {value}\n")
    f.write("\n")

    f.write("# Sections\n")
    for section_name, section_content in sections.items():
        f.write(f"## {section_name}\n")
        f.write(f"{section_content}\n")

print("Complex pixdata file generated and saved in ./tmp/ directory.")