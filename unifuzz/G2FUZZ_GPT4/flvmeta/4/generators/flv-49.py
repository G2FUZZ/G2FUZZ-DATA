import os
import struct
import time

def create_complex_flv_file(file_path, video_duration=5, width=640, height=480):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # onMetaData - Script Data Tag for video details (duration, width, height)
    # This is a simplified version and not fully conforming to AMF0/AMF3 format
    script_data_tag_header = b'\x12'  # Tag type for script data
    # Placeholder for DataSize (will update later)
    script_data_size = b'\x00\x00\x00'
    # Timestamp (UI24) and TimestampExtended (UI8)
    script_data_timestamp = b'\x00\x00\x00\x00'
    # StreamID (Always 0)
    script_data_stream_id = b'\x00\x00\x00'
    
    # Generating onMetaData event content (very simplified)
    on_meta_data_content = b'onMetaData' + struct.pack('>H', len('onMetaData')) + b'\x00\x02\x00\x0A' + \
                           b'duration' + struct.pack('>d', video_duration) + \
                           b'width' + struct.pack('>d', width) + \
                           b'height' + struct.pack('>d', height)
    
    # Update script data size
    script_data_size = struct.pack('>I', len(on_meta_data_content))[1:]
    script_data_tag = script_data_tag_header + script_data_size + script_data_timestamp + script_data_stream_id + on_meta_data_content
    
    # PreviousTagSize1
    previous_tag_size_1 = struct.pack('>I', len(script_data_tag))
    
    # Simple Video Tag (H.264 key frame)
    video_tag_header = b'\x09'  # Tag type for video
    video_data_size = b'\x00\x00\x0A'  # Placeholder for video data size (10 bytes for simplicity)
    video_timestamp = b'\x00\x00\x1E\x00'  # 30 in decimal, timestamp
    video_stream_id = b'\x00\x00\x00'  # StreamID always 0
    video_data_payload = b'\x17\x01\x00\x00\x00' + b'\x00\x00\x00\x05'  # Simplified H.264 key frame data
    
    video_tag = video_tag_header + video_data_size + video_timestamp + video_stream_id + video_data_payload
    
    # PreviousTagSize2
    previous_tag_size_2 = struct.pack('>I', len(video_tag))
    
    # Combine all parts
    flv_content = flv_header + previous_tag_size_0 + script_data_tag + previous_tag_size_1 + video_tag + previous_tag_size_2
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
complex_flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(complex_flv_file_path, video_duration=10, width=1920, height=1080)

print(f'Complex FLV file created at: {complex_flv_file_path}')