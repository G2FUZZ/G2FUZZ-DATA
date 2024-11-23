import os
import struct

def create_flv_header(has_audio=True, has_video=True):
    """Create the FLV file header."""
    type_flags = 0
    if has_audio:
        type_flags |= 0b100
    if has_video:
        type_flags |= 0b001
    return bytes([
        0x46, 0x4C, 0x56,  # 'FLV'
        0x01,  # Version 1
        type_flags,  # Type flags (audio + video)
        0x00, 0x00, 0x00, 0x09,  # Header size
        0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
    ])

def create_on_metadata(duration, width, height):
    """Create an onMetaData tag."""
    metadata = f"duration={duration}\0width={width}\0height={height}\0\0"
    data_size = len(metadata)
    return bytes([
        0x12,  # Script data tag
    ]) + struct.pack('>I', data_size)[1:] + bytes([
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + metadata.encode('utf-8')

def create_video_tag(data, timestamp):
    """Create a video tag."""
    data_size = len(data)
    return bytes([
        0x09,  # Video tag
    ]) + struct.pack('>I', data_size)[1:] + struct.pack('>I', timestamp)[:3] + bytes([
        0x00,  # Timestamp extended
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + data

def create_audio_tag(data, timestamp):
    """Create an audio tag."""
    data_size = len(data)
    return bytes([
        0x08,  # Audio tag
    ]) + struct.pack('>I', data_size)[1:] + struct.pack('>I', timestamp)[:3] + bytes([
        0x00,  # Timestamp extended
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + data

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "complex_structure.flv")  # Corrected variable name

# Start writing to the file
with open(output_path, 'wb') as f:
    # Write the FLV header
    f.write(create_flv_header(has_audio=True, has_video=True))
    
    # Write the onMetaData tag
    f.write(create_on_metadata(duration=10.0, width=640, height=360))
    
    # Example video and audio data (placeholder)
    video_data = b'\x00\x00\x00\x00'  # Placeholder video data
    audio_data = b'\x00\x00'  # Placeholder audio data
    
    # Write a couple of video and audio tags with simulated timestamps
    timestamps = [0, 1000, 2000, 3000]  # in milliseconds
    for timestamp in timestamps:
        f.write(create_video_tag(video_data, timestamp))
        f.write(create_audio_tag(audio_data, timestamp))  # Corrected function name
    
    # You can repeat the above loop or customize it to simulate a real video file

print(f"Generated complex FLV file at: {output_path}")