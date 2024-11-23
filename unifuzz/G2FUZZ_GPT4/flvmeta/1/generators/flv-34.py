import os
import struct

def create_complex_flv_with_drm(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header for a video file with possibly no audio
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x01, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0 always 0 for the first tag after the FLV header
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Construct a script data object (onMetaData) with multiple metadata entries
    on_metadata = construct_script_data({
        "duration": 0.0,
        "width": 1920,
        "height": 1080,
        "videodatarate": 0,
        "framerate": 24.0,
        "videocodecid": 7,  # AVC
        "DRM": "Enabled with DRM",
    })
    
    # Create a simple video tag (e.g., AVC keyframe)
    video_data = construct_video_frame()
    
    # Write the FLV file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(on_metadata)
        
        # Write PreviousTagSize for script data tag
        f.write(struct.pack('>I', len(on_metadata)))
        
        f.write(video_data)
        # If there were further video/audio tags, they would follow here, each preceded by the PreviousTagSize

def construct_script_data(metadata):
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        # Placeholder for data size
        0x00, 0x00, 0x00,  # To be filled in later
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for metadata)
        0x00, 0x00, 0x00,  # StreamID always 0
    ])
    
    # Start of script data 'onMetaData'
    script_data = bytearray([
        0x02, 0x00, 0x0A,  # String marker and length for 'onMetaData'
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61  # 'onMetaData'
    ])
    
    # Add metadata entries
    script_data += construct_ecma_array(metadata)
    
    # Calculate and fill in data size
    data_size = len(script_data)
    script_data_tag[1:4] = struct.pack('>I', data_size)[1:]
    
    return script_data_tag + script_data

def construct_ecma_array(metadata):
    # ECMA array header: type (0x08) + array length
    ecma_array = bytearray([0x08]) + struct.pack('>I', len(metadata))
    
    for key, value in metadata.items():
        # Key: length-prefixed string
        key_encoded = key.encode('utf-8')
        ecma_array += struct.pack('>H', len(key_encoded)) + key_encoded
        
        # Value: type-prefixed value
        if isinstance(value, str):
            value_encoded = value.encode('utf-8')
            ecma_array += bytearray([0x02]) + struct.pack('>H', len(value_encoded)) + value_encoded
        elif isinstance(value, (int, float)):
            ecma_array += bytearray([0x00]) + struct.pack('>d', float(value))
    
    # End of object marker
    ecma_array += bytearray([0x00, 0x00, 0x09])
    return ecma_array

def construct_video_frame():
    # Example of a simple video frame tag (e.g., AVC keyframe)
    # For the sake of simplicity, this example does not contain actual video data.
    frame_size = 14  # Placeholder size
    timestamp = 0
    video_data = bytearray([
        0x09,  # Tag type video
        0x00, 0x00, 0x0E,  # Data size, placeholder for now
        (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF, timestamp & 0xFF,  # Timestamp
        (timestamp >> 24) & 0xFF,  # TimestampExtended
        0x00, 0x00, 0x00,  # StreamID always 0
        0x17, 0x00, 0x00, 0x00, 0x00,  # Simple video data (e.g., AVC keyframe header)
        # Actual video frame data would go here
    ])
    # Previous tag size (placeholder for now, should be set to the real size of this tag when multiple tags are used)
    previous_tag_size = struct.pack('>I', frame_size)
    return video_data + previous_tag_size

if __name__ == "__main__":
    create_complex_flv_with_drm('./tmp/complex_example_with_drm.flv')