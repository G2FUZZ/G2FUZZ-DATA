import os

def create_flv_file_with_partial_download():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/streaming_protocols_with_partial_download.flv'
    
    # FLV file header for a video file without audio
    # FLV header format: 'FLV', version 1, flags (video tag present), header size
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Writing a simple FLV file with header and no actual video data for demonstration
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Example metadata tag content for existing features
        metadata_content = "FLV files support streaming via RTMP or HTTP."
        metadata_length = len(metadata_content)
        
        # Constructing a fake data tag for existing features
        data_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(data_tag)
        
        # Writing a final PreviousTagSize for the existing feature data tag
        flv_file.write(len(data_tag).to_bytes(4, byteorder='big'))
        
        # Adding Partial Download Playback feature description
        partial_download_content = "Partial Download Playback: FLV files can begin playback before the file is completely downloaded."
        partial_download_length = len(partial_download_content)
        
        # Constructing a fake data tag for Partial Download Playback feature
        partial_download_tag = bytes([18]) + partial_download_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(partial_download_content, 'latin1')
        flv_file.write(partial_download_tag)
        
        # Writing a final PreviousTagSize for the Partial Download Playback feature data tag
        flv_file.write(len(partial_download_tag).to_bytes(4, byteorder='big'))
    
    print(f"FLV file with Partial Download Playback feature created at {flv_file_path}")

create_flv_file_with_partial_download()