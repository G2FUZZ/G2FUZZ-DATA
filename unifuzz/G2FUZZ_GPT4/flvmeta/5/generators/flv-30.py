import os
import struct

def serialize_amf0_string(s):
    return struct.pack('>H', len(s)) + s.encode('utf-8')

def serialize_amf0_object(obj):
    content = b''
    for key, value in obj.items():
        content += serialize_amf0_string(key)
        if isinstance(value, str):
            content += b'\x02' + serialize_amf0_string(value)
        elif isinstance(value, bool):
            content += b'\x01' + (b'\x01' if value else b'\x00')
        elif isinstance(value, (int, float)):
            content += b'\x00' + struct.pack('>d', value)
        # You can implement additional types as needed
    content += b'\x00\x00\x09'  # Object end marker
    return content

def create_flv_with_complex_features(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    on_meta_data = {
        'onMetaData': {
            'duration': 0,
            'width': 1920,
            'height': 1080,
            'videodatarate': 1500,
            'framerate': 30,
            'videocodecid': 7,  # AVC
            'audiodatarate': 128,
            'audiosamplerate': 44100,
            'audiosamplesize': 16,
            'stereo': True,
            'audiocodecid': 10,  # AAC
            'filesize': 0,  # to be filled later
            'customKey': 'customValue',  # Custom metadata key
        },
    }
    
    # Serialize the onMetaData object into AMF0 format
    on_meta_data_serialized = b'\x02' + serialize_amf0_string('onMetaData') + b'\x03' + serialize_amf0_object(on_meta_data['onMetaData'])
    
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Placeholder for a video frame (e.g., keyframe)
    video_frame = b'\x09\x00\x00\x0a\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00' + b'\x00\x0a' + b'\x00'*8  # Simplified example
    video_frame_end = struct.pack('>L', len(video_frame) + 1)
    
    # Placeholder for an audio frame
    audio_frame = b'\x08\x00\x00\x0a\x00\x00\x00\x00\x00' + b'\xaf\x01' + b'\x00\x0a' + b'\x00'*8  # Simplified example
    audio_frame_end = struct.pack('>L', len(audio_frame) + 1)
    
    # Calculate total file size and update it in metadata
    total_file_size = len(flv_header) + len(previous_tag_size_0) + len(script_tag_full_length) + len(script_tag_end) + len(video_frame) + len(video_frame_end) + len(audio_frame) + len(audio_frame_end)
    on_meta_data['onMetaData']['filesize'] = total_file_size
    on_meta_data_serialized = b'\x02' + serialize_amf0_string('onMetaData') + b'\x03' + serialize_amf0_object(on_meta_data['onMetaData'])
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_frame)
        f.write(video_frame_end)
        f.write(audio_frame)
        f.write(audio_frame_end)
    
    print('FLV file with complex features created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_complex_features(output_dir)