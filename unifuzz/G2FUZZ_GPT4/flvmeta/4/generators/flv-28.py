import os
from struct import pack

def create_complex_flv_file(file_path):
    # FLV file header for a video file
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV signature, Version, Flags, Header Length
    
    # PreviousTagSize0 (always 0 for the first tag in the file)
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # FLV metadata tag (onMetaData)
    # Script data type (0x12 for onMetaData), 0 time stamp, streamID always 0
    # The length of data will be calculated after creating the metadata
    metadata_body = b'\x02\x00\x0AonMetaData'  # ScriptDataString 'onMetaData'
    metadata_body += b'\x08\x00\x00\x00\x00'  # ScriptDataECMAArray (Array Start Marker + Length)
    # The ECMAArray Length here is 0 for simplicity; normally, it contains video metadata.
    metadata_body += b'\x00\x00\x09'  # ScriptDataObjectEndMarker
    metadata_length = len(metadata_body)
    metadata_tag = pack('>BIB', 0x12, 0, metadata_length) + b'\x00\x00\x00' + metadata_body
    
    # Video tag (keyframe, for simplicity)
    # Frame type 1 (keyframe) and CodecID 7 (AVC)
    video_data = b'\x17\x00\x00\x00\x00'  # AVC sequence header
    video_data += b'\x00\x01'  # Simulated video frame data
    video_length = len(video_data)
    video_tag = pack('>BIB', 0x09, 0, video_length) + b'\x00\x00\x00' + video_data
    
    # Audio tag (AAC sequence header)
    audio_data = b'\xAF\x00'  # AAC sequence header
    audio_data += b'\x01\x02'  # Simulated audio frame data
    audio_length = len(audio_data)
    audio_tag = pack('>BIB', 0x08, 0, audio_length) + b'\x00\x00\x00' + audio_data
    
    # Calculate previous tag sizes
    metadata_tag_size = len(metadata_tag) + 4  # Including the PreviousTagSize field
    video_tag_size = len(video_tag) + 4  # Including the PreviousTagSize field
    # No PreviousTagSize after audio tag, as it's the last tag
    
    # Combine all elements
    flv_content = (
        flv_header +
        previous_tag_size_0 +
        metadata_tag + pack('>I', metadata_tag_size) +
        video_tag + pack('>I', video_tag_size) +
        audio_tag
    )
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')