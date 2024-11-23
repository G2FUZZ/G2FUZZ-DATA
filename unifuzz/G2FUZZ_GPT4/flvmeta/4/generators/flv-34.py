import os
import struct

def create_complex_flv_file(file_path):
    # FLV file header
    flv_header = b'\x46\x4C\x56\x01\x05\x00\x00\x00\x09'  # FLV signature, version, flags, and header length
    
    # PreviousTagSize0, following the FLV header
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Custom metadata in an FLV file is stored in a script data tag.
    def create_metadata_tag():
        # Script tag type
        tag_type = b'\x12'
        
        # Example metadata properties: duration, width, height, video codec ID
        metadata = {
            "duration": 120.0,
            "width": 640,
            "height": 360,
            "videocodecid": 7
        }
        
        # Simulate serialization of metadata into a byte sequence.
        metadata_bytes = b'\x00\x00\x00\x00'  # Placeholder for serialized metadata
        
        # Calculate the data size of this tag (metadata_bytes length)
        data_size = len(metadata_bytes)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Timestamp and StreamID (placeholders)
        timestamp = b'\x00\x00\x00'
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + metadata_bytes
        
        return tag
    
    def create_video_frame_tag(frame_number):
        # Video tag type
        tag_type = b'\x09'
        
        # Placeholder data for a video frame
        frame_data = b'\x00\x00\x00\x00'
        if frame_number == 0:
            frame_data = b'\x00\x00\x00\x01'
        
        # Calculate the data size of this tag (frame_data length)
        data_size = len(frame_data)
        data_size_bytes = struct.pack('>I', data_size)[1:]  # 24 bits representing the data size
        
        # Timestamp and StreamID (placeholders)
        timestamp = struct.pack('>I', frame_number * 40)[1:]  # Simulate a timestamp increase
        stream_id = b'\x00\x00\x00'
        
        # Assemble the tag
        tag = tag_type + data_size_bytes + timestamp + stream_id + frame_data
        
        return tag
    
    # Start assembling the FLV content
    flv_content = flv_header + previous_tag_size_0
    
    # Add a metadata tag
    metadata_tag = create_metadata_tag()
    flv_content += metadata_tag
    
    # Simulate adding multiple video frame tags
    for frame_number in range(10):
        frame_tag = create_video_frame_tag(frame_number)
        flv_content += frame_tag
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the FLV content to a file
    with open(file_path, 'wb') as file:
        file.write(flv_content)

# Example usage
flv_file_path = './tmp/complex_example.flv'
create_complex_flv_file(flv_file_path)

print(f'Complex FLV file created at: {flv_file_path}')