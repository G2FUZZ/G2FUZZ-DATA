import os
import struct
from datetime import datetime

def create_flv_header(has_audio=True, has_video=True):
    """Create the FLV file header."""
    type_flags = 0
    if has_audio:
        type_flags |= 0b100
    if has_video:
        type_flags |= 0b001
    return bytes([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        type_flags,  # TypeFlags (audio + video)
        0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
        0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
    ])

def create_metadata_tag(width, height, duration, audio_sample_rate, audio_channels):
    """Create an onMetaData tag with video width, height, and duration, and audio sample rate and channels."""
    metadata = f"onMetaData width={width} height={height} duration={duration} audioSampleRate={audio_sample_rate} audioChannels={audio_channels}"
    data_size = len(metadata)
    return struct.pack('>BIII', 0x12, data_size, 0, 0) + metadata.encode() + struct.pack('>I', data_size)

def create_audio_tag(timestamp, sample_data):
    """Create an audio tag."""
    data_size = len(sample_data)
    return struct.pack('>BIII', 0x08, data_size, timestamp, 0) + sample_data

def create_video_frame_tag(timestamp, frame_data, keyframe=False):
    """Create a video tag for a frame, marking it as a keyframe if specified."""
    frame_type = 0x10 if keyframe else 0x20  # Keyframe type or inter frame
    codec_id = 0x07  # AVC
    data_size = len(frame_data) + 5  # Additional bytes for AVC header
    return struct.pack('>BIII', 0x09, data_size, timestamp, 0) + bytes([frame_type | codec_id, 0x00, 0x00, 0x00]) + frame_data

def create_flv_file(output_path, width, height, duration, audio_sample_rate, audio_channels):
    """Generate an FLV file with specified parameters."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'wb') as f:
        f.write(create_flv_header())
        f.write(create_metadata_tag(width, height, duration, audio_sample_rate, audio_channels))
        
        # Example content - In a real scenario, you would loop through actual frame data and timestamps.
        timestamps = [0, 500, 1000, 1500]  # In milliseconds
        for ts in timestamps:
            f.write(create_audio_tag(ts, b'\x00' * 100))  # Dummy audio data
            f.write(create_video_frame_tag(ts, b'\x00' * 250, keyframe=(ts == 0)))  # Dummy video frame data
        
        # Write final PreviousTagSize (Dummy value)
        f.write(bytes([0x00, 0x00, 0x00, 0x1E]))

output_dir = "./tmp/"
output_path = os.path.join(output_dir, "complex_structure_video.flv")

create_flv_file(output_path, width=640, height=480, duration=2, audio_sample_rate=44100, audio_channels=2)

print(f"Generated FLV file with complex structures at: {output_path}")