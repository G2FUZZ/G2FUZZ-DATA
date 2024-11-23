import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the 'pgx' files with extended complex structures
content_template = """ 
# Header Section
Title: {title}
Author: {author}
Date: {date}

# Introduction Section
Introduction:
{introduction_content}

# Body Section
{body_content}

# Conclusion Section
Conclusion:
{conclusion_content}

# Footer Section
Version: {version}
Tags: {tags}
"""

# Custom metadata for each file
file_metadata = [
    {"title": "Complex File 1", "author": "John Doe", "date": "2022-12-31", 
     "introduction_content": "This is the introduction of Complex File 1.", 
     "body_content": "This is the body content of Complex File 1.", 
     "conclusion_content": "This is the conclusion of Complex File 1.", 
     "version": "1.0", "tags": "complex, example"},
    
    {"title": "Complex File 2", "author": "Jane Smith", "date": "2022-12-31", 
     "introduction_content": "This is the introduction of Complex File 2.", 
     "body_content": "This is the body content of Complex File 2.", 
     "conclusion_content": "This is the conclusion of Complex File 2.", 
     "version": "1.0", "tags": "advanced, sample"},
    
    {"title": "Complex File 3", "author": "Alice Johnson", "date": "2022-12-31", 
     "introduction_content": "This is the introduction of Complex File 3.", 
     "body_content": "This is the body content of Complex File 3.", 
     "conclusion_content": "This is the conclusion of Complex File 3.", 
     "version": "1.0", "tags": "detailed, example"}
]

# Generate 'pgx' files with extended complex structures
for i, metadata in enumerate(file_metadata, start=1):  # Generate files based on metadata
    file_name = f'./tmp/extended_complex_file_{i}.pgx'
    
    content = content_template.format(**metadata)
    
    with open(file_name, 'w') as file:
        file.write(content)

print("Generated 'pgx' files with extended complex structures successfully.")