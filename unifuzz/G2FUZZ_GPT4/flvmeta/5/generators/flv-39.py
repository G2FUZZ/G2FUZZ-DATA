import os
import random

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_streaming_protocols.flv'
    
    # FLV file header for a video and audio file
    # FLV header format: 'FLV', version 1, flags (audio and video tags present), header size
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Writing a more complex FLV file with header, video, and audio data
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Example video tag - Simplified representation of a keyframe (type 9)
        # Frame type (keyframe) and Codec ID (AVC)
        video_data = bytes([0x17]) + bytes([0x00, 0x00, 0x00])  # Simplified AVC video packet
        video_data_length = len(video_data)
        video_timestamp = random.randint(0, 1000)  # Random timestamp for demonstration
        video_tag = bytes([9]) + video_data_length.to_bytes(3, byteorder='big') + video_timestamp.to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + video_data
        flv_file.write(video_tag)
        flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        # Example audio tag - Simplified representation of an AAC audio frame (type 8)
        # Sound format (AAC) and AAC packet type (sequence header)
        audio_data = bytes([0xAF, 0x00])  # Simplified AAC audio sequence header
        audio_data_length = len(audio_data)
        audio_timestamp = random.randint(0, 1000)  # Random timestamp for demonstration
        audio_tag = bytes([8]) + audio_data_length.to_bytes(3, byteorder='big') + audio_timestamp.to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + audio_data
        flv_file.write(audio_tag)
        flv_file.write(len(audio_tag).to_bytes(4, byteorder='big'))
        
        # Adding more metadata and tags as needed following similar structure
        
    print(f"Complex FLV file with video and audio tags created at {flv_file_path}")

create_complex_flv_file()