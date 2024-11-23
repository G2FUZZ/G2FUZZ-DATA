import os
import struct

def write_flv_file(file_path, metadata, video_data):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    
    # FLV body with metadata and video data
    flv_body = b''
    
    # PreviousTagSize0 (reserved for first tag)
    flv_body += struct.pack('>I', 0)
    
    # FLV Tag for metadata
    tag_type_metadata = 18  # Metadata Tag
    timestamp = 0
    stream_id = 0
    
    # Data for metadata
    metadata_bytes = struct.pack('>I', len(metadata)) + metadata
    
    tag_header_metadata = struct.pack('>BBHBB', tag_type_metadata, 0, len(metadata_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
    
    # Write metadata tag to FLV body
    flv_body += tag_header_metadata
    flv_body += metadata_bytes
    
    # Update PreviousTagSize0 with actual tag size
    flv_body_size_metadata = len(tag_header_metadata) + len(metadata_bytes)
    flv_body = flv_body[:0] + struct.pack('>I', flv_body_size_metadata) + flv_body[4:]
    
    # Add more tags with video data
    for i, frame_data in enumerate(video_data):
        tag_type_video = 9  # Video Tag
        timestamp += 40  # Increment timestamp by 40ms for each frame
        video_data_bytes = struct.pack('>I', len(frame_data)) + frame_data
        
        tag_header_video = struct.pack('>BBHBB', tag_type_video, 0, len(video_data_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
        
        # Write video tag to FLV body
        flv_body += struct.pack('>I', len(tag_header_video) + len(video_data_bytes))
        flv_body += tag_header_video
        flv_body += video_data_bytes
    
    # Write FLV file
    with open(file_path, 'wb') as f:
        f.write(flv_header)
        f.write(flv_body)

# Metadata for the FLV file
metadata = b'Metadata: video duration=60s, dimensions=1920x1080, frame rate=30fps'

# Video data for the FLV file (simulated frames)
video_frames = [b'Frame 1 data', b'Frame 2 data', b'Frame 3 data']

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save FLV file with metadata and video data
write_flv_file('./tmp/extended_metadata_file.flv', metadata, video_frames)