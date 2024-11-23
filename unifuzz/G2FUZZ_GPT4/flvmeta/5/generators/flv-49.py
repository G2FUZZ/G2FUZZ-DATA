import os
import random

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_streaming_video.flv'
    
    # FLV file header for a video file with audio
    # FLV header format: 'FLV', version 1, flags (video tag present | audio tag present), header size
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Writing a simple FLV file with header and no actual video data for demonstration
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Simulating multiple video and audio frames
        for i in range(1, 11):  # Generate 10 video and 10 audio tags for demo
            # Simulate a video frame
            video_content = f"Video frame {i}".encode('latin1')
            video_data_tag = construct_data_tag(9, video_content)
            flv_file.write(video_data_tag)
            flv_file.write(len(video_data_tag).to_bytes(4, byteorder='big'))
            
            # Simulate an audio frame
            audio_content = f"Audio frame {i}".encode('latin1')
            audio_data_tag = construct_data_tag(8, audio_content)
            flv_file.write(audio_data_tag)
            flv_file.write(len(audio_data_tag).to_bytes(4, byteorder='big'))
        
    print(f"Complex FLV file created at {flv_file_path}")

def construct_data_tag(tag_type, content):
    """
    Constructs a data tag for the FLV file.
    
    Args:
    - tag_type: An integer indicating the type of the tag (8 for audio, 9 for video).
    - content: Byte content of the tag.
    
    Returns:
    - A byte array representing the constructed tag.
    """
    # Tag structure: TagType (1 byte) | DataSize (3 bytes) | Timestamp (3 bytes) | TimestampExtended (1 byte) | StreamID (3 bytes) | Data
    data_size = len(content)
    timestamp = random.randint(0, 1000)  # Simulate a random timestamp for each frame
    timestamp_extended = timestamp >> 24 & 0xFF
    timestamp &= 0xFFFFFF
    stream_id = 0  # Default StreamID for FLV
    
    tag = bytes([tag_type]) + \
          data_size.to_bytes(3, byteorder='big') + \
          timestamp.to_bytes(3, byteorder='big') + \
          bytes([timestamp_extended]) + \
          stream_id.to_bytes(3, byteorder='big') + \
          content
    
    return tag

create_complex_flv_file()