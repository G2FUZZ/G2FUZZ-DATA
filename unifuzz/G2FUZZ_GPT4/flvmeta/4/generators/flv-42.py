import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV Header for a file with audio and video
    
    # PreviousTagSize0 (always 0 for the first tag in the file)
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Custom Metadata Tag (Script Data Tag)
    # For simplicity, this is just a placeholder showing how a metadata tag might be structured
    metadata_tag = create_metadata_tag({
        "author": "Example Author",
        "title": "Sample FLV Video",
        "duration": 120,  # Duration in seconds
    })
    
    # Video Tag Placeholder - Let's simulate a simple keyframe
    video_data = b'\x00\x00\x00\x00'  # Placeholder for video frame data
    video_tag = create_video_tag(video_data)
    
    # Audio Tag Placeholder - Simulate a simple audio frame
    audio_data = b'\x00\x00'  # Placeholder for audio frame data
    audio_tag = create_audio_tag(audio_data)
    
    # Combine all elements
    flv_content = flv_header + previous_tag_size_0 + metadata_tag + video_tag + audio_tag
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to the file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

def create_metadata_tag(metadata):
    """Create a custom metadata tag for the FLV file."""
    # Simulate metadata in a very basic form
    # Normally, metadata would be encoded in AMF format
    metadata_str = str(metadata)
    data_length = len(metadata_str)
    tag_type = 18  # Script data
    
    # Tag header: Type(1 byte) + Data size(3 bytes) + Timestamp(3 bytes) + Timestamp extended(1 byte) + StreamID(3 bytes)
    tag_header = struct.pack('>B', tag_type) + struct.pack('>L', data_length)[1:] + b'\x00\x00\x00' + b'\x00' + b'\x00\x00\x00'
    
    # Tag data
    tag_data = metadata_str.encode('utf-8')
    
    # Previous tag size (header + data)
    previous_tag_size = struct.pack('>L', len(tag_header) + data_length)
    
    return tag_header + tag_data + previous_tag_size

def create_video_tag(video_data):
    """Create a simple video tag."""
    data_length = len(video_data)
    tag_type = 9  # Video tag
    # Video tag header (same structure as metadata tag)
    tag_header = struct.pack('>B', tag_type) + struct.pack('>L', data_length)[1:] + b'\x00\x00\x00' + b'\x00' + b'\x00\x00\x00'
    
    # Previous tag size (header + data)
    previous_tag_size = struct.pack('>L', len(tag_header) + data_length)
    
    return tag_header + video_data + previous_tag_size

def create_audio_tag(audio_data):
    """Create a simple audio tag."""
    data_length = len(audio_data)
    tag_type = 8  # Audio tag
    # Audio tag header (same structure as metadata and video tags)
    tag_header = struct.pack('>B', tag_type) + struct.pack('>L', data_length)[1:] + b'\x00\x00\x00' + b'\x00' + b'\x00\x00\x00'
    
    # Previous tag size (header + data)
    previous_tag_size = struct.pack('>L', len(tag_header) + data_length)
    
    return tag_header + audio_data + previous_tag_size

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')