import os
import struct
import random

def create_complex_flv(output_path, num_frames=10):
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Placeholder for onMetaData, actual values will be filled later
    on_meta_data = {
        'onMetaData': {
            'duration': 0,  # To be updated
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
            'filesize': 0,  # To be updated
        }
    }
    
    # Placeholder for onMetaData serialization (for demonstration purposes)
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'  # Simplified serialization
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    video_tags = []
    audio_tags = []

    # Generate video and audio frames
    for i in range(num_frames):
        # Simulate changing frame sizes and data
        frame_size = random.randint(5, 15)
        video_data = b'\x00\x00\x00' + bytes(random.getrandbits(8) for _ in range(frame_size))
        video_frame_type = 1  # key frame for simplicity
        codec_id = 7  # AVC
        video_tag_data = bytes([((video_frame_type << 4) | codec_id)]) + video_data
        video_tag_start = b'\x09' + struct.pack('>L', len(video_tag_data))[1:] + b'\x00\x00\x00\x00\x00'
        video_tag_full_length = video_tag_start + video_tag_data
        video_tag_end = struct.pack('>L', len(video_tag_full_length) + 1)
        video_tags.append((video_tag_full_length, video_tag_end))

        audio_data = b'\x00' + bytes(random.getrandbits(8) for _ in range(frame_size))
        sound_format = 10  # AAC
        sound_rate = 3  # 44 kHz
        sound_size = 1  # 16-bit samples
        sound_type = 1  # Stereo
        audio_tag_data = bytes([((sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)]) + audio_data
        audio_tag_start = b'\x08' + struct.pack('>L', len(audio_tag_data))[1:] + b'\x00\x00\x00\x00\x00'
        audio_tag_full_length = audio_tag_start + audio_tag_data
        audio_tag_end = struct.pack('>L', len(audio_tag_full_length) + 1)
        audio_tags.append((audio_tag_full_length, audio_tag_end))

    # Update onMetaData fields
    on_meta_data['onMetaData']['duration'] = num_frames / on_meta_data['onMetaData']['framerate']
    
    # Update onMetaData serialization (simplified for demonstration)
    # Note: Proper serialization is necessary for a fully functional FLV file.
    # This example uses a simplified approach for demonstration purposes only.
    
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    flv_file_path = os.path.join(output_path, 'complex_video.flv')
    with open(flv_file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        for video_tag, video_end in video_tags:
            f.write(video_tag)
            f.write(video_end)
        for audio_tag, audio_end in audio_tags:
            f.write(audio_tag)
            f.write(audio_end)

        # Update filesize in metadata (simplified approach)
        on_meta_data['onMetaData']['filesize'] = f.tell()
    
    print(f'Complex FLV file created with {num_frames} video and audio frames at {flv_file_path}')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir, num_frames=10)