import os
import struct

def write_flv_file(file_path, metadata):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    
    # FLV body with metadata
    flv_body = b''
    
    # PreviousTagSize0 (reserved for first tag)
    flv_body += struct.pack('>I', 0)
    
    # FLV Tag for metadata
    tag_type = 18  # Metadata Tag
    timestamp = 0
    stream_id = 0
    
    # Data for metadata
    metadata_bytes = struct.pack('>I', len(metadata)) + metadata
    
    tag_header = struct.pack('>BBHBB', tag_type, 0, len(metadata_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
    
    # Write tag to FLV body
    flv_body += tag_header
    flv_body += metadata_bytes
    
    # Update PreviousTagSize0 with actual tag size
    flv_body_size = len(flv_body)
    flv_body = flv_body[:0] + struct.pack('>I', flv_body_size) + flv_body[4:]
    
    # Write FLV file
    with open(file_path, 'wb') as f:
        f.write(flv_header)
        f.write(flv_body)

# Metadata for the FLV file
metadata = b'Metadata: video duration=60s, dimensions=1920x1080, frame rate=30fps'

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save FLV file with metadata
write_flv_file('./tmp/metadata_file.flv', metadata)