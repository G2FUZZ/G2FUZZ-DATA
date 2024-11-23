import os
import struct
import random

# Helper functions for serializing AMF0 data types
def serialize_amf0_str(s):
    return struct.pack('>H', len(s)) + s.encode('utf-8')

def serialize_amf0_double(number):
    return b'\x00' + struct.pack('>d', number)

def serialize_amf0_bool(value):
    return b'\x01' + (b'\x01' if value else b'\x00')

def serialize_amf0_object(obj):
    serialized = b''
    for key, value in obj.items():
        serialized += serialize_amf0_str(key)
        if isinstance(value, str):
            serialized += b'\x02' + serialize_amf0_str(value)
        elif isinstance(value, bool):
            serialized += serialize_amf0_bool(value)
        elif isinstance(value, (int, float)):
            serialized += serialize_amf0_double(value)
    return serialized + b'\x00\x00\x09'

# Main function to create FLV with complex features
def create_flv_with_complex_features(output_path, video_duration=10, framerate=30, width=640, height=480):
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Initial onMetaData
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
        'filesize': 0,  # Placeholder
        'encoder': 'Custom FLV Generator',
        'hasKeyframes': True,
        'hasVideo': True,
        'hasAudio': True,
        'hasMetadata': True,
        'canSeekToEnd': True
    }

    # Serialize initial onMetaData
    on_meta_data_serialized = b'\x12' + serialize_amf0_object({'onMetaData': on_meta_data})
    script_data_length = len(on_meta_data_serialized) - 1
    script_tag_full_length = struct.pack('>L', script_data_length)[1:] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    video_data = b'\x00' * 100  # Placeholder for video data
    audio_data = b'\x00' * 100  # Placeholder for audio data

    # Generate multiple video and audio tags to simulate frames and samples
    video_tags = b''
    audio_tags = b''
    for i in range(video_duration * framerate):
        # Simulate video frame
        frame_data = random.randbytes(100)  # Random video frame data
        video_tag = b'\x09' + struct.pack('>L', len(frame_data) + 5)[1:] + b'\x00\x00\x00\x00' + frame_data
        video_tags += video_tag + struct.pack('>L', len(video_tag) + 1)
        
        # Simulate audio sample
        if i % (framerate // 30) == 0:  # Assume audio sample rate is 30 times less than video framerate
            sample_data = random.randbytes(25)  # Random audio sample data
            audio_tag = b'\x08' + struct.pack('>L', len(sample_data) + 2)[1:] + b'\x00\x00\x00\x00' + sample_data
            audio_tags += audio_tag + struct.pack('>L', len(audio_tag) + 1)

    # Calculating final filesize and updating onMetaData
    total_file_size = (len(flv_header) + len(previous_tag_size_0) + len(script_tag_full_length) + len(script_tag_end) +
                       len(video_tags) + len(audio_tags))
    on_meta_data['filesize'] = total_file_size  # Update filesize in metadata

    # Serialize updated onMetaData
    updated_meta_data_serialized = b'\x12' + serialize_amf0_object({'onMetaData': on_meta_data})
    updated_script_data_length = len(updated_meta_data_serialized) - 1
    updated_script_tag_full_length = struct.pack('>L', updated_script_data_length)[1:] + updated_meta_data_serialized
    updated_script_tag_end = struct.pack('>L', len(updated_script_tag_full_length) + 1)

    # Write the FLV file
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(updated_script_tag_full_length)
        f.write(updated_script_tag_end)
        f.write(video_tags)
        f.write(audio_tags)

    print('Complex FLV file with advanced features created.')

# Specify the output file path
output_file_path = './tmp/complex_video_with_advanced_features.flv'
create_flv_with_complex_features(output_file_path)