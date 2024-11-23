import os

def create_flv_file_with_additional_features():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/interactive_streaming_protocols.flv'
    
    # FLV file header for a video file without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Writing a simple FLV file with header and no actual video data for demonstration
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # The existing metadata tag about streaming protocols
        metadata_content = "FLV files support streaming via RTMP or HTTP."
        metadata_length = len(metadata_content)
        metadata_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_content, 'latin1')
        flv_file.write(metadata_tag)
        
        # Writing PreviousTagSize for the metadata tag
        flv_file.write(len(metadata_tag).to_bytes(4, byteorder='big'))
        
        # Metadata tag about interactivity feature
        interactivity_description = "FLV files can support interactive features when used with Adobe Flash, including clickable links within the video, allowing for a more engaging user experience."
        interactivity_length = len(interactivity_description)
        interactivity_tag = bytes([18]) + interactivity_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(interactivity_description, 'latin1')
        flv_file.write(interactivity_tag)
        
        # Writing PreviousTagSize for the interactivity tag
        flv_file.write(len(interactivity_tag).to_bytes(4, byteorder='big'))

        # New metadata tag about Scripting Support feature
        scripting_support_description = "ActionScript can be used in conjunction with FLV files for creating interactive applications. This includes manipulating playback, integrating with other web page elements, and handling user input."
        scripting_support_length = len(scripting_support_description)
        scripting_support_tag = bytes([18]) + scripting_support_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(scripting_support_description, 'latin1')
        flv_file.write(scripting_support_tag)
        
        # Writing PreviousTagSize for the Scripting Support tag
        flv_file.write(len(scripting_support_tag).to_bytes(4, byteorder='big'))
    
    print(f"FLV file with additional features created at {flv_file_path}")

create_flv_file_with_additional_features()