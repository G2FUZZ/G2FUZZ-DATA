import os
import struct
import random
import json

def create_complex_encrypted_flv_file(file_path, num_video_frames=5, num_audio_frames=10):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Metadata Tag for onMetaData
    on_metadata = construct_on_metadata()
    metadata_tag = construct_tag(18, on_metadata, 0)
    
    # Dynamic Metadata Tags for Encryption/DRM
    drm_metadata = b'ENCRYPTED\x00'
    drm_tag = construct_tag(18, drm_metadata, 0)
    
    # Custom Metadata Tag (e.g., Video Dimensions)
    video_metadata = b'DIMENSIONS\x01\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00'  # 1024x1024 in AMF0 format
    video_dimensions_tag = construct_tag(18, video_metadata, 0)
    
    # Generate multiple video and audio tags with varying timestamps and data
    video_tags = [
        construct_tag(
            9,  # TagType 9 for video
            b'\x00' + b'\x00\x00\x00' + random_bytes(random.randint(250, 500)),  # Simplified video frame with variable size
            i * 1000  # Incrementing timestamp for each frame
        ) for i in range(1, num_video_frames + 1)
    ]
    
    audio_tags = [
        construct_tag(
            8,  # TagType 8 for audio
            b'\xAF' + b'\x01' + random_bytes(random.randint(100, 200)),  # AAC audio sequence header with variable size
            i * 500  # Incrementing timestamp for each frame, more frequent than video
        ) for i in range(1, num_audio_frames + 1)
    ]
    
    # Combine all elements
    flv_content = flv_header + previous_tag_size_0 + metadata_tag + drm_tag + video_dimensions_tag + b''.join(video_tags + audio_tags)

    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

def construct_tag(tag_type, data, timestamp):
    """
    Constructs a FLV tag.
    
    :param tag_type: Integer, type of the tag (e.g., 18 for script data, 9 for video, 8 for audio)
    :param data: Bytes, the data of the tag
    :param timestamp: Integer, the timestamp of the tag
    :return: Bytes, the constructed tag
    """
    data_size = len(data)
    timestamp_extended = timestamp >> 24
    timestamp &= 0xFFFFFF
    stream_id = 0  # Always 0
    
    # Correct the struct.pack format string and arguments
    tag_header = struct.pack('>BIII', tag_type, data_size, timestamp, stream_id)
    tag_header = tag_header[:1] + tag_header[2:4] + tag_header[5:8] + bytes([timestamp_extended]) + tag_header[8:]
    previous_tag_size = struct.pack('>I', len(data) + 11)  # Tag header is 11 bytes
    return tag_header + data + previous_tag_size

def random_bytes(size):
    """
    Generates a sequence of random bytes.
    
    :param size: Integer, the number of bytes to generate
    :return: Bytes, the sequence of random bytes
    """
    return bytes(random.getrandbits(8) for _ in range(size))

def construct_on_metadata():
    """
    Constructs a onMetaData tag in AMF0 format with some common metadata fields.
    
    :return: Bytes, the onMetaData tag data
    """
    metadata = {
        "duration": 0,
        "width": 1024,
        "height": 1024,
        "videocodecid": 7,  # AVC
        "audiocodecid": 10,  # AAC
    }
    on_metadata_str = "onMetaData" + json.dumps(metadata)  # Simplified, real encoding should be in AMF0
    return on_metadata_str.encode()

# Example usage
flv_file_path = './tmp/complex_encrypted_example.flv'
create_complex_encrypted_flv_file(flv_file_path, num_video_frames=5, num_audio_frames=10)

print(f'Complex Encrypted FLV file with additional tags and structures created at: {flv_file_path}')