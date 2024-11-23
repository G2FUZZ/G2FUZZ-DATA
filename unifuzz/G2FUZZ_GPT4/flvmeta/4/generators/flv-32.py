import os
import struct


def create_script_data_tag(tag_name, value):
    """
    Create a script data tag for FLV.
    
    Parameters:
    - tag_name: The name of the tag (e.g., "DRM", "AccessibilityFeatures")
    - value: The value associated with the tag
    
    Returns:
    A bytes object representing the tag in FLV format.
    """
    # TagType (18 for script data)
    tag_type = b'\x12'
    
    # Convert tag_name and value to their script data representations
    # String type (2) + Length of the string + Actual string bytes
    tag_name_data = struct.pack('>B', 2) + struct.pack('>H', len(tag_name)) + tag_name.encode('utf-8')
    value_data = struct.pack('>B', 2) + struct.pack('>H', len(value)) + value.encode('utf-8')
    
    # DataSize: Length of the tag_name_data + value_data
    data_size = len(tag_name_data) + len(value_data)
    data_size_bytes = struct.pack('>I', data_size)[1:]  # 3 bytes for data size
    
    # Timestamp and StreamID
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    
    # Combine to form the tag
    tag = tag_type + data_size_bytes + timestamp + stream_id + tag_name_data + value_data
    
    # PreviousTagSizeN
    previous_tag_size = struct.pack('>I', len(tag))
    
    return tag + previous_tag_size


def create_video_frame_tag(frame_data):
    """
    Create a simple video tag.
    
    Parameters:
    - frame_data: The raw video frame data (as bytes).
    
    Returns:
    A bytes object representing the video tag in FLV format.
    """
    # TagType (9 for video)
    tag_type = b'\x09'
    
    # DataSize
    data_size_bytes = struct.pack('>I', len(frame_data))[1:]  # 3 bytes for data size
    
    # Timestamp and StreamID
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    
    # Combine to form the tag
    tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
    
    # PreviousTagSizeN
    previous_tag_size = struct.pack('>I', len(tag))
    
    return tag + previous_tag_size


def create_extended_encrypted_flv_file(file_path):
    """
    Create an extended and encrypted FLV file with additional complex features.
    """
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV Header for version 1 with audio and video
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Create DRM and Accessibility Features tags
    drm_tag = create_script_data_tag("DRM", "True")
    accessibility_features_tag = create_script_data_tag("AccessibilityFeatures", "Enabled")
    
    # Create a simple video frame (this is just a placeholder for demonstration purposes)
    video_frame_data = b'\x00' * 100  # 100 bytes of zero for video data
    video_frame_tag = create_video_frame_tag(video_frame_data)
    
    # Combine all elements to form the FLV content
    flv_content = flv_header + drm_tag + accessibility_features_tag + video_frame_tag + previous_tag_size_0
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_encrypted_example.flv'
create_extended_encrypted_flv_file(flv_file_path)

print(f'Extended encrypted FLV file with Accessibility Features and more complex file features created at: {flv_file_path}')