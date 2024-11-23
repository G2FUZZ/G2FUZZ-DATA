import os
import struct

def write_flv_file(file_path, metadata, video_data, audio_data):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    
    # FLV body with metadata, video, and audio data
    flv_body = b''
    
    # PreviousTagSize0 (reserved for first tag)
    flv_body += struct.pack('>I', 0)
    
    # FLV Tag for metadata
    tag_type_metadata = 18  # Metadata Tag
    timestamp = 0
    
    metadata_bytes = struct.pack('>I', len(metadata)) + metadata
    tag_header_metadata = struct.pack('>BBHBB', tag_type_metadata, 0, len(metadata_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
    
    flv_body += tag_header_metadata
    flv_body += metadata_bytes
    
    # FLV Tag for video data
    tag_type_video = 9  # Video Tag
    timestamp += 1000  # Example timestamp increment
    
    video_data_bytes = struct.pack('>I', len(video_data)) + video_data
    tag_header_video = struct.pack('>BBHBB', tag_type_video, 0, len(video_data_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
    
    flv_body += tag_header_video
    flv_body += video_data_bytes
    
    # FLV Tag for audio data
    tag_type_audio = 8  # Audio Tag
    timestamp += 1000  # Example timestamp increment
    
    audio_data_bytes = struct.pack('>I', len(audio_data)) + audio_data
    tag_header_audio = struct.pack('>BBHBB', tag_type_audio, 0, len(audio_data_bytes), (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF)
    
    flv_body += tag_header_audio
    flv_body += audio_data_bytes
    
    # Update PreviousTagSize0 with actual tag size
    flv_body_size = len(flv_body)
    flv_body = flv_body[:0] + struct.pack('>I', flv_body_size) + flv_body[4:]
    
    # Write FLV file
    with open(file_path, 'wb') as f:
        f.write(flv_header)
        f.write(flv_body)

# Metadata for the FLV file
metadata = b'Metadata: video duration=60s, dimensions=1920x1080, frame rate=30fps'

# Video data for the FLV file
video_data = b'\x00\x00\x00\x01'  # Example video data

# Audio data for the FLV file
audio_data = b'\x00\x00\x00\x02'  # Example audio data

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save FLV file with metadata, video, and audio data
write_flv_file('./tmp/complex_metadata_file.flv', metadata, video_data, audio_data)