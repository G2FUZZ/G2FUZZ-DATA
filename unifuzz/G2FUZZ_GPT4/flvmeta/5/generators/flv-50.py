import os
from random import randint

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Path to the complex FLV file to be created
    flv_file_path = './tmp/complex_streaming_video.flv'

    # FLV file header for a video file with audio (TypeFlagsAudio is 4 and TypeFlagsVideo is 1)
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')

    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')

    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)

        # Example script data tag for metadata
        metadata_content = "duration\x00?\xf0\x00\x00\x00\x00\x00\x00"  # Example duration metadata
        metadata_tag = construct_script_data_tag(metadata_content)
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))

        # Generating a sequence of video tags to simulate video frames
        for frame_number in range(1, 31):  # Simulate 30 frames
            frame_type = 9 if frame_number % 5 == 0 else 8  # Keyframe every 5 frames, otherwise interframe
            video_data = generate_video_frame_data(frame_type)
            video_tag = construct_video_tag(video_data)
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        print(f"Complex FLV file created at {flv_file_path}")

def construct_script_data_tag(data_content):
    """Constructs a script data tag for FLV metadata."""
    # Script tag type is 18
    tag_type = bytes([18])
    data_length = len(data_content)
    data_stream = tag_type + data_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(data_content, 'latin1')
    return data_stream

def generate_video_frame_data(frame_type):
    """Generates fake video frame data."""
    # Frame data will be random bytes for this example
    frame_data = bytes([randint(0, 255) for _ in range(100)])  # 100 bytes of random video data
    if frame_type == 9:  # Keyframe
        frame_info = bytes([0x17])  # Keyframe, AVC
    else:  # Interframe
        frame_info = bytes([0x27])  # Interframe, AVC
    # AVC NALU type + CompositionTime (3 bytes)
    avc_header = frame_info + bytes([0x00, 0x00, 0x00])
    return avc_header + frame_data

def construct_video_tag(video_data):
    """Constructs a video tag."""
    tag_type = bytes([9])  # Video tag
    data_length = len(video_data)
    data_stream = tag_type + data_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + video_data
    return data_stream

create_complex_flv_file()