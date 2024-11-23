import os
import struct
import json
import random

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV signature, version, flags, and header length
    
    # PreviousTagSize0, following the FLV header
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Custom metadata in an FLV file is stored in a script data tag.
    def create_metadata_tag(metadata):
        # Script tag type
        tag_type = b'\x12'
        
        # Extended metadata with more details
        extended_metadata = metadata.copy()
        extended_metadata['encoder'] = 'Python FLV Generator'
        extended_metadata['filesize'] = 'Placeholder'  # To be updated after file creation
        
        # Serialize metadata using a simple JSON representation for the example
        metadata_str = json.dumps({"onMetaData": extended_metadata})
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
    
    def create_video_frame_tag(frame_number, custom_frame_size=None):
        # Video tag type
        tag_type = b'\x09'
        
        # Custom or random data for a video frame to simulate real data
        frame_data_size = custom_frame_size if custom_frame_size else random.randint(500, 1500)
        frame_data = os.urandom(frame_data_size)  # Variable size of video data
        
        # Calculate the data size of this tag (frame_data length)
        data_size = len(frame_data)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Custom timestamp increment
        timestamp = struct.pack('>I', frame_number * 67)[1:]  # Customized timestamp increase
        
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
        
        return tag, len(tag)
    
    def create_audio_frame_tag(frame_number, custom_frame_size=None):
        # Audio tag type
        tag_type = b'\x08'
        
        # Custom or random data for an audio frame to simulate real data
        frame_data_size = custom_frame_size if custom_frame_size else random.randint(200, 500)
        frame_data = os.urandom(frame_data_size)  # Variable size of audio data
        
        # Calculate the data size of this tag (frame_data length)
        data_size = len(frame_data)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Custom timestamp, synced with video for simplicity
        timestamp = struct.pack('>I', frame_number * 67)[1:]
        
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
        
        return tag, len(tag)
    
    # Example metadata properties with more details
    metadata = {
        "duration": 120.0,
        "width": 640,
        "height": 360,
        "videocodecid": 7,
        "audiocodecid": 10,
        "framerate": 24,
        "audiochannels": 2
    }
    
    # Start assembling the FLV content
    flv_content = flv_header + previous_tag_size_0
    
    # Add a metadata tag
    metadata_tag, metadata_tag_size = create_metadata_tag(metadata)
    flv_content += metadata_tag
    
    previous_tag_size = metadata_tag_size
    flv_content += struct.pack('>I', previous_tag_size)
    
    # Simulate adding multiple video and audio frame tags with varying sizes and custom timestamps
    for frame_number in range(1, 301):  # Simulating a 5-second video at 60 fps
        video_frame_size = 1024 + frame_number * 10  # Increasing video frame size
        frame_tag, frame_tag_size = create_video_frame_tag(frame_number, custom_frame_size=video_frame_size)
        flv_content += frame_tag
        flv_content += struct.pack('>I', frame_tag_size)
        
        audio_frame_size = 256  # Constant audio frame size
        audio_tag, audio_tag_size = create_audio_frame_tag(frame_number, custom_frame_size=audio_frame_size)
        flv_content += audio_tag
        flv_content += struct.pack('>I', audio_tag_size)
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)
    
    # Update the metadata with the accurate filesize
    filesize = os.path.getsize(file_path)
    with open(file_path, 'r+b') as file:
        # Assuming metadata is the first tag after the header
        file.seek(len(flv_header) + len(previous_tag_size_0))  # Skip FLV header and first tag size
        update_metadata_tag, _ = create_metadata_tag({**metadata, "filesize": filesize})
        file.write(update_metadata_tag)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')