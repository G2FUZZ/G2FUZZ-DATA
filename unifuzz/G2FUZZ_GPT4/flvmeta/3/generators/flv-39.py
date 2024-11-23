import os
import struct

def create_flv_file(output_path):
    flv_header = bytes([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # TypeFlags (audio + video)
        0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    ])

    # PreviousTagSize0
    previous_tag_size = bytes([0x00, 0x00, 0x00, 0x00])

    # onMetaData tag (AMF0 Data)
    on_metadata = bytearray()
    on_metadata.extend(b'\x12')  # Script data tag
    on_metadata_size_pos = len(on_metadata)
    on_metadata.extend(b'\x00\x00\x00')  # Placeholder for data size
    on_metadata.extend(b'\x00\x00\x00\x00')  # Timestamp
    on_metadata.extend(b'\x00\x00\x00')  # StreamID
    on_metadata.extend(construct_on_metadata())  # Actual metadata content
    update_data_size(on_metadata, on_metadata_size_pos)
    
    # Sample video and audio tags
    video_tags = construct_video_tags()
    audio_tags = construct_audio_tags()

    # Write the FLV content to a file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size)
        f.write(on_metadata)
        for tag in video_tags + audio_tags:
            f.write(tag)

def construct_on_metadata():
    """Constructs onMetaData tag content."""
    metadata = bytearray()
    metadata.extend(b'\x02')
    metadata.extend(struct.pack('>H', len("onMetaData")))
    metadata.extend(b'onMetaData')
    metadata.extend(b'\x08')
    metadata.extend(struct.pack('>I', 3))
    metadata.extend(encode_amf0_data("duration", 120.0))
    metadata.extend(encode_amf0_data("width", 640))
    metadata.extend(encode_amf0_data("height", 360))
    metadata.extend(b'\x00\x00\x09')
    return metadata

def encode_amf0_data(key, value):
    data = bytearray()
    data.extend(struct.pack('>H', len(key)))
    data.extend(key.encode('utf-8'))
    if isinstance(value, float):
        data.extend(b'\x00')
        data.extend(struct.pack('>d', value))
    elif isinstance(value, int):
        data.extend(b'\x00')
        data.extend(struct.pack('>d', float(value)))
    return data

def construct_video_tags():
    tags = []
    for i in range(2):
        tag = bytearray()
        tag.extend(b'\x09')
        tag.extend(b'\x00\x00\x00')
        timestamp = i * 1000
        tag.extend(struct.pack('>I', timestamp)[:3])
        tag.extend(b'\x00')
        tag.extend(b'\x00\x00\x00')
        tag.extend(b'\x00' * 10)
        update_data_size(tag, 1)
        tags.append(tag)
    return tags

def construct_audio_tags():
    tags = []
    for i in range(2):
        tag = bytearray()
        tag.extend(b'\x08')
        tag.extend(b'\x00\x00\x00')
        timestamp = 500 + i * 1000
        tag.extend(struct.pack('>I', timestamp)[:3])
        tag.extend(b'\x00')
        tag.extend(b'\x00\x00\x00')
        tag.extend(b'\x00' * 5)
        update_data_size(tag, 1)
        tags.append(tag)
    return tags

def update_data_size(data, pos):
    size = len(data) - pos - 10
    struct.pack_into('>I', data, pos, size)

output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "complex_example.flv")
create_flv_file(output_path)

print(f"Generated complex FLV file at: {output_path}")