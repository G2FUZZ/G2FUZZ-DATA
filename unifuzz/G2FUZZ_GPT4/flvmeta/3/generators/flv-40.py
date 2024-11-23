import os
import struct
from random import randint

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "enhanced_complex_example.flv")

# FLV file header
flv_header = bytes([
    0x46, 0x4C, 0x56,  # Signature "FLV"
    0x01,  # Version 1
    0x05,  # TypeFlags (audio + video)
    0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    # FLV Body start
    0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
])

# Function to encode AMF0 data type
def encode_amf0_string(s):
    return struct.pack('>H', len(s)) + s.encode('utf-8')

# Function to generate metadata tag with AMF0 encoding
def create_metadata_tag():
    on_metadata = b'\x02' + encode_amf0_string('onMetaData')
    data = b'\x08' + struct.pack('>L', 3)  # Strict array with 3 elements
    data += encode_amf0_string('width') + b'\x00?\xf0\x00\x00\x00\x00\x00\x00'
    data += encode_amf0_string('height') + b'\x00?\xf0\x00\x00\x00\x00\x00\x00'
    data += encode_amf0_string('framerate') + b'\x00\x40\x49\x00\x00\x00\x00\x00\x00'
    
    metadata_body = on_metadata + data
    metadata_tag = bytes([
        0x12,  # Tag type script
        (len(metadata_body) >> 16) & 0xFF,
        (len(metadata_body) >> 8) & 0xFF,
        len(metadata_body) & 0xFF,
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID
    ]) + metadata_body
    return metadata_tag

# Enhanced function to create a sample video tag, including keyframes
def create_video_tag(timestamp=0, data_size=40, is_keyframe=False):
    frame_type = 0x10 if is_keyframe else 0x20  # 0x10 for keyframe, 0x20 for inter frame
    codec_id = 0x07  # AVC
    video_data = bytes([frame_type | codec_id]) + bytes([i % 256 for i in range(data_size)])
    return bytes([
        0x09,  # Tag type video
        (data_size >> 16) & 0xFF,
        (data_size >> 8) & 0xFF,
         data_size & 0xFF,
        (timestamp >> 16) & 0xFF,
        (timestamp >> 8) & 0xFF,
         timestamp & 0xFF,
        (timestamp >> 24) & 0xFF,  # Extended timestamp
        0x00, 0x00, 0x00,  # StreamID
    ]) + video_data

# Function to generate a series of tags
def generate_tags():
    tags = []
    timestamp = 0
    for _ in range(5):  # Generate 5 video frames
        is_keyframe = randint(0, 1) == 1
        tags.append(create_video_tag(timestamp, data_size=randint(500, 1024), is_keyframe=is_keyframe))
        timestamp += randint(100, 1000)
    
    # The original code snippet was missing the create_audio_tag function.
    # Assuming a similar structure to create_video_tag for demonstration purposes.
    def create_audio_tag(timestamp, data_size=40):
        audio_data = bytes([i % 256 for i in range(data_size)])
        return bytes([
            0x08,  # Tag type audio
            (data_size >> 16) & 0xFF,
            (data_size >> 8) & 0xFF,
             data_size & 0xFF,
            (timestamp >> 16) & 0xFF,
            (timestamp >> 8) & 0xFF,
             timestamp & 0xFF,
            0x00,  # Extended timestamp
            0x00, 0x00, 0x00,  # StreamID
        ]) + audio_data

    for _ in range(3):  # Generate 3 audio frames
        tags.append(create_audio_tag(timestamp, data_size=randint(200, 512)))
        timestamp += randint(100, 1000)
    
    return tags

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    
    metadata_tag = create_metadata_tag()
    f.write(metadata_tag)
    previous_tag_size = 11 + len(metadata_tag) - 11  # Tag header is 11 bytes
    f.write(struct.pack('>I', previous_tag_size))
    
    tags = generate_tags()
    for tag in tags:
        f.write(tag)
        previous_tag_size = 11 + len(tag) - 11
        f.write(struct.pack('>I', previous_tag_size))

print(f"Generated an enhanced FLV file with complex structures at: {output_path}")