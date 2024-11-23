import os

# Function to add metadata and custom script tags to the FLV file
def add_complex_features(file_path):
    # Define metadata tag
    metadata_tag = b'\x12\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Define custom script tag
    custom_script_tag = b'\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Read the existing FLV file content
    with open(file_path, 'rb') as f:
        flv_content = f.read()
    
    # Insert metadata and custom script tags into the FLV content
    updated_flv_content = flv_content[:13] + metadata_tag + custom_script_tag + flv_content[13:]
    
    # Write the updated content back to the file
    with open(file_path, 'wb') as f:
        f.write(updated_flv_content)

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy FLV file
with open('./tmp/encrypted_file_with_complex_features.flv', 'wb') as f:
    # Dummy content for the FLV file
    dummy_content = b'FLV Encrypted File'

    # Write the dummy content to the file
    f.write(dummy_content)

# Add metadata and custom script tags to the FLV file
add_complex_features('./tmp/encrypted_file_with_complex_features.flv')

print("FLV file with encryption feature, Metadata tag, and Custom script tag generated and saved successfully.")