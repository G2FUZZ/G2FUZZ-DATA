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
    on_meta_data = {
        'onMetaData': {
            'duration': 5,
            'width': 640,
            'height': 360,
            'videodatarate': 500,
            'framerate': 24,
            'videocodecid': 7,  # AVC
            'audiodatarate': 128,
            'audiosamplerate': 44100,
            'audiosamplesize': 16,
            'stereo': True,
            'audiocodecid': 10,  # AAC
            'filesize': 0,  # To be filled later
        }
    }
    
    # Placeholder for onMetaData serialization (for demonstration purposes)
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'

    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    # Video tag (sample frame)
    video_tag_start = b'\x09\x00\x00\x0A\x00\x00\x00\x00\x00'  # TagType 9 for video, 10 bytes of data, StreamID 0
    video_frame_type = 1  # key frame
    codec_id = 7  # AVC
    video_data = b'\x00\x00\x00' + bytes(random.getrandbits(8) for _ in range(10))  # AVC sequence header + sample data
    video_tag_data = bytes([((video_frame_type << 4) | codec_id)]) + video_data
    video_tag_length = len(video_tag_data)
    video_tag_full_length = video_tag_start + struct.pack('>L', video_tag_length)[:-1] + video_tag_data
    video_tag_end = struct.pack('>L', len(video_tag_full_length) + 1)

    # Audio tag (sample frame)
    audio_tag_start = b'\x08\x00\x00\x0A\x00\x00\x00\x00\x00'  # TagType 8 for audio, 10 bytes of data, StreamID 0
    sound_format = 10  # AAC
    sound_rate = 3  # 44 kHz
    sound_size = 1  # 16-bit samples
    sound_type = 1  # Stereo
    audio_data = b'\x00' + bytes(random.getrandbits(8) for _ in range(10))  # AAC sequence header + sample data
    audio_tag_data = bytes([((sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)]) + audio_data
    audio_tag_length = len(audio_tag_data)
    audio_tag_full_length = audio_tag_start + struct.pack('>L', audio_tag_length)[:-1] + audio_tag_data
    audio_tag_end = struct.pack('>L', len(audio_tag_full_length) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag_full_length)
        f.write(video_tag_end)
        f.write(audio_tag_full_length)
        f.write(audio_tag_end)

    print('Complex FLV file created with video and audio frames.')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir)