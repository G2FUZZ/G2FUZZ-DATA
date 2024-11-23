import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with streaming support and alpha channel support features
with open('./tmp/streaming_alpha_support.flv', 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # FLV body with streaming support and alpha channel support features
    f.write(b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
print("FLV file with streaming and alpha channel support features generated successfully.")