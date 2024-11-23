import os
import json

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the pgx file with metadata and multiple pages
pgx_data = {
    "metadata": {
        "title": "Complex PGX File",
        "author": "John Doe",
        "created_date": "2022-09-15"
    },
    "pages": [
        {
            "page_number": 1,
            "content": "Page 1 content..."
        },
        {
            "page_number": 2,
            "content": "Page 2 content..."
        }
    ]
}

# Generate the pgx file with complex file structures
with open('./tmp/complex.pgx', 'w') as file:
    file.write(json.dumps(pgx_data, indent=4))