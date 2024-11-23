import os
import struct
import time

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Path to the generated FLV file
flv_file_path = './tmp/complex_structure.flv'

# FLV header structure:
# Signature: "FLV" (3 bytes)
# Version: 1 (1 byte)
# Flags: 5 (Audio + Video tags present) (1 byte)
# Header Length: 9 (4 bytes)
flv_header = b'FLV\x01\x05\x00\x00\x00\x09'

# First PreviousTagSize0: 0 (4 bytes, UI32)
previous_tag_size0 = b'\x00\x00\x00\x00'

def create_metadata_tag():
    """
    Creates a metadata tag for FLV file.
    For simplicity, this does not include extensive metadata.
    """
    # Construct a simple onMetaData object with duration and filesize (minimal example)
    script_data = b'{"duration":0.0,"filesize":0.0}'  # Simplified example
    data_length = len(script_data)
    # Tag type (18 for script data) + Data size + Timestamp + StreamID
    tag_header = struct.pack('>B3B3B3B', 18, (data_length >> 16) & 0xFF, (data_length >> 8) & 0xFF, data_length & 0xFF, 0, 0, 0, 0, 0, 0) 
    # Form the tag
    tag = tag_header + script_data
    return tag

def create_video_tag():
    """
    Creates a dummy video tag for FLV file.
    This tag does not contain actual video data.
    """
    video_data = b'\x00\x00\x00\x00'  # Placeholder for video data
    data_length = len(video_data)
    # Tag type (9 for video) + Data size + Timestamp + StreamID
    tag_header = struct.pack('>B3B3B3B', 9, (data_length >> 16) & 0xFF, (data_length >> 8) & 0xFF, data_length & 0xFF, 0, 0, 0, 0, 0, 0)
    # Form the tag
    tag = tag_header + video_data
    return tag

def create_audio_tag():
    """
    Creates a dummy audio tag for FLV file.
    This tag does not contain actual audio data.
    """
    audio_data = b'\x00\x00\x00\x00'  # Placeholder for audio data
    data_length = len(audio_data)
    # Tag type (8 for audio) + Data size + Timestamp + StreamID
    tag_header = struct.pack('>B3B3B3B', 8, (data_length >> 16) & 0xFF, (data_length >> 8) & 0xFF, data_length & 0xFF, 0, 0, 0, 0, 0, 0)
    # Form the tag
    tag = tag_header + audio_data
    return tag

with open(flv_file_path, 'wb') as flv_file:
    flv_file.write(flv_header)
    flv_file.write(previous_tag_size0)
    
    # Write a metadata tag
    metadata_tag = create_metadata_tag()
    flv_file.write(metadata_tag)
    # Write the PreviousTagSize after metadata tag
    flv_file.write(struct.pack('>I', len(metadata_tag)))
    
    # Write a video tag
    video_tag = create_video_tag()
    flv_file.write(video_tag)
    # Write the PreviousTagSize after video tag
    flv_file.write(struct.pack('>I', len(video_tag)))
    
    # Write an audio tag
    audio_tag = create_audio_tag()
    flv_file.write(audio_tag)
    # Write the PreviousTagSize after audio tag
    flv_file.write(struct.pack('>I', len(audio_tag)))
    
print(f'FLV file with complex structure created at {flv_file_path}')