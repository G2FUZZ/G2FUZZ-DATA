import struct
import os

def create_flv_file_with_complex_features(output_path):
    # FLV file header
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    # PreviousTagSize0 following the FLV header
    previous_tag_size0 = bytearray([0x00, 0x00, 0x00, 0x00])

    # Metadata tag (script data tag for onMetaData event)
    meta_tag_data = create_metadata_tag()
    previous_tag_size_meta = len(meta_tag_data)
    previous_tag_size_meta = struct.pack('>I', previous_tag_size_meta)

    # Video tag (a simple example)
    video_tag_data = create_video_tag()
    previous_tag_size_video = len(video_tag_data)
    previous_tag_size_video = struct.pack('>I', previous_tag_size_video)

    # Audio tag (a simple example)
    audio_tag_data = create_audio_tag()
    previous_tag_size_audio = len(audio_tag_data)
    previous_tag_size_audio = struct.pack('>I', previous_tag_size_audio)

    # Combine everything
    flv_content = flv_header + previous_tag_size0 + meta_tag_data + previous_tag_size_meta + video_tag_data + previous_tag_size_video + audio_tag_data + previous_tag_size_audio

    # Write the bytes to an FLV file
    with open(output_path, 'wb') as flv_file:
        flv_file.write(flv_content)

def create_metadata_tag():
    # Placeholder metadata in AMF0 format (very simplified)
    # Actual metadata should include details like width, height, duration, etc.
    metadata = b'\x02\x00\x0aonMetaData\x08\x00\x00\x00\x00'
    tag_type = 0x12  # Script data
    data_size = len(metadata)
    timestamp = 0
    stream_id = 0
    tag_header = struct.pack('>BIII', tag_type, data_size, timestamp, stream_id)
    return tag_header + metadata

def create_video_tag():
    # Placeholder video data (a simple H.264 keyframe example)
    # Actual video data would be encoded video frames
    video_data = b'\x17\x00\x00\x00\x00\x00\x01\x23\x45'
    tag_type = 0x09  # Video tag
    data_size = len(video_data)
    timestamp = 40  # Example timestamp
    stream_id = 0
    tag_header = struct.pack('>BIII', tag_type, data_size, timestamp, stream_id)
    return tag_header + video_data

def create_audio_tag():
    # Placeholder audio data (a simple AAC sequence header)
    # Actual audio data would be encoded audio frames
    audio_data = b'\xAF\x00\x12\x34'
    tag_type = 0x08  # Audio tag
    data_size = len(audio_data)
    timestamp = 20  # Example timestamp
    stream_id = 0
    tag_header = struct.pack('>BIII', tag_type, data_size, timestamp, stream_id)
    return tag_header + audio_data

# Specify output path
output_path = './tmp/complex_sample.flv'

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the FLV file with complex features
create_flv_file_with_complex_features(output_path)