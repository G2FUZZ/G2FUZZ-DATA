import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with streaming support feature
with open('./tmp/streaming_support.flv', 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # FLV body with streaming support feature
    f.write(b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
print("FLV file with streaming support feature generated successfully.")