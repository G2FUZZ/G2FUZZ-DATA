import os
import struct

def create_flv_with_complex_structure(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'  # Simplified serialized onMetaData
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Video tag - simplified example
    video_tag_start = b'\x09\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 9 for video, StreamID 0
    video_data = b'\x00\x00\x00\x00'  # Placeholder for video data
    video_data_length = len(video_data)
    video_tag_full_length = video_tag_start + struct.pack('>L', video_data_length)[:-1] + video_data
    video_tag_end = struct.pack('>L', len(video_tag_full_length) + 1)
    
    # Audio tag - simplified example
    audio_tag_start = b'\x08\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 8 for audio, StreamID 0
    audio_data = b'\x00\x00\x00\x00'  # Placeholder for audio data
    audio_data_length = len(audio_data)
    audio_tag_full_length = audio_tag_start + struct.pack('>L', audio_data_length)[:-1] + audio_data
    audio_tag_end = struct.pack('>L', len(audio_tag_full_length) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag_full_length)
        f.write(video_tag_end)
        f.write(audio_tag_full_length)
        f.write(audio_tag_end)
    
    print('FLV file with complex structure including script, video, and audio tags created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_complex_structure(output_dir)