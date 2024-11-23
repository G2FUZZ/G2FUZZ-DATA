import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ras' file with encryption and metadata
encrypted_data = b'ENCRYPTED_DATA'
metadata = {'author': 'John Doe', 'creation_date': '2022-12-01'}

# Save the encrypted data and metadata to a 'ras' file
with open('./tmp/complex_sample.ras', 'wb') as file:
    file.write(encrypted_data)
    file.write(str(metadata).encode())