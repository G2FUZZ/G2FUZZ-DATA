import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0 (always 0 for the first tag in the file)
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag for metadata (e.g., duration, width, height)
    # Simplified example of a script tag containing onMetaData event with video width and height
    script_tag_header = b'\x12'  # Script data tag type
    script_data_length = b'\x00\x00\x1A'  # Example length, adjust according to actual script data length
    timestamp = b'\x00\x00\x00'  # Timestamp (3 bytes) + TimestampExtended (1 byte)
    timestamp_extended = b'\x00'
    stream_id = b'\x00\x00\x00'  # Always 0 for FLV
    
    # Example script data: onMetaData with width and height
    script_data = b'onMetaData' + b'\x00\x00\x00\x02' + b'width' + b'\x00\x00\x00\x80' + b'height' + b'\x00\x00\x00\x60'
    
    # Initialize script_tag correctly
    script_tag = script_tag_header + script_data_length + timestamp + timestamp_extended + stream_id + script_data
    script_tag_size = len(script_tag) + 4  # Correct calculation of script_tag_size
    script_tag += struct.pack('>I', script_tag_size)  # PreviousTagSizeN for the next tag
    
    # Video tag for a single frame (simplified example)
    video_tag_header = b'\x09'  # Video tag
    video_data_length = b'\x00\x00\x0A'  # Example length, adjust according to actual video data length
    video_data = b'\x00\x00\x00\x00' + b'\x17' + b'\x01' + b'\x00\x00\x00' + b'\x00\x00\x00\x01'  # Simplified video frame data
    
    video_tag = video_tag_header + video_data_length + timestamp + timestamp_extended + stream_id + video_data
    video_tag_size = len(video_tag) + 4  # Correct calculation of video_tag_size
    video_tag += struct.pack('>I', video_tag_size)  # PreviousTagSizeN for subsequent tags or end of file
    
    # FLV file content
    flv_content = flv_header + previous_tag_size_0 + script_tag + video_tag
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')