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

def create_flv_with_complex_features(output_path, video_duration=10, framerate=30, width=640, height=480):
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
        'encoder': 'Custom FLV Generator',
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

    # Placeholder for video and audio tags
    video_data = b'\x00' * 100  # Placeholder for video data
    audio_data = b'\x00' * 100  # Placeholder for audio data
    
    # Generate video and audio tags
    video_tag = b'\x09' + struct.pack('>L', len(video_data) + 5)[1:] + b'\x00\x00\x00\x00' + video_data
    audio_tag = b'\x08' + struct.pack('>L', len(audio_data) + 2)[1:] + b'\x00\x00\x00\x00' + audio_data
    video_tag_end = struct.pack('>L', len(video_tag) + 1)
    audio_tag_end = struct.pack('>L', len(audio_tag) + 1)

    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    flv_file_path = os.path.join(output_path, 'complex_video_with_accessibility_features.flv')
    with open(flv_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag)
        f.write(video_tag_end)
        f.write(audio_tag)
        f.write(audio_tag_end)  # Corrected line
    
    print('Complex FLV file with advanced features created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_complex_features(output_dir)