import os
import struct
import random

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

def create_flv_with_complex_features(output_path, video_duration=10, framerate=30, width=640, height=480):
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'

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
        'filesize': 0,
        'encoder': 'Custom FLV Generator v2',
        'hasKeyframes': True,
        'hasVideo': True,
        'hasAudio': True,
        'hasMetadata': True,
        'canSeekToEnd': True,
        'customMetadataEntry': 'ExampleValue'  # New custom metadata entry
    }

    on_meta_data_serialized = b'\x12' + serialize_amf0_object({'onMetaData': on_meta_data})
    script_data_length = len(on_meta_data_serialized) - 1
    script_tag_full_length = struct.pack('>L', script_data_length)[1:] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    video_tags = b''
    audio_tags = b''
    keyframe_indices = []

    for i in range(video_duration * framerate):
        # Variable frame sizes
        frame_size = random.randint(50, 150)
        frame_data = random.randbytes(frame_size)

        # Mark every 30th frame as a keyframe
        frame_type = b'\x17' if i % 30 == 0 else b'\x27'
        if frame_type == b'\x17': keyframe_indices.append(len(video_tags) + 11)  # 11 bytes FLV tag header

        video_tag = frame_type + struct.pack('>L', len(frame_data) + 5)[1:] + b'\x00\x00\x00\x00' + frame_data
        video_tags += video_tag + struct.pack('>L', len(video_tag) + 1)

        if i % (framerate // 30) == 0:
            sample_size = random.randint(10, 30)
            sample_data = random.randbytes(sample_size)
            audio_tag = b'\x08' + struct.pack('>L', len(sample_data) + 2)[1:] + b'\x00\x00\x00\x00' + sample_data
            audio_tags += audio_tag + struct.pack('>L', len(audio_tag) + 1)

    total_file_size = (len(flv_header) + len(previous_tag_size_0) + len(script_tag_full_length) + len(script_tag_end) +
                       len(video_tags) + len(audio_tags))
    on_meta_data['filesize'] = total_file_size
    on_meta_data['keyframes'] = {
        'filepositions': keyframe_indices,
        'times': [i/framerate for i in range(video_duration * framerate) if i % 30 == 0]
    }

    updated_meta_data_serialized = b'\x12' + serialize_amf0_object({'onMetaData': on_meta_data})
    updated_script_data_length = len(updated_meta_data_serialized) - 1
    updated_script_tag_full_length = struct.pack('>L', updated_script_data_length)[1:] + updated_meta_data_serialized
    updated_script_tag_end = struct.pack('>L', len(updated_script_tag_full_length) + 1)

    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    try:
        with open(output_path, 'wb') as f:
            f.write(flv_header)
            f.write(previous_tag_size_0)
            f.write(updated_script_tag_full_length)
            f.write(updated_script_tag_end)
            f.write(video_tags)
            f.write(audio_tags)
        print('Complex FLV file with advanced features and custom metadata created.')
    except IOError as e:
        print(f"Error writing file: {e}")

output_file_path = './tmp/complex_video_with_advanced_features_v2.flv'
create_flv_with_complex_features(output_file_path)