import os
import random
import struct

def create_advanced_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/advanced_video.flv'
    
    # FLV file header for a video file with audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Add a complex metadata tag
        metadata_content = "onMetaData" + \
                           "\x08\x00\x00\x00\x07" + \
                           "duration\x00?\xf0\x00\x00\x00\x00\x00\x00" + \
                           "width\x00@\x1f\x00\x00\x00\x00\x00\x00" + \
                           "height\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "videocodecid\x00@\x1e\x00\x00\x00\x00\x00\x00" + \
                           "audiocodecid\x00@\x1f\x85\xebQ\xb8\x1e\x09@\x00" + \
                           "framerate\x00@\x1f\x00\x00\x00\x00\x00\x00" + \
                           "filesize\x00?\xf0\x00\x00\x00\x00\x00\x00"
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Simulate the addition of video and audio frames
        for i in range(1, 11):  # Generate 10 frames (5 video and 5 audio for simplicity)
            timestamp = i * 1000  # Assuming each frame is 1 second apart
            
            if i % 2 == 0:  # Simulate audio frame
                frame_data = os.urandom(128)  # Smaller random data for audio
                audio_tag_type = 8  # Audio data
                sound_format = 10  # AAC
                sound_rate = 3  # 44 kHz
                sound_size = 1  # 16-bit samples
                sound_type = 1  # Stereo sound
                audio_header = bytes([sound_format << 4 | sound_rate << 2 | sound_size << 1 | sound_type])
                audio_data = audio_header + frame_data
                audio_tag = bytes([audio_tag_type]) + len(audio_data).to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + audio_data
                flv_file.write(audio_tag)
                flv_file.write(len(audio_tag).to_bytes(4, byteorder='big'))
            else:  # Simulate video frame
                frame_data = os.urandom(1024)  # Randomly generated frame data
                video_tag_type = 9  # Video data
                frame_type = 1 if i == 1 else 2  # Key frame for the first frame, inter frame for the others
                codec_id = 7  # AVC
                video_header = bytes([frame_type << 4 | codec_id])
                video_data = video_header + frame_data
                video_tag = bytes([video_tag_type]) + len(video_data).to_bytes(3, byteorder='big') + timestamp.to_bytes(4, byteorder='big') + video_data
                flv_file.write(video_tag)
                flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        print(f"Advanced FLV file created at {flv_file_path}")

create_advanced_flv_file()