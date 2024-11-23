import os
import struct
import random
import json

def create_complex_flv(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'

    # Placeholder for file content
    file_content = bytearray()

    # Script tag - onMetaData
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
    
    # Serialize the onMetaData tag
    def serialize_script_data(data):
        # This is a very simplified serialization
        encoded_data = json.dumps(data).encode()
        script_tag_data = b'\x02' + struct.pack('>H', len('onMetaData')) + b'onMetaData'
        script_tag_data += b'\x08' + struct.pack('>L', len(data)) + encoded_data
        return script_tag_data
    
    # Generate video and audio tags
    def generate_media_tags(frames):
        media_tags = bytearray()
        for frame in frames:
            if frame['type'] == 'video':
                # Generate a video tag
                video_tag_start = b'\x09\x00\x00\x0A\x00\x00\x00\x00\x00'  # TagType 9 for video
                video_frame_type = random.choice([1, 2])  # Keyframe or interframe
                codec_id = 7  # AVC
                video_data = b'\x00\x00\x00' + bytes(random.getrandbits(8) for _ in range(10))  # AVC sequence header + sample data
                video_tag_data = bytes([((video_frame_type << 4) | codec_id)]) + video_data
                video_tag_length = len(video_tag_data)
                video_tag_full_length = video_tag_start + struct.pack('>L', video_tag_length)[:-1] + video_tag_data
                video_tag_end = struct.pack('>L', len(video_tag_full_length) + 1)
                media_tags += video_tag_full_length + video_tag_end
            elif frame['type'] == 'audio':
                # Generate an audio tag
                audio_tag_start = b'\x08\x00\x00\x0A\x00\x00\x00\x00\x00'  # TagType 8 for audio
                sound_format = 10  # AAC
                sound_rate = 3  # 44 kHz
                sound_size = 1  # 16-bit samples
                sound_type = 1  # Stereo
                audio_data = b'\x00' + bytes(random.getrandbits(8) for _ in range(10))  # AAC sequence header + sample data
                audio_tag_data = bytes([((sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)]) + audio_data
                audio_tag_length = len(audio_tag_data)
                audio_tag_full_length = audio_tag_start + struct.pack('>L', audio_tag_length)[:-1] + audio_tag_data
                audio_tag_end = struct.pack('>L', len(audio_tag_full_length) + 1)
                media_tags += audio_tag_full_length + audio_tag_end
        return media_tags
    
    # Create sample frames (for this example, 5 video and 5 audio frames)
    sample_frames = [{'type': 'video'} for _ in range(5)] + [{'type': 'audio'} for _ in range(5)]
    media_tags = generate_media_tags(sample_frames)
    
    # Update onMetaData
    on_meta_data['onMetaData']['duration'] = 5  # Assuming 5 seconds for demo
    on_meta_data_serialized = serialize_script_data(on_meta_data)

    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    # Assemble the file content
    file_content += flv_header
    file_content += previous_tag_size_0
    file_content += script_tag_full_length
    file_content += script_tag_end
    file_content += media_tags

    # Update filesize in onMetaData
    on_meta_data['onMetaData']['filesize'] = len(file_content)
    updated_on_meta_data_serialized = serialize_script_data(on_meta_data)

    # Update the script tag with the new filesize
    updated_script_data_length = len(updated_on_meta_data_serialized)
    updated_script_tag_full_length = script_tag_start + struct.pack('>L', updated_script_data_length)[:-1] + updated_on_meta_data_serialized
    updated_script_tag_end = struct.pack('>L', len(updated_script_tag_full_length) + 1)
    
    # Reassemble the file content with updated filesize
    file_content = file_content[:len(flv_header) + len(previous_tag_size_0)] + updated_script_tag_full_length + updated_script_tag_end + file_content[len(file_content) - len(media_tags):]

    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(file_content)

    print('Complex FLV file created with multiple video and audio frames and updated onMetaData.')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir)