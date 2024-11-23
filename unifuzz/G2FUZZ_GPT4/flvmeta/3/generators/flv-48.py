import os
import struct
import random

def create_flv_header(has_audio=True, has_video=True):
    """Creates the FLV file header."""
    type_flags = (has_audio << 2) | has_video
    flv_header = struct.pack('3sBBI', b'FLV', 0x01, type_flags, 0x09)
    return flv_header + b'\x00\x00\x00\x00'

def create_metadata_tag(width=640, height=480, duration=0, framerate=30, audiocodecid=10, audiosamplerate=44100):
    """Creates an onMetaData tag with extended video and audio properties."""
    metadata = (f"width={width}\nheight={height}\nduration={duration}\nframerate={framerate}\n"
                f"audiocodecid={audiocodecid}\naudiosamplerate={audiosamplerate}\n").encode()
    data_size = len(metadata)
    timestamp = 0
    stream_id = 0
    return struct.pack('>BIII', 18, data_size, timestamp, stream_id) + metadata

def create_audio_tag(data, timestamp=0):
    """Creates an audio tag."""
    sound_format = 10  # AAC
    sound_rate = 3    # 44 kHz
    sound_size = 1    # 16-bit samples
    sound_type = 1    # Stereo sound
    aac_packet_type = 1  # AAC raw
    audio_data = struct.pack('>B', ((sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)) + struct.pack('>B', aac_packet_type) + data
    data_size = len(audio_data)
    stream_id = 0
    return struct.pack('>BIII', 8, data_size, timestamp, stream_id) + audio_data

def create_video_tag(data, timestamp=0, frame_type='keyframe'):
    """Enhanced to support variable frame rates and different frame types."""
    frame_types = {'keyframe': 0x10, 'interframe': 0x20}
    codec_id = 0x07  # AVC (H.264)
    avc_packet_type = 1  # AVC NALU
    composition_time = 0
    video_data = struct.pack('>BHB', frame_types[frame_type] | codec_id, avc_packet_type, composition_time) + data
    data_size = len(video_data)
    stream_id = 0
    return struct.pack('>BIII', 9, data_size, timestamp, stream_id) + video_data

def create_previous_tag_size(tag):
    """Creates the PreviousTagSize field based on the last tag's size."""
    return struct.pack('>I', len(tag))

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "more_complex_example.flv")

# FLV file content
flv_content = bytearray(create_flv_header())

# Add extended metadata tag
metadata_tag = create_metadata_tag(duration=120, audiocodecid=10, audiosamplerate=44100)
flv_content.extend(metadata_tag)
flv_content.extend(create_previous_tag_size(metadata_tag))

# Simulate adding multiple video tags with variable frame rates and both keyframe and interframe types
timestamps = [0, 500, 1000, 1500, 2000]  # Example timestamps in milliseconds
for timestamp in timestamps:
    frame_type = 'keyframe' if timestamp == 0 else 'interframe'
    video_data = os.urandom(256)  # Simulated video frame data
    video_tag = create_video_tag(video_data, timestamp, frame_type)
    flv_content.extend(video_tag)
    flv_content.extend(create_previous_tag_size(video_tag))

# Simulate adding an audio tag
audio_data = os.urandom(128)  # Simulated audio frame data
audio_tag = create_audio_tag(audio_data, 1000)  # Example timestamp
flv_content.extend(audio_tag)
flv_content.extend(create_previous_tag_size(audio_tag))

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_content)

print(f"Generated FLV file at: {output_path}")