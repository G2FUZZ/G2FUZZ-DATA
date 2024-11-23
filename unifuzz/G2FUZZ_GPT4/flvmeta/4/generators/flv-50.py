import os
from struct import pack
from random import randint

def create_complex_flv_file_v2(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Metadata tag (script data tag to simulate metadata, e.g., duration, width, height, and more)
    metadata_tag_type = b'\x12'
    metadata_body = (b'\x02\x00\x0AonMetaData' +
                     b'\x08\x00\x00\x00\x05'  # Increased the number of metadata properties
                     b'\x00\x08duration\x00\x40\x81\xE0\x00\x00\x00\x00\x00' +
                     b'\x00\x05width\x00\x40\x90\x00\x00\x00\x00\x00\x00' +
                     b'\x00\x06height\x00\x40\x6E\x00\x00\x00\x00\x00\x00' +
                     b'\x00\x0CvideoCodecId\x00\x40\x1C\x00\x00\x00\x00\x00\x00' +
                     b'\x00\x0BaudioCodecId\x00\x40\x2C\x00\x00\x00\x00\x00\x00' +
                     b'\x00\x00\x09')  # ECMA array end
    metadata_data_size = pack('>I', len(metadata_body))[1:]
    metadata_timestamp = b'\x00\x00\x00'
    metadata_stream_id = b'\x00\x00\x00'
    metadata_tag = metadata_tag_type + metadata_data_size + metadata_timestamp + metadata_stream_id + metadata_body
    
    previous_tag_size_metadata = pack('>I', len(metadata_tag))
    
    # Helper function to create video tags
    def create_video_tag(timestamp, keyframe=True):
        frame_type = b'\x17' if keyframe else b'\x27'  # Key frame or inter frame
        video_body = frame_type + b'\x00\x00\x00\x00' + (b'\x00\x00\x01' * randint(5, 15))  # Dummy data
        video_data_size = pack('>I', len(video_body))[1:]
        video_timestamp = pack('>I', timestamp)[1:]
        video_stream_id = b'\x00\x00\x00'
        return b'\x09' + video_data_size + video_timestamp + video_stream_id + video_body
    
    # Helper function to create audio tags
    def create_audio_tag(timestamp):
        audio_body = b'\xAF\x01' + (b'\x00' * randint(10, 30))  # Dummy data
        audio_data_size = pack('>I', len(audio_body))[1:]
        audio_timestamp = pack('>I', timestamp)[1:]
        audio_stream_id = b'\x00\x00\x00'
        return b'\x08' + audio_data_size + audio_timestamp + audio_stream_id + audio_body
    
    # Generate multiple video and audio tags with varying timestamps and keyframes
    content = []
    timestamp = 0
    for i in range(5):  # Example with 5 video frames and audio frames
        keyframe = (i % 2 == 0)
        content.append(create_video_tag(timestamp, keyframe=keyframe))
        content.append(create_audio_tag(timestamp + 50))  # Offset audio slightly for demonstration
        timestamp += 300  # Increment timestamp to simulate time passing
    
    # Calculate and insert PreviousTagSize values
    tags_with_sizes = [previous_tag_size_0 + metadata_tag + previous_tag_size_metadata]
    for tag in content:
        tags_with_sizes.append(tag)
        tags_with_sizes.append(pack('>I', len(tag)))
    
    # Combine all parts
    flv_content = flv_header + b''.join(tags_with_sizes)
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
complex_flv_file_path_v2 = './tmp/complex_example_v2.flv'
create_complex_flv_file_v2(complex_flv_file_path_v2)

print(f'More complex FLV file created at: {complex_flv_file_path_v2}')