import os
import struct

def create_flv_header(has_audio=True, has_video=True):
    """Create the FLV file header."""
    type_flags = (has_audio << 2) | has_video
    header = struct.pack('>3sBBI', b'FLV', 1, type_flags, 9)
    return header + b'\x00\x00\x00\x00'  # PreviousTagSize0

def create_tag(tag_type, data, timestamp=0):
    """Create an FLV tag."""
    data_size = len(data)
    stream_id = 0
    return struct.pack('>BIII', tag_type, data_size, timestamp, stream_id) + data

def create_metadata_tag(duration, width, height):
    """Create a script data tag for metadata."""
    script_data = b''  # Simplified: Actual metadata encoding would be more complex
    return create_tag(18, script_data)

def create_video_tag(frame_data, timestamp, is_keyframe=True, codec_id=7):
    """Create a video tag."""
    frame_type = 1 if is_keyframe else 2
    video_data = struct.pack('>B', (frame_type << 4) | codec_id) + frame_data
    return create_tag(9, video_data, timestamp)

def create_audio_tag(audio_data, timestamp):
    """Create an audio tag."""
    sound_format = 2  # MP3 for example
    sound_rate = 3  # 44 kHz
    sound_size = 1  # 16-bit samples
    sound_type = 1  # Stereo sound
    audio_header = struct.pack('>B', (sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)
    return create_tag(8, audio_header + audio_data, timestamp)

def write_flv_file(output_path, tags):
    """Write the FLV content to a file."""
    with open(output_path, 'wb') as f:
        f.write(create_flv_header())
        for tag in tags:
            f.write(tag)
            f.write(struct.pack('>I', len(tag)))  # PreviousTagSize

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "complex_example.flv")

# Example frame and audio data (placeholders for actual data)
frame_data = b'\x00' * 300  # Placeholder for video frame data
audio_data = b'\x00' * 100  # Placeholder for audio data

# Creating multiple tags for a more complex structure
tags = [
    create_metadata_tag(duration=100, width=640, height=480),
    create_video_tag(frame_data, timestamp=0),
    create_audio_tag(audio_data, timestamp=1000),
    create_video_tag(frame_data, timestamp=2000, is_keyframe=False),
    create_audio_tag(audio_data, timestamp=3000),
]

write_flv_file(output_path, tags)

print(f"Generated complex FLV file at: {output_path}")