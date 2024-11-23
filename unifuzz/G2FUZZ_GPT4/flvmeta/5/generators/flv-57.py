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

def generate_video_frame(frame_number, width, height):
    """Generate a simulated video frame."""
    # Creating a simple pattern for the video frame
    frame_data = bytearray(random.getrandbits(8) for _ in range(width * height // 10))
    return frame_data

def generate_audio_frame(frame_number):
    """Generate a simulated audio frame."""
    # Creating a simple waveform pattern for the audio frame
    frame_data = bytearray(random.getrandbits(8) for _ in range(256))
    return frame_data

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
        'videocodecid': 7,  # AVC
        'audiodatarate': 128,
        'audiosamplerate': 44100,
        'audiosamplesize': 16,
        'stereo': True,
        'audiocodecid': 10,  # AAC
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

    # Generate video and audio tags
    video_tags = b''
    audio_tags = b''
    total_tags_length = 0

    for frame_number in range(video_duration * framerate):
        # Simulate variable frame rate by skipping some frames
        if frame_number % random.randint(1, 3) == 0:
            video_frame = generate_video_frame(frame_number, width, height)
            video_tag_header = b'\x09' + struct.pack('>L', len(video_frame) + 5)[1:] + b'\x00\x00\x00\x00'
            video_tag = video_tag_header + video_frame
            video_tags += video_tag + struct.pack('>L', len(video_tag) + 1)
            total_tags_length += len(video_tag) + 4

        # Generate audio frame for every video frame
        audio_frame = generate_audio_frame(frame_number)
        audio_tag_header = b'\x08' + struct.pack('>L', len(audio_frame) + 2)[1:] + b'\x00\x00\x00\x00'
        audio_tag = audio_tag_header + audio_frame
        audio_tags += audio_tag + struct.pack('>L', len(audio_tag) + 1)
        total_tags_length += len(audio_tag) + 4

    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    flv_file_path = os.path.join(output_path, 'complex_video_with_accessibility_features.flv')
    with open(flv_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tags)
        f.write(audio_tags)
        
        # Update the filesize in the metadata
        f.seek(0, os.SEEK_END)
        filesize = f.tell()
        f.seek(13)  # Seek to the position right after FLV header and previous tag size
        f.write(serialize_amf0_object({'onMetaData': {**on_meta_data, 'filesize': filesize}}))

    print('Complex FLV file with advanced features created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_complex_features(output_dir)