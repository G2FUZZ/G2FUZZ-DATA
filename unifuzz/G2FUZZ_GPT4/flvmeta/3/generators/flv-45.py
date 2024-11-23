import os
import struct
import json

def create_flv_header(has_audio=True, has_video=True):
    """Create the FLV file header."""
    type_flags = (has_audio << 2) | has_video
    header = struct.pack('>3sBBI', b'FLV', 1, type_flags, 9)
    return header + b'\x00\x00\x00\x00'  # PreviousTagSize0

def create_tag(tag_type, data, timestamp=0):
    """Create an FLV tag."""
    data_size = len(data)
    stream_id = 0
    tag_header = struct.pack('>BIII', tag_type, data_size, timestamp, stream_id)
    return tag_header + data

def encode_amf_string(s):
    """Encode a string in AMF0 format."""
    return struct.pack('>H', len(s)) + s.encode('utf-8')

def encode_amf_double(d):
    """Encode a double in AMF0 format."""
    return struct.pack('>Bd', 0, d)

def create_metadata_tag(metadata):
    """Create a script data tag for metadata encoded in AMF0 format."""
    script_data = b'\x02' + encode_amf_string('onMetaData') + b'\x08' + struct.pack('>L', len(metadata))

    for key, value in metadata.items():
        script_data += encode_amf_string(key)
        if isinstance(value, str):
            script_data += b'\x02' + encode_amf_string(value)
        elif isinstance(value, (int, float)):
            script_data += encode_amf_double(value)

    script_data += b'\x00\x00\x09'  # AMF0 Object End Marker
    return create_tag(18, script_data)

def create_video_tag(frame_data, timestamp, is_keyframe=True, codec_id=7):
    """Create a video tag."""
    frame_type = 1 if is_keyframe else 2
    video_data = struct.pack('>B', (frame_type << 4) | codec_id) + frame_data
    return create_tag(9, video_data, timestamp)

def create_audio_tag(audio_data, timestamp, sound_format=2):
    """Create an audio tag with variable formats."""
    sound_rate = 3  # 44 kHz
    sound_size = 1  # 16-bit samples
    sound_type = 1  # Stereo sound
    audio_header = struct.pack('>B', (sound_format << 4) | (sound_rate << 2) | (sound_size << 1) | sound_type)
    return create_tag(8, audio_header + audio_data, timestamp)

def write_flv_file(output_path, tags):
    """Write the FLV content to a file."""
    with open(output_path, 'wb') as f:
        f.write(create_flv_header())
        for tag in tags:
            f.write(tag)
            f.write(struct.pack('>I', len(tag)))  # PreviousTagSize

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "more_complex_example.flv")

# Example frame and audio data (placeholders for actual data)
frame_data = b'\x00' * 300  # Placeholder for video frame data
audio_data = b'\x00' * 100  # Placeholder for audio data

# Metadata for the FLV file
metadata = {
    'duration': 100,
    'width': 640,
    'height': 480,
    'videocodecid': 7,  # For AVC
    'audiocodecid': 10,  # For AAC
    'audiochannels': 2,
}

# Creating multiple tags for a more complex structure
tags = [
    create_metadata_tag(metadata),
    create_video_tag(frame_data, timestamp=0),
    create_audio_tag(audio_data, timestamp=1000, sound_format=10),  # AAC format
    create_video_tag(frame_data, timestamp=2000, is_keyframe=False, codec_id=4),  # VP6 codec
    create_audio_tag(audio_data, timestamp=3000, sound_format=2),  # MP3 format
]

write_flv_file(output_path, tags)

print(f"Generated more complex FLV file at: {output_path}")