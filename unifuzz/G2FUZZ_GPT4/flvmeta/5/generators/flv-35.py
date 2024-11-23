import os
import random
import struct

def create_enhanced_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/enhanced_video.flv'
    
    # FLV file header for a video file with audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Add a metadata tag with detailed information
        metadata_content = "duration\x00?\xf0\x00\x00\x00\x00\x00\x00" + \
                           "width\x00@\x1f\x00\x00\x00\x00\x00\x00" + \
                           "height\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "framerate\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "videocodecid\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "audiocodecid\x00@\x1e\x00\x00\x00\x00\x00\x00"
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Simulate the addition of video frames with variable sizes
        for i in range(1, 11):  # Generate 10 frames with variable sizes
            frame_data = os.urandom(random.randint(512, 2048))  # Randomly generated frame data of variable size
            frame_length = len(frame_data)
            timestamp = i * 500  # Assuming each frame is 0.5 seconds apart
            
            # Video tag: Frame Type(1 byte) + CodecID(1 byte) + Frame Data
            video_tag_type = 9  # Video data
            frame_info = bytes([0x17 if i == 1 else 0x27]) + bytes([0x01])  # Key frame (for first frame) or inter frame + AVC NALU
            video_data = frame_info + frame_data
            video_tag = bytes([video_tag_type]) + frame_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + video_data
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        # Simulate the addition of audio frames
        for i in range(1, 21):  # Generate 20 audio frames
            audio_data = os.urandom(random.randint(256, 1024))  # Randomly generated audio data of variable size
            audio_length = len(audio_data)
            timestamp = i * 250  # Assuming each audio frame is 0.25 seconds apart
            
            # Audio tag: SoundFormat(1 byte) + SoundRate(1 byte) + SoundSize(1 byte) + SoundType(1 byte) + Audio Data
            audio_tag_type = 8  # Audio data
            audio_info = bytes([0xAF])  # AAC sequence header
            audio_data = audio_info + audio_data
            audio_tag = bytes([audio_tag_type]) + audio_length.to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + audio_data
            flv_file.write(audio_tag)
            flv_file.write(len(audio_tag).to_bytes(4, byteorder='big'))
        
        print(f"Enhanced FLV file created at {flv_file_path}")

create_enhanced_flv_file()