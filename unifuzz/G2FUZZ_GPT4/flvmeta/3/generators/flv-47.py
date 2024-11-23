import os
import struct
from random import randint

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "enhanced_complex_structure.flv")

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

# Enhanced function to generate multiple metadata tags
def create_metadata_tags():
    tags = []
    properties = [
        ('width', 1280.0),
        ('height', 720.0),
        ('framerate', 30.0),
        ('videocodecid', 7.0),
        ('audiocodecid', 10.0)
    ]
    for prop_name, prop_value in properties:
        on_metadata = b'\x02' + encode_amf0_string('onMetaData')
        data = b'\x08' + struct.pack('>L', 1)  # Strict array with 1 element
        data += encode_amf0_string(prop_name) + struct.pack('>d', prop_value)
        metadata_body = on_metadata + data
        metadata_tag = bytes([
            0x12,  # Tag type script
            (len(metadata_body) >> 16) & 0xFF,
            (len(metadata_body) >> 8) & 0xFF,
            len(metadata_body) & 0xFF,
            0x00, 0x00, 0x00, 0x00,  # Timestamp
            0x00, 0x00, 0x00,  # StreamID
        ]) + metadata_body
        tags.append(metadata_tag)
    return tags

# AVC sequence header for video
def create_avc_sequence_header():
    avc_sequence_header = bytes([
        0x09,  # Tag type video
        0x00, 0x00, 0x0D,  # Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00,  # Timestamp extended
        0x00, 0x00, 0x00,  # StreamID
        0x17,  # Frame type (1 = keyframe) + Codec ID (7 = AVC)
        0x00,  # AVC packet type (0 = sequence header)
        0x00, 0x00, 0x00,  # Composition time
        # AVCDecoderConfigurationRecord starts here
        0x01,  # configurationVersion
        0x64,  # AVCProfileIndication
        0x00,  # profile_compatibility
        0x1F,  # AVCLevelIndication
        0xFF   # lengthSizeMinusOne and number of SPS NALUs
    ]) + bytes([0xE1, 0x00, 0x17, 0x67, 0x64, 0x00, 0x1F, 0xAC, 0xD9, 0x40, 0x50, 0x05, 0xBB, 0x01, 0x10, 0x00, 0x00, 0x3E, 0x90, 0x00, 0x0E, 0xA6, 0x08, 0xF1, 0x83, 0x19, 0x60])
    return avc_sequence_header

# AAC sequence header for audio
def create_aac_sequence_header():
    aac_sequence_header = bytes([
        0x08,  # Tag type audio
        0x00, 0x00, 0x02,  # Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00,  # Timestamp extended
        0x00, 0x00, 0x00,  # StreamID
        0xAF,  # SoundFormat (10 = AAC) + SoundRate (3 = 44kHz) + SoundSize (1 = 16-bit) + SoundType (1 = Stereo)
        0x00,  # AAC packet type (0 = sequence header)
        0x12, 0x10  # AudioSpecificConfig (MPEG-4 Audio)
    ])
    return aac_sequence_header

# Enhanced function to create a sample video tag, including keyframes and AVC NALUs
def create_video_tag(timestamp=0, data_size=40, is_keyframe=False):
    frame_type = 0x10 if is_keyframe else 0x20  # 0x10 for keyframe, 0x20 for inter frame
    codec_id = 0x07  # AVC
    avc_packet_type = 0x01  # NALU
    composition_time = 0x000000  # No composition time offset
    video_data = bytes([frame_type | codec_id, avc_packet_type]) + struct.pack('>I', composition_time)[1:] + bytes([i % 256 for i in range(data_size)])
    return bytes([
        0x09,  # Tag type video
        (data_size + 5) >> 16 & 0xFF,
        (data_size + 5) >> 8 & 0xFF,
         (data_size + 5) & 0xFF,
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
    tags.append(create_avc_sequence_header())  # Add AVC sequence header
    tags.append(create_aac_sequence_header())  # Add AAC sequence header

    for _ in range(5):  # Generate 5 video frames
        is_keyframe = randint(0, 1) == 1
        tags.append(create_video_tag(timestamp, data_size=randint(500, 1024), is_keyframe=is_keyframe))
        timestamp += randint(100, 1000)

    # Assuming a similar structure to create_video_tag for audio tags
    def create_audio_tag(timestamp, data_size=40):
        aac_packet_type = 0x01  # Raw AAC frame data
        audio_data = bytes([0xAF, aac_packet_type]) + bytes([i % 256 for i in range(data_size)])  # SoundFormat (10 = AAC) + SoundRate (3 = 44kHz) + SoundSize (1 = 16-bit) + SoundType (1 = Stereo)
        return bytes([
            0x08,  # Tag type audio
            (data_size + 2) >> 16 & 0xFF,
            (data_size + 2) >> 8 & 0xFF,
             (data_size + 2) & 0xFF,
            (timestamp >> 16) & 0xFF,
            (timestamp >> 8) & 0xFF,
             timestamp & 0xFF,
            (timestamp >> 24) & 0xFF,  # Extended timestamp
            0x00, 0x00, 0x00,  # StreamID
        ]) + audio_data
     
    for _ in range(3):  # Generate 3 audio frames
        tags.append(create_audio_tag(timestamp, data_size=randint(200, 512)))
        timestamp += randint(100, 1000)

    return tags

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    
    metadata_tags = create_metadata_tags()
    for tag in metadata_tags:
        f.write(tag)
        previous_tag_size = len(tag)
        f.write(struct.pack('>I', previous_tag_size))
    
    tags = generate_tags()
    for tag in tags:
        f.write(tag)
        previous_tag_size = len(tag)
        f.write(struct.pack('>I', previous_tag_size))

print(f"Generated an enhanced FLV file with complex structures at: {output_path}")