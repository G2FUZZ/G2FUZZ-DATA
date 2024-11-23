import os
import struct
import time

def create_complex_flv_file(file_path, metadata, frame_rate, video_frame_count, audio_sample_count):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Enhanced metadata with frame rate and more
    metadata['frameRate'] = frame_rate
    metadata['videoFrameCount'] = video_frame_count
    metadata['audioSampleCount'] = audio_sample_count

    script_data = construct_script_data(metadata)

    # Dummy video and audio frame data (for demonstration purposes)
    video_frame_data = b'\x00\x00\x00\x00' * video_frame_count # Simplified video frame data
    audio_frame_data = b'\x01\x01\x01\x01' * audio_sample_count # Simplified audio frame data

    video_tag = construct_video_tag(video_frame_data)
    audio_tag = construct_audio_tag(audio_frame_data)

    with open(file_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_data)
        f.write(video_tag)
        f.write(audio_tag)
        # PreviousTagSize for script, video, and audio tags
        f.write(struct.pack('>L', len(script_data)))
        f.write(struct.pack('>L', len(video_tag)))
        f.write(struct.pack('>L', len(audio_tag)))

def construct_script_data(metadata):
    script_data = b'\x12\x00\x01\x00\x00\x00\x00\x00\x00\x00'  # Script Tag Header Placeholder
    script_data_body = b'\x02\x00\x0AonMetaData' + b'\x08' + struct.pack('>L', len(metadata))
    for key, value in metadata.items():
        script_data_body += struct.pack('>H', len(key)) + key.encode('utf-8')
        if isinstance(value, str):
            script_data_body += b'\x02' + struct.pack('>H', len(value)) + value.encode('utf-8')
        elif isinstance(value, (int, float)):
            script_data_body += b'\x00' + struct.pack('>d', value)
        elif isinstance(value, bool):
            script_data_body += b'\x01' + struct.pack('>?', value)
    script_data_body += b'\x00\x00\x09'  # Object end marker
    data_size = len(script_data_body)
    script_data = b'\x12' + struct.pack('>L', data_size << 8) + b'\x00\x00\x00\x00\x00' + script_data_body
    return script_data

def construct_video_tag(data):
    # Simplified video tag construction
    timestamp = int(time.time())
    video_data_header = b'\x09' + struct.pack('>L', len(data) << 8 | timestamp) + b'\x00\x00\x00\x00'
    return video_data_header + data

def construct_audio_tag(data):
    # Simplified audio tag construction
    timestamp = int(time.time())
    audio_data_header = b'\x08' + struct.pack('>L', len(data) << 8 | timestamp) + b'\x00\x00\x00\x00'
    return audio_data_header + data

if __name__ == '__main__':
    file_path = './tmp/complex_sample.flv'
    metadata = {
        'duration': 0,
        'width': 640,
        'height': 480,
        'videocodecid': 7,
        'audiocodecid': 10,
        'canSeekToEnd': True,
        'creator': 'Advanced FLV Generator',
        'hasVideo': True,
        'hasAudio': True,
    }
    frame_rate = 30.0
    video_frame_count = 5
    audio_sample_count = 5
    create_complex_flv_file(file_path, metadata, frame_rate, video_frame_count, audio_sample_count)