import os

def create_complex_flv_file(output_path):
    # FLV file header for a video file with audio and video support
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    # PreviousTagSize0 always follows the FLV header, which is 0 for the first tag
    previous_tag_size0 = bytearray([0x00, 0x00, 0x00, 0x00])

    # Preparing the file content with the FLV header and the first PreviousTagSize0
    flv_content = flv_header + previous_tag_size0

    # Generate a metadata tag (similar to the simple example)
    metadata_tag = create_metadata_tag({
        "duration": 0,  # Placeholder, real duration needs to be calculated
        "width": 1280,
        "height": 720,
        "videocodecid": 7,  # AVC
        "audiocodecid": 10  # AAC
    })
    flv_content += metadata_tag + calculate_previous_tag_size(metadata_tag)

    # Generate a sample video frame (H.264 keyframe)
    video_frame = create_video_frame()
    flv_content += video_frame + calculate_previous_tag_size(video_frame)

    # Generate a sample audio frame (AAC frame)
    audio_frame = create_audio_frame()
    flv_content += audio_frame + calculate_previous_tag_size(audio_frame)

    # Write the bytes to an FLV file
    with open(output_path, 'wb') as flv_file:
        flv_file.write(flv_content)

def create_metadata_tag(metadata):
    # Construct the onMetaData tag with AMF0 encoded data
    # This example simplifies the encoding; for real use, a proper AMF0 encoder should be used.
    return b''  # Placeholder for metadata tag construction

def calculate_previous_tag_size(tag):
    # Calculate and return the PreviousTagSize for a given tag
    return len(tag).to_bytes(4, 'big')

def create_video_frame():
    # Generate a sample H.264 keyframe (SPS, PPS, and I-frame)
    # This is a simplified placeholder. In practice, you would use actual H.264 NAL units.
    return b''  # Placeholder for video frame construction

def create_audio_frame():
    # Generate a sample AAC audio frame
    # This is a simplified placeholder. In a real implementation, actual AAC raw data should be used.
    return b''  # Placeholder for audio frame construction

# Specify the output path for the FLV file
output_path = './tmp/complex_sample.flv'

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the complex FLV file
create_complex_flv_file(output_path)