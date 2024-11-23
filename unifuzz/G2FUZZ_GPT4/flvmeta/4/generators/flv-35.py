import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV Header for audio and video
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Video tag - FrameType (1 key frame) + CodecID (2 AVC)
    # AVC video packet - AVC sequence header
    video_data = b'\x01\x02'  # Simplified video data
    video_tag = create_video_tag(video_data)
    
    # Audio tag - SoundFormat (10 AAC) + SoundRate (3 44kHz) + SoundSize (1 16-bit samples) + SoundType (1 Stereo)
    # AAC audio packet - AAC sequence header
    audio_data = b'\x10\x3B'  # Simplified audio data
    audio_tag = create_audio_tag(audio_data)
    
    # Combine all parts to form the FLV content
    flv_content = flv_header + previous_tag_size_0 + video_tag + audio_tag

    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

def create_video_tag(data):
    """Generates a simple video tag for the FLV file."""
    tag_type = b'\x09'  # Video tag
    data_size = struct.pack('>I', len(data))[1:]  # Data size, 3 bytes
    timestamp = b'\x00\x00\x00'  # Timestamp, 3 bytes
    timestamp_extended = b'\x00'  # TimestampExtended, 1 byte
    stream_id = b'\x00\x00\x00'  # StreamID, always 0
    body = tag_type + data_size + timestamp + timestamp_extended + stream_id + data
    previous_tag_size = struct.pack('>I', len(body))
    return body + previous_tag_size

def create_audio_tag(data):
    """Generates a simple audio tag for the FLV file."""
    tag_type = b'\x08'  # Audio tag
    data_size = struct.pack('>I', len(data))[1:]  # Data size, 3 bytes
    timestamp = b'\x00\x00\x00'  # Timestamp, 3 bytes
    timestamp_extended = b'\x00'  # TimestampExtended, 1 byte
    stream_id = b'\x00\x00\x00'  # StreamID, always 0
    body = tag_type + data_size + timestamp + timestamp_extended + stream_id + data
    previous_tag_size = struct.pack('>I', len(body))
    return body + previous_tag_size

# Example usage
flv_file_path_complex = './tmp/example_complex.flv'
create_complex_flv_file(flv_file_path_complex)

print(f'Complex FLV file created at: {flv_file_path_complex}')