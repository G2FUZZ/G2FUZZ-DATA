import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the 'pgx' files with complex structures
content_template = """ 
# Header Section
Title: {title}
Author: {author}
Date: {date}

# Body Section
{body_content}

# Footer Section
Version: {version}
"""

# Generate 'pgx' files with complex structures
for i in range(1, 4):  # Generate 3 'pgx' files
    file_name = f'./tmp/complex_file_{i}.pgx'
    
    # Customize content for each file
    title = f"Complex File {i}"
    author = "John Doe"
    date = "2022-12-31"
    body_content = f"This is the body content of Complex File {i}."
    version = "1.0"
    
    content = content_template.format(title=title, author=author, date=date, body_content=body_content, version=version)
    
    with open(file_name, 'w') as file:
        file.write(content)

print("Generated 'pgx' files with complex structures successfully.")