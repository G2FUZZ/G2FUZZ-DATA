import os
import struct

def create_complex_flv(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Script data tag (onMetaData)
    on_metadata = b'onMetaData'
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        0x00, 0x00, 0x00,  # Placeholder for data size, will be replaced later
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID
        0x02,  # String marker
    ]) + struct.pack('>H', len(on_metadata)) + on_metadata + bytearray([
        0x08, 0x00, 0x00, 0x00, 0x01,  # ECMA array marker and length (1 property for example)
        0x00, 0x05,  # Length of 'width' string
        0x77, 0x69, 0x64, 0x74, 0x68,  # 'width' string
        0x00, 0x40, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00,  # Number marker and value 144.0
        0x00, 0x00, 0x09  # Object end marker
    ])
    
    # Update script data size
    script_data_size = len(script_data_tag) - 11  # Subtract tag header
    script_data_tag[1:4] = struct.pack('>I', script_data_size)[1:]
    
    # Append PreviousTagSize
    script_data_tag += struct.pack('>I', len(script_data_tag))
    
    # Sample AVC video tag (Simplified for example)
    video_data = bytearray([
        0x09,  # Tag type video
        0x00, 0x00, 0x0D,  # Data size, placeholder, will be adjusted
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID
        0x17, 0x01, 0x00, 0x00, 0x00,  # AVC video packet header (key frame, AVC NALU)
        # Dummy NALU data (not a real video frame, for demonstration only)
        0x00, 0x00, 0x00, 0x01,  # Start code
        0x67, 0x64, 0x00, 0x0A,  # SPS NALU (simplified)
        0x00, 0x00, 0x00, 0x01,  # Start code
        0x68, 0x65, 0x00, 0x0B,  # PPS NALU (simplified)
    ])
    
    # Update video data size
    video_data_size = len(video_data) - 11  # Subtract tag header
    video_data[1:4] = struct.pack('>I', video_data_size)[1:]
    
    # Append PreviousTagSize for video tag
    video_data += struct.pack('>I', len(video_data))
    
    # Write the FLV file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_data_tag)
        f.write(video_data)
        # Further video/audio tags would follow here

if __name__ == "__main__":
    create_complex_flv('./tmp/complex_example.flv')