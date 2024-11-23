import os
import random
import struct
import time

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_video.flv'
    
    # FLV file header for a video file with audio (0x05) would be without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Add an extended metadata tag with more detailed information
        metadata_content = "duration\x00?\xf0\x00\x00\x00\x00\x00\x00" + \
                           "width\x00@\x1f\x00\x00\x00\x00\x00\x00" + \
                           "height\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "framerate\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "videocodecid\x00@\x1e\x00\x00\x00\x00\x00\x00"
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Add a custom script data tag for user-defined metadata
        script_data_tag = create_custom_script_tag("MyCustomData", "This is a sample custom data")
        flv_file.write(script_data_tag)
        flv_file.write(len(script_data_tag).to_bytes(4, byteorder='big'))
        
        # Simulate the addition of video frames with variable frame rates
        for i in range(1, 6):  # Just for demonstration, generate 5 frames
            frame_data = os.urandom(1024 + random.randint(-512, 512))  # Randomly generated frame data with variable size
            frame_length = len(frame_data)
            timestamp = i * 1000  # Assuming each frame is 1 second apart
            composition_time = random.randint(-500, 500)  # Composition time offset for AVC frames
            
            # Handle negative composition_time correctly
            if composition_time < 0:
                # Convert to a positive value with the same bit representation as if it were signed
                composition_time = 0xFFFFFF + composition_time + 1
            
            # Video tag: Frame Type(1 byte) + CodecID(1 byte) + Frame Data
            video_tag_type = 9  # Video data
            frame_info = bytes([0x17 if i == 1 else 0x27, 0x01])  # Key frame (for first frame) or inter frame + AVC NALU
            video_data = frame_info + composition_time.to_bytes(3, byteorder='big') + frame_data
            video_tag = bytes([video_tag_type]) + frame_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + (0).to_bytes(3, byteorder='big') + video_data
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        print(f"Complex FLV file created at {flv_file_path}")

def create_custom_script_tag(name, value):
    # Encodes a name/value pair as a script data tag
    # Name is encoded as SCRIPTDATASTRING, value as SCRIPTDATAVALUE
    name_encoded = bytes([len(name) >> 8, len(name) & 0xFF]) + bytes(name, 'latin1')
    value_encoded = bytes([2]) + bytes([len(value) >> 8, len(value) & 0xFF]) + bytes(value, 'latin1')
    script_data = name_encoded + value_encoded
    data_length = len(script_data)
    script_tag = bytes([18]) + data_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + script_data
    return script_tag

create_complex_flv_file()