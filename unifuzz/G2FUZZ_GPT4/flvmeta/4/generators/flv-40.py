import os
import struct
import json

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV signature, version, flags, and header length
    
    # PreviousTagSize0, following the FLV header
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Custom metadata in an FLV file is stored in a script data tag.
    def create_metadata_tag(metadata):
        # Script tag type
        tag_type = b'\x12'
        
        # Serialize metadata using a simple JSON representation for the example
        metadata_str = json.dumps(metadata)
        metadata_bytes = metadata_str.encode('utf-8')
        
        # Calculate the data size of this tag (metadata_bytes length)
        data_size = len(metadata_bytes)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Timestamp and StreamID (placeholders)
        timestamp = b'\x00\x00\x00'
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + metadata_bytes
        
        return tag, len(tag)
    
    def create_video_frame_tag(frame_number):
        # Video tag type
        tag_type = b'\x09'
        
        # Random data for a video frame to simulate real data
        frame_data = os.urandom(1024)  # 1KB of video data
        
        # Calculate the data size of this tag (frame_data length)
        data_size = len(frame_data)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Timestamp and StreamID (placeholders)
        timestamp = struct.pack('>I', frame_number * 40)[1:]  # Simulate a timestamp increase
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
        
        return tag, len(tag)
    
    def create_audio_frame_tag(frame_number):
        # Audio tag type
        tag_type = b'\x08'
        
        # Random data for an audio frame to simulate real data
        frame_data = os.urandom(256)  # 256 bytes of audio data
        
        # Calculate the data size of this tag (frame_data length)
        data_size = len(frame_data)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Timestamp - same as video for simplicity
        timestamp = struct.pack('>I', frame_number * 40)[1:]
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
        
        return tag, len(tag)
    
    # Example metadata properties
    metadata = {
        "duration": 120.0,
        "width": 640,
        "height": 360,
        "videocodecid": 7,
        "audiocodecid": 10
    }
    
    # Start assembling the FLV content
    flv_content = flv_header + previous_tag_size_0
    
    # Add a metadata tag
    metadata_tag, metadata_tag_size = create_metadata_tag(metadata)
    flv_content += metadata_tag
    
    previous_tag_size = metadata_tag_size
    flv_content += struct.pack('>I', previous_tag_size)  # Corrected syntax error here
    
    # Simulate adding multiple video and audio frame tags
    for frame_number in range(10):
        frame_tag, frame_tag_size = create_video_frame_tag(frame_number)
        flv_content += frame_tag
        flv_content += struct.pack('>I', frame_tag_size)
        
        audio_tag, audio_tag_size = create_audio_frame_tag(frame_number)
        flv_content += audio_tag
        flv_content += struct.pack('>I', audio_tag_size)
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')