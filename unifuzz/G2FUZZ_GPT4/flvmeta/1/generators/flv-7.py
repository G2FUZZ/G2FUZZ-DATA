def create_flv_file(output_path):
    # FLV file header for a video file
    # FLV header consists of 'FLV', version (1), flags (audio/video), and header size
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    # PreviousTagSize0 always follows the FLV header, which is 0 for the first tag
    previous_tag_size0 = bytearray([0x00, 0x00, 0x00, 0x00])

    # In a real scenario, here we would add FLV tags to create video and audio data.
    # For simplicity, this example will not include detailed FLV body content.

    # Combine the FLV header and the first PreviousTagSize0
    flv_content = flv_header + previous_tag_size0

    # Write the bytes to an FLV file
    with open(output_path, 'wb') as flv_file:
        flv_file.write(flv_content)

# Specify the output path for the FLV file
output_path = './tmp/sample.flv'

# Create the directory if it doesn't exist
import os
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the FLV file
create_flv_file(output_path)