import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy FLV file with Script Data, Multi-bitrate Support, and Custom Metadata
flv_data = b'FLV File Generated by Python'

# Adding Script Data feature
script_data = b'Script Data: FLV files can contain script data used for interactive content or metadata.'

# Adding Multi-bitrate Support feature
multi_bitrate_data = b'Multi-bitrate Support: FLV files can contain multiple bitrates for adaptive streaming.'

# Adding Custom Metadata feature
custom_metadata = b'Custom Metadata: FLV files can store custom metadata fields for specific application requirements.'

with open('./tmp/sample_with_script_data_multibitrate_custommetadata.flv', 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')
    f.write(b'\x00\x00\x00\x09')  # PreviousTagSize0

    # FLV body
    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x11')  # Tag Type: Script Data, DataSize: 17
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
    f.write(b'\x00\x00\x00\x00\x00')  # StreamID
    f.write(script_data)  # Script Data

    f.write(b'\x00\x00\x00\x1f')  # PreviousTagSize1

    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x1a')  # Tag Type: Multi-bitrate Support, DataSize: 26
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
    f.write(b'\x00\x00\x00\x00\x00')  # StreamID
    f.write(multi_bitrate_data)  # Multi-bitrate Support

    f.write(b'\x00\x00\x00$\x00\x00\x00\x00\x09')  # PreviousTagSize2

    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x17')  # Tag Type: Custom Metadata, DataSize: 23
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
    f.write(b'\x00\x00\x00\x00\x00')  # StreamID
    f.write(custom_metadata)  # Custom Metadata

    f.write(b'\x00\x00\x00$\x00\x00\x00\x00\x09')  # PreviousTagSize3

    f.write(b'\x00\x00\x00\x00\x09')  # Tag Type: Video, DataSize: 9
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp, StreamID

    f.write(flv_data)  # Existing FLV data

print("FLV file with Script Data, Multi-bitrate Support, and Custom Metadata generated successfully!")