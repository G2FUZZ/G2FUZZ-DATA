import os
import struct
import random

def create_complex_flv(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    # Placeholder for onMetaData (Similar to above, but with actual content for demonstration)
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'  # Placeholder for serialized onMetaData
    
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Video and Audio Data Placeholders
    # Video tag (TagType 9)
    video_tag_start = b'\x09\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 9 for video, StreamID 0
    video_data = b'\x00' + os.urandom(4000)  # FrameType and CodecID followed by random video data
    video_data_length = len(video_data)
    video_tag_full_length = video_tag_start + struct.pack('>L', video_data_length)[:-1] + video_data
    video_tag_end = struct.pack('>L', len(video_tag_full_length) + 1)
    
    # Audio tag (TagType 8)
    audio_tag_start = b'\x08\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 8 for audio, StreamID 0
    audio_data = b'\xAF' + os.urandom(1000)  # SoundFormat, SoundRate, SoundSize, SoundType followed by random audio data
    audio_data_length = len(audio_data)
    audio_tag_full_length = audio_tag_start + struct.pack('>L', audio_data_length)[:-1] + audio_data
    audio_tag_end = struct.pack('>L', len(audio_tag_full_length) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    flv_file_path = os.path.join(output_path, 'complex_video.flv')
    with open(flv_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag_full_length)
        f.write(video_tag_end)
        f.write(audio_tag_full_length)
        f.write(audio_tag_end)
    
    print(f'Complex FLV file created at {flv_file_path}.')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir)