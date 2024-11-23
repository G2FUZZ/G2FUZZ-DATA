import os
import struct
import random
import json

def construct_tag(tag_type, data, timestamp):
    """
    Constructs a FLV tag.
    
    :param tag_type: Integer, the type of the tag (8 for audio, 9 for video, 18 for script data)
    :param data: Bytes, the tag data
    :param timestamp: Integer, the timestamp of the tag in milliseconds
    :return: Bytes, the constructed FLV tag
    """
    data_size = len(data)
    timestamp_extended = timestamp >> 24
    timestamp &= 0xFFFFFF
    
    tag_header = struct.pack('>B3B3B1B3B', tag_type, (data_size >> 16) & 0xFF, (data_size >> 8) & 0xFF, data_size & 0xFF, 
                             (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF, timestamp & 0xFF, 
                             timestamp_extended, 0, 0, 0)
    
    flv_tag = tag_header + data
    
    previous_tag_size = struct.pack('>I', len(flv_tag))
    
    return flv_tag + previous_tag_size

def construct_advanced_on_metadata(num_video_frames, num_audio_frames):
    metadata = {
        "duration": num_video_frames * 1.0,
        "width": 1920,
        "height": 1080,
        "videocodecid": 7,
        "audiocodecid": 10,
        "videoframerate": num_video_frames,
        "audiochannels": 2,
        "audiosamplerate": 44100,
    }
    metadata_str = construct_simplified_amf0(metadata)
    return metadata_str

def construct_simplified_amf0(metadata):
    encoded = b''
    for key, value in metadata.items():
        encoded += b'\x02' + struct.pack('>H', len(key)) + key.encode()
        if isinstance(value, str):
            encoded += b'\x02' + struct.pack('>H', len(value)) + value.encode()
        elif isinstance(value, int):
            encoded += b'\x00' + struct.pack('>d', float(value))
        elif isinstance(value, float):
            encoded += b'\x00' + struct.pack('>d', value)
    encoded += b'\x00\x00\x09'
    return encoded

def generate_video_tags(num_frames):
    video_tags = []
    for i in range(1, num_frames + 1):
        if i == 1:
            frame_type = b'\x17'
            avc_record = b'\x00' + b'\x00\x00\x00'
            video_data = avc_record + random_bytes(random.randint(250, 500))
        else:
            frame_type = b'\x27'
            video_data = b'\x01' + b'\x00\x00\x00' + random_bytes(random.randint(250, 500))
        video_tags.append(construct_tag(9, frame_type + video_data, i * 1000))
    return video_tags

def generate_audio_tags(num_frames):
    audio_tags = []
    for i in range(1, num_frames + 1):
        if i == 1:
            sound_format = b'\xAF'
            aac_header = b'\x00'
            audio_data = aac_header + random_bytes(random.randint(100, 200))
        else:
            sound_format = b'\xAF'
            audio_data = b'\x01' + random_bytes(random.randint(100, 200))
        audio_tags.append(construct_tag(8, sound_format + audio_data, i * 500))
    return audio_tags

def random_bytes(size):
    return bytes(random.getrandbits(8) for _ in range(size))

def create_advanced_encrypted_flv_file(file_path, num_video_frames=5, num_audio_frames=10):
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    on_metadata = construct_advanced_on_metadata(num_video_frames, num_audio_frames)
    metadata_tag = construct_tag(18, on_metadata, 0)
    drm_metadata = b'ENCRYPTED\x00'
    drm_tag = construct_tag(18, drm_metadata, 0)
    custom_metadata = b'ADDITIONAL_INFO\x02\x00\x0CExample Data\x00'
    custom_metadata_tag = construct_tag(18, custom_metadata, 0)
    video_tags = generate_video_tags(num_video_frames)
    audio_tags = generate_audio_tags(num_audio_frames)
    flv_content = flv_header + previous_tag_size_0 + metadata_tag + drm_tag + custom_metadata_tag + b''.join(video_tags + audio_tags)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(flv_content)

flv_file_path = './tmp/advanced_encrypted_example.flv'
create_advanced_encrypted_flv_file(flv_file_path, num_video_frames=5, num_audio_frames=10)

print(f'Advanced Encrypted FLV file with additional features and structures created at: {flv_file_path}')