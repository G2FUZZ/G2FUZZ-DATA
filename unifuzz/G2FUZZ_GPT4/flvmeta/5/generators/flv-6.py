import os

def create_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/streaming_protocols.flv'
    
    # FLV file header for a video file without audio
    # FLV header format: 'FLV', version 1, flags (video tag present), header size
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Writing a simple FLV file with header and no actual video data for demonstration
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Normally, here you would write FLV tags for the video data.
        # This example writes a simple metadata tag related to streaming protocols as a placeholder.
        # Please note, in a real scenario, encoding actual video data would require using video encoding libraries.
        
        # Example metadata tag content (not functional, for demonstration only)
        metadata_content = "FLV files support streaming via RTMP or HTTP."
        metadata_length = len(metadata_content)
        
        # Constructing a fake data tag (not a standard FLV tag, for demonstration)
        # Tag type (18 for script data), data size, timestamp, streamID, and fake data
        data_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        
        flv_file.write(data_tag)
        
        # Writing a final PreviousTagSize for the fake data tag, for demonstration
        flv_file.write(len(data_tag).to_bytes(4, byteorder='big'))
    
    print(f"FLV file created at {flv_file_path}")

create_flv_file()