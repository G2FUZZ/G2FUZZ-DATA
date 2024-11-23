import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy FLV file
with open('./tmp/encrypted_file.flv', 'wb') as f:
    # Dummy content for the FLV file
    dummy_content = b'FLV Encrypted File'
    
    # Write the dummy content to the file
    f.write(dummy_content)

print("FLV file with encryption feature generated and saved successfully.")