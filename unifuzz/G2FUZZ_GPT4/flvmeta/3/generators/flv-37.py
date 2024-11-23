import os
import struct

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "complex_example.flv")

# FLV file header
flv_header = bytes([
    0x46, 0x4C, 0x56,  # Signature "FLV"
    0x01,  # Version 1
    0x05,  # TypeFlags (audio + video)
    0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    # FLV Body start
    0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
])

# Metadata tag (simulated, not actual metadata structure)
metadata_tag = bytes([
    0x12,  # Tag type script
    0x00, 0x00, 0x20,  # Data size (32 bytes for this example)
    0x00, 0x00, 0x00, 0x00,  # Timestamp
    0x00, 0x00, 0x00,  # StreamID
    # Simulated metadata content
]) + bytes([i % 256 for i in range(32)])  # Just a placeholder for metadata, fixed to avoid byte range error

# Function to create a sample video tag
def create_video_tag(timestamp=0, data_size=40):
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
    ]) + bytes([i % 256 for i in range(data_size)])  # Simulated video data, fixed to avoid byte range error

# Function to create a sample audio tag
def create_audio_tag(timestamp=0, data_size=25):
    return bytes([
        0x08,  # Tag type audio
        (data_size >> 16) & 0xFF,
        (data_size >> 8) & 0xFF,
         data_size & 0xFF,
        (timestamp >> 16) & 0xFF,
        (timestamp >> 8) & 0xFF,
         timestamp & 0xFF,
        (timestamp >> 24) & 0xFF,  # Extended timestamp
        0x00, 0x00, 0x00,  # StreamID
    ]) + bytes([i % 256 for i in range(data_size)])  # Simulated audio data, fixed to avoid byte range error

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    f.write(metadata_tag)
    previous_tag_size = 11 + len(metadata_tag) - 11  # Tag header is 11 bytes
    f.write(struct.pack('>I', previous_tag_size))
    
    # Write a sample video tag
    video_tag = create_video_tag(timestamp=1000, data_size=1024)
    f.write(video_tag)
    previous_tag_size = 11 + 1024
    f.write(struct.pack('>I', previous_tag_size))
    
    # Write a sample audio tag
    audio_tag = create_audio_tag(timestamp=2000, data_size=512)
    f.write(audio_tag)
    previous_tag_size = 11 + 512
    f.write(struct.pack('>I', previous_tag_size))

print(f"Generated a more complex FLV file with multiple tags at: {output_path}")