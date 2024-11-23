import os
import struct

def create_script_data_object(name, value):
    name_data = struct.pack('>B', 2) + struct.pack('>H', len(name)) + name.encode('utf-8')
    value_data = struct.pack('>B', 2) + struct.pack('>H', len(value)) + value.encode('utf-8')
    return name_data + value_data

def create_on_meta_data_tag(video_duration, video_width, video_height):
    tag_type = b'\x12'
    on_meta_data_name = struct.pack('>B', 2) + struct.pack('>H', len("onMetaData")) + b"onMetaData"
    properties = []
    properties.append(create_script_data_object("duration", str(video_duration)))
    properties.append(create_script_data_object("width", str(video_width)))
    properties.append(create_script_data_object("height", str(video_height)))
    object_end_marker = struct.pack('>B', 9)
    properties_data = b''.join(properties) + object_end_marker
    data_size = len(on_meta_data_name) + len(properties_data)
    data_size_bytes = struct.pack('>I', data_size)[1:]
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp + stream_id + on_meta_data_name + properties_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

def create_audio_frame_tag(audio_data):
    tag_type = b'\x08'
    data_size_bytes = struct.pack('>I', len(audio_data))[1:]
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp + stream_id + audio_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

# Assuming a generic implementation for create_video_frame_tag
def create_video_frame_tag(frame_data):
    tag_type = b'\x09'  # Video tag
    data_size_bytes = struct.pack('>I', len(frame_data))[1:]
    timestamp = b'\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
    previous_tag_size = struct.pack('>I', len(tag))
    return tag + previous_tag_size

def create_complex_flv_file(file_path, video_frames_count=10, video_frame_length=1000):
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    flv_content = [flv_header, previous_tag_size_0]
    
    on_meta_data_tag = create_on_meta_data_tag(video_duration=video_frames_count, video_width=1920, video_height=1080)
    flv_content.append(on_meta_data_tag)
    
    for i in range(video_frames_count):
        frame_data = os.urandom(video_frame_length)
        video_frame_tag = create_video_frame_tag(frame_data)
        flv_content.append(video_frame_tag)
    
    audio_data = os.urandom(500)
    audio_frame_tag = create_audio_frame_tag(audio_data)
    flv_content.append(audio_frame_tag)
    
    final_flv_content = b''.join(flv_content)
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(final_flv_content)

flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path, video_frames_count=5)

print(f'Complex FLV file with multiple video frames, an audio frame, and onMetaData created at: {flv_file_path}')