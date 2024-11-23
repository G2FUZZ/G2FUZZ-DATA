import os
import time

def create_complex_flv(output_path):
    # FLV file header for a video file with no audio
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x01,  # Video tags only, no audio
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    # Initialize the FLV body with the first previous tag size
    flv_body = bytearray([0x00, 0x00, 0x00, 0x00])

    # Function to add a video tag to the FLV body
    def add_video_tag(body, timestamp, is_keyframe=True):
        # Tag type 9 = video
        tag_type = 0x09
        # Example data size and data (simplified for demonstration)
        data_size = 0x2A if is_keyframe else 0x1A  # Keyframes larger, interframes smaller
        timestamp_bytes = timestamp.to_bytes(3, byteorder='big') + (timestamp // 16777216).to_bytes(1, byteorder='big')
        stream_id = b'\x00\x00\x00'  # StreamID always 0
        video_data = bytearray([
            0x17 if is_keyframe else 0x27,  # Frame type and codec (AVC)
            0x01,  # AVC NALU
            0x00, 0x00, 0x00,  # Composition time
            # The rest would be the NALU data
        ])
        video_data.extend(os.urandom(data_size - 5))  # Generate random video data for simplicity

        # Assemble the tag
        data_length_bytes = data_size.to_bytes(3, byteorder='big')
        tag_header = bytearray([tag_type]) + data_length_bytes + timestamp_bytes + stream_id
        tag_data = video_data

        # Append the tag to the body
        body.extend(tag_header)
        body.extend(tag_data)

        # Append the previous tag size (tag header + data)
        previous_tag_size = (len(tag_header) + len(tag_data)).to_bytes(4, byteorder='big')
        body.extend(previous_tag_size)

    # Simulate 30fps video for 2 seconds (60 frames total)
    for frame_number in range(60):
        timestamp = int((frame_number / 30) * 1000)  # Convert frame number to milliseconds
        is_keyframe = frame_number % 30 == 0  # First frame or every 30 frames is a keyframe
        add_video_tag(flv_body, timestamp, is_keyframe)

    # Write the header and body to the file
    output_file = os.path.join(output_path, "complex_example.flv")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(output_file, "wb") as flv_file:
        flv_file.write(flv_header)
        flv_file.write(flv_body)

    print(f"FLV file created at {output_file}")

# Use the function to create a more complex FLV file
create_complex_flv('./tmp/')