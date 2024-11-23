import os
import random

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Path to the complex FLV file to be created
    flv_file_path = './tmp/complex_video_stream.flv'

    # FLV file header for a video file without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')

    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')

    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)

        # Write multiple metadata tags with simulated data
        for i in range(1, 4):  # Creating three metadata tags for demonstration
            metadata_content = f"Example metadata {i}: Demonstrating complex structures in FLV files."
            metadata_length = len(metadata_content)
            data_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
            flv_file.write(data_tag)
            flv_file.write(len(data_tag).to_bytes(4, byteorder='big'))

        # Write video frame tags
        for i in range(1, 5):  # Creating four video frames for demonstration
            # Simulating a small video frame payload
            frame_payload = bytes([random.randint(0, 255) for _ in range(50)])  # Random payload for demonstration
            frame_length = len(frame_payload)
            timestamp = i * 1000  # Incrementing timestamps for each frame

            # Constructing the video frame tag
            video_frame_tag = bytes([9]) + frame_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(3, byteorder='big') + bytes([0]) + (0).to_bytes(3, byteorder='big') + frame_payload
            flv_file.write(video_frame_tag)
            flv_file.write(len(video_frame_tag).to_bytes(4, byteorder='big'))

    print(f"Complex FLV file created at {flv_file_path}")

create_complex_flv_file()