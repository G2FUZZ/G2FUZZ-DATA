import os
import random
import struct

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_video.flv'
    
    # FLV file header for a video file without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Add a metadata tag with more detailed information
        metadata_content = "duration\x00?\xf0\x00\x00\x00\x00\x00\x00" + \
                           "width\x00@\x1f\x00\x00\x00\x00\x00\x00" + \
                           "height\x00@\x1e\x00\x00\x00\x00\x00\x00"
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Simulate the addition of video frames
        for i in range(1, 6):  # Just for demonstration, generate 5 frames
            frame_data = os.urandom(1024)  # Randomly generated frame data
            frame_length = len(frame_data)
            timestamp = i * 1000  # Assuming each frame is 1 second apart
            
            # Video tag: Frame Type(1 byte) + CodecID(1 byte) + Frame Data
            # Here, we're simulating a simple video frame without real encoding details
            video_tag_type = 9  # Video data
            frame_info = bytes([0x17 if i == 1 else 0x27]) + bytes([0x01])  # Key frame (for first frame) or inter frame + AVC NALU
            video_data = frame_info + frame_data
            video_tag = bytes([video_tag_type]) + frame_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + video_data
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        print(f"Complex FLV file created at {flv_file_path}")

create_complex_flv_file()