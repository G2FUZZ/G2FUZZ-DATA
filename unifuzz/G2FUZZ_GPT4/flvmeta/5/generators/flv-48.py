import os
import struct

def create_complex_flv(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x11\x11\x11\x11'  # Simplified placeholder for serialized onMetaData
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Video tag - AVC sequence header (simplified placeholder)
    video_tag_start = b'\x09\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'  # TagType 9 for video, DataSize 13 bytes for this placeholder
    video_data = b'\x17\x00\x00\x00\x00' + b'\x01\x64\x00\x1f\xff\xe1\x00\x19\x67\x64\x00\x1f\xac\xd9\x40\x78\x02\x27\xe5\xc0\x44\x00\x00\x03\x00\x04\x00\x00\x03\x00\xca\x3c\x48\x96\x58'
    video_tag_end = struct.pack('>L', len(video_data) + 11)  # Video tag size

    # Audio tag - AAC sequence header (simplified placeholder)
    audio_tag_start = b'\x08\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00'  # TagType 8 for audio, DataSize 5 bytes for this placeholder
    audio_data = b'\xaf\x00\x01\x4d\x40'
    audio_tag_end = struct.pack('>L', len(audio_data) + 11)  # Audio tag size

    # Prepare the output file path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file_path = os.path.join(output_path, 'complex_video_with_audio.flv')
    
    # Write the FLV file
    with open(output_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag_start + video_data)
        f.write(video_tag_end)
        f.write(audio_tag_start + audio_data)
        f.write(audio_tag_end)
    
    print('Complex FLV file with video and audio streams created.')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir)