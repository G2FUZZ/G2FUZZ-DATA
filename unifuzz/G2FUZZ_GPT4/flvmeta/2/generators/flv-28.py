import os
import struct

def create_complex_flv(output_path):
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # Video tags and audio
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    # Function to create a script data tag for metadata
    def create_metadata_tag(duration, width, height):
        script_tag = bytearray([0x12])  # Tag type 18 for script data
        metadata = f"duration={duration}\x00width={width}\x00height={height}\x00\x09"
        script_data = bytearray([0x02]) + metadata.encode('utf-8')
        data_length = len(script_data)
        data_length_bytes = struct.pack('>I', data_length)[-3:]
        timestamp = bytearray([0x00, 0x00, 0x00])  # Always 0 for script tags
        stream_id = bytearray([0x00, 0x00, 0x00])  # Always 0
        return script_tag + data_length_bytes + timestamp + stream_id + script_data

    # Function to create a video tag (keyframe)
    def create_video_tag(frame_data, timestamp):
        tag_type = bytearray([0x09])  # Tag type 9 for video
        data_length = len(frame_data)
        data_length_bytes = struct.pack('>I', data_length)[-3:]
        timestamp_bytes = struct.pack('>I', timestamp)[1:] + struct.pack('>I', timestamp)[:1]  # Extended timestamp
        stream_id = bytearray([0x00, 0x00, 0x00])  # Always 0
        return tag_type + data_length_bytes + timestamp_bytes + stream_id + frame_data

    # Define a simple video frame (keyframe)
    def create_keyframe():
        return bytearray([0x17, 0x00, 0x00, 0x00, 0x00]) + b'KEYFRAME'

    # Define a simple inter frame
    def create_inter_frame():
        return bytearray([0x27, 0x00, 0x00, 0x00, 0x00]) + b'INTERFRAME'

    flv_body = bytearray()
    flv_body += create_metadata_tag(100, 320, 240)
    flv_body += create_video_tag(create_keyframe(), 0)
    for timestamp in range(1000, 5000, 1000):
        flv_body += create_video_tag(create_inter_frame(), timestamp)

    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    file_path = os.path.join(output_path, "complex_example.flv")
    with open(file_path, "wb") as flv_file:
        flv_file.write(flv_header)
        prev_tag_size = 0
        for i in range(0, len(flv_body), 11):
            data_length_buffer = b'\x00' + flv_body[i+1:i+4]
            tag_size = struct.unpack_from('>I', data_length_buffer)[0] + 11
            flv_file.write(struct.pack('>I', prev_tag_size))
            flv_file.write(flv_body[i:i+tag_size])
            prev_tag_size = tag_size
        flv_file.write(struct.pack('>I', prev_tag_size))

create_complex_flv('./tmp/')