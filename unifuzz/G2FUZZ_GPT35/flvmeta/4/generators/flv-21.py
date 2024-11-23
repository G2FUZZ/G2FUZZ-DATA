import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with streaming support and custom metadata feature
with open('./tmp/streaming_custom_metadata.flv', 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # FLV body with streaming support feature
    f.write(b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
    # Custom metadata feature
    custom_metadata = b'\x08\x00\x00\x00\x15Custom Metadata Field: Value'
    f.write(custom_metadata)
    
print("FLV file with streaming support and custom metadata feature generated successfully.")