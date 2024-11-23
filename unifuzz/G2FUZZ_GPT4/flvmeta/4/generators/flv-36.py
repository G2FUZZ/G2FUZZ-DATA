import os
import struct

def create_complex_flv_file(file_path, video_data, audio_data, metadata):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV + Version 1 + Flags 5 + Offset 9
    
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Metadata Tag
    metadata_script_data = create_metadata_tag(metadata)
    
    # Video Tag (simplified example with placeholder data)
    video_tag = create_video_tag(video_data)
    
    # Audio Tag (simplified example with placeholder data)
    audio_tag = create_audio_tag(audio_data)
    
    # Combine all elements
    flv_content = flv_header + previous_tag_size_0 + metadata_script_data + video_tag + audio_tag
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

def create_metadata_tag(metadata):
    # Example of creating a script data tag for metadata
    # TagType (18 for script data), DataSize, Timestamp (0x000000), StreamID (0x000000)
    # Custom script data for metadata
    data = b''  # Placeholder for encoded metadata
    for key, value in metadata.items():
        data += encode_script_data_object(key, value)
        
    data_size = len(data)
    tag_header = struct.pack('>BIII', 18, data_size, 0, 0)  # Convert integers to bytes
    tag_footer = struct.pack('>I', data_size + 11)  # Size of the tag including the header but excluding this field
    
    return tag_header + data + tag_footer

def encode_script_data_object(key, value):
    # This function should encode the key-value pairs according to the FLV specification for script data objects
    # Placeholder for simplicity
    return b''  # Implement actual encoding based on FLV spec

def create_video_tag(video_data):
    # Simplified example of creating a video tag
    # TagType (9 for video), DataSize, Timestamp (0x000000), StreamID (0x000000)
    # Placeholder video data
    data_size = len(video_data)
    tag_header = struct.pack('>BIII', 9, data_size, 0, 0)
    tag_footer = struct.pack('>I', data_size + 11)
    
    return tag_header + video_data + tag_footer

def create_audio_tag(audio_data):
    # Simplified example of creating an audio tag
    # TagType (8 for audio), DataSize, Timestamp (0x000000), StreamID (0x000000)
    # Placeholder audio data
    data_size = len(audio_data)
    tag_header = struct.pack('>BIII', 8, data_size, 0, 0)
    tag_footer = struct.pack('>I', data_size + 11)
    
    return tag_header + audio_data + tag_footer

# Example usage
flv_file_path = './tmp/complex_example.flv'
video_data = b'\x00' * 1000  # Placeholder for video frame data
audio_data = b'\x00' * 500   # Placeholder for audio frame data
metadata = {'duration': 120, 'width': 640, 'height': 480}
create_complex_flv_file(flv_file_path, video_data, audio_data, metadata)

print(f'Complex FLV file created at: {flv_file_path}')