import os
import random

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_streaming_with_video_frames.flv'
    
    # FLV file header for a video file without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Open the file to start writing the complex FLV structure
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Adding a script data tag for metadata
        metadata = "duration\x00@\x1f\x85\xebQ\xb8\x1e\x09@\x00\x00\x00\x00\x00\x00\x00"  # Example metadata with duration
        metadata_tag = construct_script_data_tag(metadata)
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Generating and adding video data tags
        for i in range(10):  # Generate 10 fake video frames for demonstration
            video_frame_data = generate_fake_video_frame(i)
            video_data_tag = construct_video_data_tag(video_frame_data)
            flv_file.write(video_data_tag)
            flv_file.write(len(video_data_tag).to_bytes(4, byteorder='big'))
        
        print(f"Complex FLV file with video data tags created at {flv_file_path}")

def construct_script_data_tag(metadata):
    # Script data tag starts with 18
    tag_type = bytes([18])
    data_length = len(metadata)
    timestamp = (0).to_bytes(3, byteorder='big')
    stream_id = (0).to_bytes(3, byteorder='big')
    script_data = bytes(metadata, 'latin1')
    return tag_type + data_length.to_bytes(3, byteorder='big') + timestamp + stream_id + script_data

def generate_fake_video_frame(frame_number):
    # Fake video frame data for demonstration, typically would be actual video data
    frame_data = f"frame{frame_number}" + "".join(random.choices("0123456789abcdef", k=60))
    return frame_data

def construct_video_data_tag(video_frame_data):
    # Video data tag starts with 9
    tag_type = bytes([9])
    data_length = len(video_frame_data)
    timestamp = (0).to_bytes(3, byteorder='big')  # Placeholder for demonstration
    timestamp_extended = (0).to_bytes(1, byteorder='big')  # Placeholder for demonstration
    stream_id = (0).to_bytes(3, byteorder='big')
    video_data = bytes(video_frame_data, 'latin1')
    return tag_type + data_length.to_bytes(3, byteorder='big') + timestamp + timestamp_extended + stream_id + video_data

create_complex_flv_file()