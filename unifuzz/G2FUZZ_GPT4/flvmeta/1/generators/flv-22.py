def create_flv_file_with_adobe_integration(output_path):
    # FLV file header for a video file with Adobe integration feature
    # FLV header consists of 'FLV', version (1), flags (audio/video), and header size
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    # PreviousTagSize0 always follows the FLV header, which is 0 for the first tag
    previous_tag_size0 = bytearray([0x00, 0x00, 0x00, 0x00])

    # Metadata tag for Adobe Flash Platform Integration
    # Constructing a simple onMetaData tag with an AMF0 encoded string 'onMetaData'
    # and a simplified object with a custom property to illustrate integration.
    # Note: In a real application, the metadata should contain meaningful data and be correctly encoded.
    metadata_tag_type = bytearray([0x12])  # Script data tag
    metadata_body = b'\x02\x00\x0aonMetaData\x08\x00\x00\x00\x00\x03'  # Simplified AMF0 object
    metadata_body += b'\x00\x23IntegrationWithAdobeFlashPlatform\x02\x00\x15True Adobe Flash Integration'
    metadata_body += b'\x00\x00\x09'  # AMF0 object end marker

    # Calculate the DataSize for the metadata tag body and prepend it
    metadata_data_size = len(metadata_body).to_bytes(3, 'big')
    metadata_timestamp = (0).to_bytes(3, 'big') + (0).to_bytes(1, 'big')  # 24-bit timestamp + 8-bit timestamp extended
    metadata_stream_id = (0).to_bytes(3, 'big')  # Always 0 for FLV tags
    metadata_tag_header = metadata_tag_type + metadata_data_size + metadata_timestamp + metadata_stream_id

    # Combine the FLV header, the first PreviousTagSize0, metadata tag header, and metadata body
    flv_content = flv_header + previous_tag_size0 + metadata_tag_header + metadata_body

    # Calculate the PreviousTagSize for the metadata tag and append it
    previous_tag_size_metadata = (len(metadata_tag_header) + len(metadata_body)).to_bytes(4, 'big')
    flv_content += previous_tag_size_metadata

    # Write the bytes to an FLV file
    with open(output_path, 'wb') as flv_file:
        flv_file.write(flv_content)

# Specify the output path for the FLV file
output_path = './tmp/sample_with_adobe_integration.flv'

# Create the directory if it doesn't exist
import os
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the FLV file with Adobe Flash Platform Integration
create_flv_file_with_adobe_integration(output_path)