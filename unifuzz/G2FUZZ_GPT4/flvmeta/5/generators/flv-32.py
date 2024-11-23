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
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'  # Placeholder for serialized onMetaData
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)

    # Generate a random sequence of video and audio tags
    def generate_media_tags(count):
        tags = []
        for i in range(count):
            # Randomly choose between audio (8) and video (9) tag types
            tag_type = random.choice([8, 9])
            data_length = random.randint(100, 1000)  # Random data length
            timestamp = i * 1000  # Incrementing timestamp
            stream_id = 0  # Default stream ID
            data = os.urandom(data_length)  # Random binary data as placeholder
            tag_header = struct.pack('>B', tag_type) + struct.pack('>L', data_length)[1:] + struct.pack('>L', timestamp)[:3] + b'\x00' + struct.pack('>L', stream_id)[1:]
            tag_data = tag_header + data
            tag_size = struct.pack('>L', len(tag_data) + 1)
            tags.append((tag_data, tag_size))
        return tags

    # Generate a sequence of 10 video and audio tags as an example
    media_tags = generate_media_tags(10)

    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)

        # Write the generated media tags
        for tag_data, tag_size in media_tags:
            f.write(tag_data)
            f.write(tag_size)
    
    print('Complex FLV file created with multiple video and audio tags.')

# Specify the output directory
output_dir = './tmp/'
create_complex_flv(output_dir)