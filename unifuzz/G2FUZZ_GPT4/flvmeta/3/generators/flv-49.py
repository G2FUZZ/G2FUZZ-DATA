import os
from datetime import datetime

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "complex_example.flv")

# Function to generate a script data tag (metadata)
def generate_metadata_tag(video_duration, width, height):
    # Example metadata script data tag with onMetaData event
    # This is a simplified representation and does not conform to the actual AMF format
    metadata = f"onMetaData duration={video_duration} width={width} height={height}".encode()
    data_size = len(metadata)
    tag = bytes([
        0x12,  # Tag type script data
        (data_size >> 16) & 0xFF, (data_size >> 8) & 0xFF, data_size & 0xFF,  # Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID
    ]) + metadata
    return tag

# Function to generate a simple audio tag
def generate_audio_tag(timestamp, sample_data):
    data_size = len(sample_data)
    tag = bytes([
        0x08,  # Tag type audio
        (data_size >> 16) & 0xFF, (data_size >> 8) & 0xFF, data_size & 0xFF,  # Data size
        (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF, timestamp & 0xFF,  # Timestamp
        0x00,  # TimestampExtended
        0x00, 0x00, 0x00,  # StreamID
    ]) + sample_data
    return tag

# FLV file header
flv_header = bytes([
    0x46, 0x4C, 0x56,  # Signature "FLV"
    0x01,  # Version 1
    0x05,  # TypeFlags (audio + video)
    0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    # FLV Body start
    0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
])

# Generate metadata tag
metadata_tag = generate_metadata_tag(video_duration=60, width=640, height=360)

# Example audio sample data (This is not actual audio data, just a placeholder)
audio_sample_data = bytes([0x00] * 10)  # Placeholder for actual audio frame data
audio_tag = generate_audio_tag(timestamp=1000, sample_data=audio_sample_data)

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    f.write(metadata_tag)
    # Write a PreviousTagSize for metadata tag
    f.write((len(metadata_tag) + 11).to_bytes(4, 'big'))  # +11 for the tag header size
    f.write(audio_tag)
    # Future tags (such as video frames) can be added here in a similar manner
    # For each additional tag, update the PreviousTagSize accordingly

print(f"Generated complex FLV file at: {output_path}")