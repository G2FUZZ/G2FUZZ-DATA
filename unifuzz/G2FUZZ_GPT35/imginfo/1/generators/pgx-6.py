import os
import json
from datetime import datetime

# Create a dictionary with metadata information
metadata = {
    "author": "John Doe",
    "creation_date": str(datetime.now()),
    "description": "This is a sample 'pgx' file with metadata."
}

# Create a 'pgx' file with metadata
file_name = 'sample.pgx'
file_path = f'./tmp/{file_name}'

with open(file_path, 'w') as file:
    json.dump(metadata, file)

print(f"'{file_name}' containing metadata has been generated and saved in './tmp/'.")