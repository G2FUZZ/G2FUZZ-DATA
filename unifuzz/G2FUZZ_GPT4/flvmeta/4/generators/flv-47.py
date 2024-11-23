import os
import struct
from random import randint

def create_script_data_object(name, value, value_type='string'):
    name_data = struct.pack('>B', 2) + struct.pack('>H', len(name)) + name.encode('utf-8')
    if value_type == 'string':
        value_data = struct.pack('>B', 2) + struct.pack('>H', len(value)) + value.encode('utf-8')
    elif value_type == 'number':
        value_data = struct.pack('>B', 0) + struct.pack('>d', value)
    elif value_type == 'boolean':
        value_data = struct.pack('>B', 1) + struct.pack('>B', value)
    else:
        raise ValueError("Unsupported value type")
    return name_data + value_data

def create_on_meta_data_tag(video_duration, video_width, video_height, video_codec_id=7, audio_codec_id=10):
    tag_type = b'\x12'
    on_meta_data_name = struct.pack('>B', 2) + struct.pack('>H', len("onMetaData")) + b"onMetaData"
    properties = [
        create_script_data_object("duration", video_duration, value_type='number'),
        create_script_data_object("width", video_width, value_type='number'),
        create_script_data_object("height", video_height, value_type='number'),
        create_script_data_object("videocodecid", video_codec_id, value_type='number'),
        create_script_data_object("audiocodecid", audio_codec_id, value_type='number'),
    ]
    object_end_marker = struct.pack('>B', 9)
    properties_data = b''.join(properties) + object_end_marker
    data_size = len(on_meta_data_name) + len(properties_data)
    data_size_bytes = struct.pack('>I', data_size)[1:]
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp + stream_id + on_meta_data_name + properties_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

def create_audio_frame_tag(audio_data, timestamp=0):
    tag_type = b'\x08'
    data_size_bytes = struct.pack('>I', len(audio_data))[1:]
    timestamp_bytes = struct.pack('>I', timestamp)[1:] + struct.pack('>B', timestamp >> 24)
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp_bytes + stream_id + audio_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

def create_video_frame_tag(frame_data, keyframe=False, timestamp=0):
    tag_type = b'\x09'
    frame_info = b'\x17' if keyframe else b'\x27'
    data_size_bytes = struct.pack('>I', len(frame_data) + 1)[1:]
    timestamp_bytes = struct.pack('>I', timestamp)[1:] + struct.pack('>B', timestamp >> 24)
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp_bytes + stream_id + frame_info + frame_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

def create_complex_flv_file(file_path, video_frames_count=10, video_frame_length=1000, audio_frames_count=5, audio_frame_length=500):
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    flv_content = [flv_header, previous_tag_size_0]
    
    on_meta_data_tag = create_on_meta_data_tag(video_duration=video_frames_count * 2, video_width=1920, video_height=1080)
    flv_content.append(on_meta_data_tag)
    
    for i in range(video_frames_count):
        frame_data = os.urandom(video_frame_length)
        timestamp = i * 2000
        keyframe = (i % 5 == 0)
        video_frame_tag = create_video_frame_tag(frame_data, keyframe=keyframe, timestamp=timestamp)
        flv_content.append(video_frame_tag)
    
    for j in range(audio_frames_count):
        audio_data = os.urandom(audio_frame_length)
        timestamp = j * 4000
        audio_frame_tag = create_audio_frame_tag(audio_data, timestamp=timestamp)
        flv_content.append(audio_frame_tag)
    
    final_flv_content = b''.join(flv_content)
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(final_flv_content)

flv_file_path = './tmp/advanced_example.flv'
create_complex_flv_file(flv_file_path, video_frames_count=5, audio_frames_count=3)

print(f'Advanced FLV file with multiple video frames, multiple audio frames, keyframes, and onMetaData created at: {flv_file_path}')