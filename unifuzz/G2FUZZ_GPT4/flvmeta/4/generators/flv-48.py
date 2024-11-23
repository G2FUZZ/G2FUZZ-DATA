import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script Tag (MetaData) - OnMetaData
    # For simplicity, we're going to create a very basic onMetaData with placeholder values
    # Normally, this would include details like duration, width, height, etc.
    script_data = create_script_data_tag()
    
    # Video Tag - keyframe (Simplified representation)
    video_data = create_video_tag()
    
    # Audio Tag (Simplified representation)
    audio_data = create_audio_tag()
    
    flv_content = (
        flv_header +
        previous_tag_size_0 +
        script_data +
        video_data +
        audio_data
    )
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to the file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

def create_script_data_tag():
    # Placeholder for script data tag content
    # This is highly simplified and not following the AMF0/AMF3 format exactly
    script_data_content = b'\x02\x00\x0AonMetaData\x08\x00\x00\x00\x00'
    # Tag type for script data
    tag_type = b'\x12'
    # Data size
    data_size = struct.pack('>I', len(script_data_content))[1:]
    # Timestamp and StreamID (3 bytes timestamp, 1 byte timestamp extension, and 3 bytes streamID)
    timestamp = b'\x00\x00\x00\x00\x00\x00\x00'
    # Forming the tag
    script_data_tag = tag_type + data_size + timestamp + script_data_content
    # Previous tag size (tag size + 11 bytes header)
    previous_tag_size = struct.pack('>I', len(script_data_tag))
    
    return script_data_tag + previous_tag_size

def create_video_tag():
    # Placeholder for video frame data (e.g., a keyframe)
    video_data_content = b'\x00' * 10  # Simplified placeholder data
    # Tag type for video
    tag_type = b'\x09'
    # Data size
    data_size = struct.pack('>I', len(video_data_content))[1:]
    # Timestamp and StreamID
    timestamp = b'\x00\x00\x00\x00\x00\x00\x00'
    # Forming the tag
    video_tag = tag_type + data_size + timestamp + video_data_content
    # Previous tag size
    previous_tag_size = struct.pack('>I', len(video_tag))
    
    return video_tag + previous_tag_size

def create_audio_tag():
    # Placeholder for audio frame data
    audio_data_content = b'\x00' * 5  # Simplified placeholder data
    # Tag type for audio
    tag_type = b'\x08'
    # Data size
    data_size = struct.pack('>I', len(audio_data_content))[1:]
    # Timestamp and StreamID
    timestamp = b'\x00\x00\x00\x00\x00\x00\x00'
    # Forming the tag
    audio_tag = tag_type + data_size + timestamp + audio_data_content
    # Previous tag size
    previous_tag_size = struct.pack('>I', len(audio_tag))
    
    return audio_tag + previous_tag_size

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')