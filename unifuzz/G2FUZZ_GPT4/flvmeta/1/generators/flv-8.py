import os

def create_flv_with_script_data(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header for a video file with no audio
    # FLV version 1, has video, no audio, header length 9
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x01, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0 always 0 for the first tag after the FLV header
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Construct a script data object (onMetaData)
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        0x00, 0x00, 0x0D,  # Data size (example size, likely not correct for real data)
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for metadata)
        0x00, 0x00, 0x00,  # StreamID always 0
        0x02, 0x00, 0x0A,  # String marker and length
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61,  # 'onMetaData' string
        0x08, 0x00, 0x00, 0x00, 0x00,  # ECMA array marker and length (0 for this example)
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
    create_flv_with_script_data('./tmp/example.flv')