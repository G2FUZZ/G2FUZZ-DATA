import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0 (always 0 for the first tag in the file)
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Custom Metadata Tag (Script Data)
    metadata = b'\x12'  # Tag type for script data
    metadata_body = b'METADATA\x00' + struct.pack('>B', 0)  # Example metadata name
    metadata_body += b'\x08\x00\x00\x00\x03'  # ECMA array (type 8), 3 elements
    metadata_body += b'width\x00?\xf0\x00\x00\x00\x00\x00\x00'  # width: 1920
    metadata_body += b'height\x00?\xf0\x00\x00\x00\x00\x00\x00'  # height: 1080
    metadata_body += b'duration\x00@\x9c\x00\x00\x00\x00\x00\x00'  # duration: 5 seconds
    metadata_body += b'\x00\x00\x09'  # ECMA array end
    metadata += struct.pack('>L', len(metadata_body))[1:]  # Data size (3 bytes)
    metadata += b'\x00\x00\x00\x00\x00\x00\x00'  # Timestamp and StreamID
    metadata += metadata_body
    
    # Simulate video frames
    video_frame = b'\x09'  # Tag type for video
    video_frame_body = b'\x17\x00\x00\x00' + b'\x00' * 10  # Video data example
    video_frame += struct.pack('>L', len(video_frame_body))[1:]  # Data size
    video_frame += b'\x00\x00\x00\x00\x00\x00\x00'  # Timestamp and StreamID
    video_frame += video_frame_body
    
    # Simulate a simple audio frame
    audio_frame = b'\x08'  # Tag type for audio
    audio_frame_body = b'\xAF' + b'\x01' + b'\x00' * 4  # Audio data example
    audio_frame += struct.pack('>L', len(audio_frame_body))[1:]  # Data size
    audio_frame += b'\x00\x00\x00\x00\x00\x00\x00'  # Timestamp and StreamID
    audio_frame += audio_frame_body
    
    # Calculate PreviousTagSize for each tag
    prev_tag_size_metadata = struct.pack('>L', len(metadata) + 11)  # 11 bytes for tag header
    prev_tag_size_video = struct.pack('>L', len(video_frame) + 11)
    prev_tag_size_audio = struct.pack('>L', len(audio_frame) + 11)
    
    # Combine all elements
    flv_content = (flv_header + previous_tag_size_0 + metadata + prev_tag_size_metadata +
                   video_frame + prev_tag_size_video + video_frame + prev_tag_size_video + 
                   audio_frame + prev_tag_size_audio)

    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file with custom metadata, video frames, and an audio frame created at: {flv_file_path}')