import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_flv_file(filename, metadata, custom_header):
    with open(filename, 'wb') as file:
        # Write custom header
        file.write(custom_header)
        
        # Write metadata information
        metadata_length = len(metadata).to_bytes(4, byteorder='big')
        file.write(metadata_length)
        file.write(metadata.encode())
        
        # Write data
        file.write(b'FLV File - Quality: FLV files can maintain good quality while keeping file sizes relatively small.')

# Generate FLV files with additional complex features
for i in range(3):
    filename = f'./tmp/file_{i}.flv'
    metadata = f'Metadata for file {i}'
    custom_header = b'Custom FLV Header'
    generate_flv_file(filename, metadata, custom_header)

print('FLV files with complex features generated successfully.')