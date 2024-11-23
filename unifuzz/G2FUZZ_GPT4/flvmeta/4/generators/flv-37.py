import os
from struct import pack

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Metadata tag (script data tag to simulate metadata, e.g., duration, width, height)
    # Tag type for script data: 18
    # Data size: variable, for simplicity, we'll use a small fixed size
    # Timestamp: 0
    # StreamID: 0 (always 0)
    metadata_tag_type = b'\x12'
    metadata_body = b'\x02\x00\x0AonMetaData' + \
                    b'\x08\x00\x00\x00\x03' + \
                    b'\x00\x08duration\x00\x40\x40\xE0\x00\x00\x00\x00\x00' + \
                    b'\x00\x05width\x00\x40\x90\x00\x00\x00\x00\x00\x00' + \
                    b'\x00\x06height\x00\x40\x6E\x00\x00\x00\x00\x00\x00' + \
                    b'\x00\x00\x09'  # ECMA array end
    metadata_data_size = pack('>I', len(metadata_body))[1:]
    metadata_timestamp = b'\x00\x00\x00'
    metadata_stream_id = b'\x00\x00\x00'
    metadata_tag = metadata_tag_type + metadata_data_size + metadata_timestamp + metadata_stream_id + metadata_body
    
    previous_tag_size_metadata = pack('>I', len(metadata_tag))
    
    # Video tag (for simplicity, this will be a dummy video frame)
    video_tag_type = b'\x09'
    video_body = b'\x17\x00\x00\x00\x00' + (b'\x00\x00\x01' * 10)  # Key frame, AVC, composition time 0, dummy data
    video_data_size = pack('>I', len(video_body))[1:]
    video_timestamp = b'\x00\x00\x21'  # Some arbitrary timestamp
    video_stream_id = b'\x00\x00\x00'
    video_tag = video_tag_type + video_data_size + video_timestamp + video_stream_id + video_body
    
    previous_tag_size_video = pack('>I', len(video_tag))
    
    # Audio tag (for simplicity, this will be a dummy audio data)
    audio_tag_type = b'\x08'
    audio_body = b'\xAF\x01' + (b'\x00' * 20)  # AAC, AAC packet type sequence header, dummy data
    audio_data_size = pack('>I', len(audio_body))[1:]
    audio_timestamp = b'\x00\x00\x31'  # Some arbitrary timestamp, slightly after the video
    audio_stream_id = b'\x00\x00\x00'
    audio_tag = audio_tag_type + audio_data_size + audio_timestamp + audio_stream_id + audio_body
    
    previous_tag_size_audio = pack('>I', len(audio_tag))
    
    # Combine all parts
    flv_content = flv_header + previous_tag_size_0 + metadata_tag + previous_tag_size_metadata + video_tag + previous_tag_size_video + audio_tag + previous_tag_size_audio
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
complex_flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(complex_flv_file_path)

print(f'Complex FLV file created at: {complex_flv_file_path}')