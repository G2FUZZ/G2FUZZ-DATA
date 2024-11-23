import os
import struct

def create_complex_flv(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header for a video file
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x01, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0 always 0 for the first tag after the FLV header
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Construct a script data object (onMetaData) with multiple info
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        0x00, 0x00, 0x00, 0x00,  # Placeholder for Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for metadata)
        0x00, 0x00, 0x00,  # StreamID always 0
        0x02, 0x00, 0x0A,  # String marker and length for 'onMetaData'
        *b'onMetaData',  # 'onMetaData' string
        0x08, 0x00, 0x00, 0x00, 0x04,  # ECMA array marker and length (4 items)
    ])
    
    # Adding multiple metadata entries
    metadata_entries = [
        ('width', 640),
        ('height', 360),
        ('duration', 120.5),
        ('DRM', 'Enabled with DRM'),
    ]
    
    for key, value in metadata_entries:
        script_data_tag.extend(encode_amf0_data(key, value))
    
    # Finalize script data tag size
    script_data_tag_size = len(script_data_tag) - 11  # Subtract the tag header size
    script_data_tag[4:8] = struct.pack('>I', script_data_tag_size)[1:]  # Update the data size
    
    # Calculate the script data tag size and append it as PreviousTagSize at the end of the tag
    script_data_tag += struct.pack('>I', len(script_data_tag))
    
    # Example video frame (keyframe)
    video_frame_tag = create_video_frame()

    # Write the FLV file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_data_tag)
        f.write(video_frame_tag)
        # Further video/audio tags would follow here

def encode_amf0_data(key, value):
    """Encode AMF0 data for a given key-value pair."""
    data = bytearray()
    data.append(0x00)  # AMF0 type: String
    data.extend(struct.pack('>H', len(key)))  # String length
    data.extend(key.encode('utf-8'))  # String data
    
    if isinstance(value, str):
        data.append(0x02)  # AMF0 type: String
        data.extend(struct.pack('>H', len(value)))  # String length
        data.extend(value.encode('utf-8'))  # String data
    elif isinstance(value, (int, float)):
        data.append(0x00)  # AMF0 type: Number
        data.extend(struct.pack('>d', value))  # Number data
    return data

def create_video_frame():
    """Create a simple video frame tag (for demonstration purposes, not actual video data)."""
    video_data = bytearray([
        0x09,  # Tag type video
        0x00, 0x00, 0x0A,  # Data size (just an example size)
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for demonstration)
        0x00, 0x00, 0x00,  # StreamID always 0
        0x17, 0x01, 0x00, 0x00, 0x00,  # Video data (key frame, AVC, composition time 0)
        # Here would be the AVC video data
    ])
    video_data += struct.pack('>I', len(video_data))
    return video_data

if __name__ == "__main__":
    create_complex_flv('./tmp/complex_example_with_drm.flv')