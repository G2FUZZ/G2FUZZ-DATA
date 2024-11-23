import os
import struct
import random

def create_flv_header(has_audio=True, has_video=True):
    """Creates the FLV file header."""
    type_flags = (has_audio << 2) | has_video
    flv_header = struct.pack('3sBBI', b'FLV', 0x01, type_flags, 0x09)
    return flv_header + b'\x00\x00\x00\x00'

def create_metadata_tag(width=640, height=480, duration=0, framerate=30, audiocodecid=2, audiosamplerate=44100):
    """Creates an onMetaData tag with more detailed video and audio properties."""
    metadata_script = {
        'width': width,
        'height': height,
        'duration': duration,
        'framerate': framerate,
        'videocodecid': 7,  # AVC
        'audiocodecid': audiocodecid,
        'audiosamplerate': audiosamplerate
    }
    # Simplified; real implementation would use AMF0 encoding for the metadata
    metadata = str(metadata_script).encode()
    data_size = len(metadata)
    timestamp = 0
    stream_id = 0
    return struct.pack('>BIII', 18, data_size, timestamp, stream_id) + metadata

def create_video_tag(data, timestamp=0, frame_type='keyframe'):
    """Creates a video tag with frame_type either 'keyframe' or 'interframe'."""
    frame_types = {'keyframe': 0x10, 'interframe': 0x20}
    codec_id = 0x07  # AVC
    avc_packet_type = 0x01  # AVC NALU
    composition_time = 0
    video_data = struct.pack('>BHB', frame_types[frame_type] | codec_id, avc_packet_type, composition_time) + data
    data_size = len(video_data)
    stream_id = 0
    return struct.pack('>BIII', 9, data_size, timestamp, stream_id) + video_data

def create_audio_tag(data, timestamp=0):
    """Creates an audio tag."""
    sound_format = 10  # AAC
    sound_rate = 3  # 44 KHz
    sound_size = 1  # 16-bit samples
    sound_type = 1  # Stereo sound
    aac_packet_type = 1  # AAC raw
    audio_data = struct.pack('>BB', (sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type, aac_packet_type) + data
    data_size = len(audio_data)
    stream_id = 0
    return struct.pack('>BIII', 8, data_size, timestamp, stream_id) + audio_data

def create_previous_tag_size(tag):
    """Creates the PreviousTagSize field based on the last tag's size."""
    return struct.pack('>I', len(tag))

def generate_random_video_frames(num_frames, start_timestamp):
    """Generates random video frames (both keyframes and interframes)."""
    frames = []
    timestamp = start_timestamp
    for i in range(num_frames):
        frame_type = 'keyframe' if i % 30 == 0 else 'interframe'  # Assume a keyframe every 30 frames
        frame_data = random.randbytes(100)  # Simulated video frame data
        video_tag = create_video_tag(frame_data, timestamp, frame_type)
        frames.append(video_tag)
        timestamp += 33  # Assuming a frame rate of ~30fps
    return frames

def generate_random_audio_frames(num_frames, start_timestamp):
    """Generates random audio frames."""
    frames = []
    timestamp = start_timestamp
    for i in range(num_frames):
        frame_data = random.randbytes(50)  # Simulated audio frame data
        audio_tag = create_audio_tag(frame_data, timestamp)
        frames.append(audio_tag)
        timestamp += 23  # Simulated variable frame rate for audio
    return frames

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "more_complex_example.flv")

# FLV file content
flv_content = bytearray(create_flv_header())

# Add metadata tag
metadata_tag = create_metadata_tag()
flv_content.extend(metadata_tag)
flv_content.extend(create_previous_tag_size(metadata_tag))

# Simulate adding multiple video frames
video_frames = generate_random_video_frames(60, 0)
for frame in video_frames:
    flv_content.extend(frame)
    flv_content.extend(create_previous_tag_size(frame))

# Simulate adding multiple audio frames
audio_frames = generate_random_audio_frames(75, 0)
for frame in audio_frames:
    flv_content.extend(frame)
    flv_content.extend(create_previous_tag_size(frame))

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_content)

print(f"Generated FLV file at: {output_path}")