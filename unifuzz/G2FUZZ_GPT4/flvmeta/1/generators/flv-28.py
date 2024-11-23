import os

def create_flv_with_drm(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header for a video file with no audio
    # FLV version 1, has video, no audio, header length 9
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x01, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0 always 0 for the first tag after the FLV header
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Construct a script data object (onMetaData) with DRM info
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        0x00, 0x00, 0x1B,  # Data size (adjusted for DRM metadata)
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for metadata)
        0x00, 0x00, 0x00,  # StreamID always 0
        0x02, 0x00, 0x0A,  # String marker and length
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61,  # 'onMetaData' string
        0x08, 0x00, 0x00, 0x00, 0x01,  # ECMA array marker and length (1 for DRM)
        # Adding DRM key-value
        0x00, 0x03,  # DRM key length
        0x44, 0x52, 0x4D,  # 'DRM'
        0x02, 0x00, 0x0F,  # Type String, length of the value
        0x45, 0x6E, 0x61, 0x62, 0x6C, 0x65, 0x64, 0x20, 0x77, 0x69, 0x74, 0x68, 0x20, 0x44, 0x52, 0x4D,  # 'Enabled with DRM'
    ])
    
    # Calculate the script data tag size and append it as PreviousTagSize at the end of the tag
    script_data_tag_size = len(script_data_tag) - 11  # Subtract the tag header size
    script_view = bytearray([
        (script_data_tag_size >> 24) & 0xFF,
        (script_data_tag_size >> 16) & 0xFF,
        (script_data_tag_size >> 8) & 0xFF,
        script_data_tag_size & 0xFF,
    ])
    script_data_tag += script_view
    
    # Write the FLV file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_data_tag)
        # Further video/audio tags would follow here

if __name__ == "__main__":
    create_flv_with_drm('./tmp/example_with_drm.flv')