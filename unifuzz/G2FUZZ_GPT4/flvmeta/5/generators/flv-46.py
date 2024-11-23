import os
import struct
import random

def serialize_amf0_str(s):
    """Serialize a string into AMF0 format."""
    return struct.pack('>H', len(s)) + s.encode('utf-8')

def serialize_amf0_double(number):
    """Serialize a double into AMF0 format."""
    return b'\x00' + struct.pack('>d', number)

def serialize_amf0_bool(value):
    """Serialize a boolean into AMF0 format."""
    return b'\x01' + (b'\x01' if value else b'\x00')

def serialize_amf0_object(obj):
    """Serialize a dictionary into AMF0 object format."""
    serialized = b''
    for key, value in obj.items():
        serialized += serialize_amf0_str(key)
        if isinstance(value, str):
            serialized += b'\x02' + serialize_amf0_str(value)
        elif isinstance(value, bool):
            serialized += serialize_amf0_bool(value)
        elif isinstance(value, (int, float)):
            serialized += serialize_amf0_double(value)
    return serialized + b'\x00\x00\x09'  # End Of Object marker

def generate_video_data(frame_count, width, height):
    """Generate dummy video data for a number of frames."""
    video_data = bytearray()
    for _ in range(frame_count):
        # Simulate a simple keyframe structure
        frame_data = os.urandom(width * height // 10)  # Simplified frame data
        video_data.extend(frame_data)
    return video_data

def generate_audio_data(sample_count):
    """Generate dummy audio data."""
    return os.urandom(sample_count)

def create_flv_with_advanced_features(output_path, video_duration=10, framerate=30, width=640, height=480):
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Generating onMetaData
    on_meta_data = {
        'duration': video_duration,
        'width': width,
        'height': height,
        'videodatarate': 1500,
        'framerate': framerate,
        'videocodecid': 7,
        'audiodatarate': 128,
        'audiosamplerate': 44100,
        'audiosamplesize': 16,
        'stereo': True,
        'audiocodecid': 10,
        'filesize': 0,  # Placeholder, to be updated after file creation
        'encoder': 'Enhanced FLV Generator',
        'hasKeyframes': True,
        'hasVideo': True,
        'hasAudio': True,
        'hasMetadata': True,
        'canSeekToEnd': True
    }
    
    # Serialize onMetaData
    on_meta_data_serialized = b'\x12' + serialize_amf0_object({'onMetaData': on_meta_data})
    script_data_length = len(on_meta_data_serialized) - 1  # Subtract 1 for the tag type byte
    script_tag_full_length = struct.pack('>L', script_data_length)[1:] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    total_frames = video_duration * framerate
    video_data = generate_video_data(total_frames, width, height)
    audio_data = generate_audio_data(44100 * video_duration)  # Simplified audio data

    # Generate video and audio tags for each frame
    video_tag = b''
    audio_tag = b''
    for i in range(total_frames):
        frame_data = video_data[i * (len(video_data) // total_frames):(i + 1) * (len(video_data) // total_frames)]
        video_tag += b'\x09' + struct.pack('>L', len(frame_data) + 5)[1:] + b'\x00\x00\x00\x00' + frame_data
        video_tag += struct.pack('>L', len(frame_data) + 11)  # Tag size including header

    for i in range(0, len(audio_data), 1024):
        sample_data = audio_data[i:i + 1024]
        audio_tag += b'\x08' + struct.pack('>L', len(sample_data) + 2)[1:] + b'\x00\x00\x00\x00' + sample_data
        audio_tag += struct.pack('>L', len(sample_data) + 11)  # Tag size including header

    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    flv_file_path = os.path.join(output_path, 'advanced_video_with_complex_structures.flv')
    with open(flv_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag)
        f.write(audio_tag)
    
    print('Advanced FLV file with complex structures created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_advanced_features(output_dir)