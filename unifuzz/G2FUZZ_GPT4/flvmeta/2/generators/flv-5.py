import os
import struct

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Path to the generated FLV file
flv_file_path = './tmp/streaming_support.flv'

# FLV header structure:
# Signature: "FLV" (3 bytes)
# Version: 1 (1 byte)
# Flags: 5 (Audio + Video tags present) (1 byte)
# Header Length: 9 (4 bytes)
flv_header = b'FLV\x01\x05\x00\x00\x00\x09'

# First PreviousTagSize0: 0 (4 bytes, UI32)
previous_tag_size0 = b'\x00\x00\x00\x00'

# For the sake of simplicity, this example does not include the creation of actual FLV tags.
# Creating meaningful video/audio data involves encoding frames which is beyond the scope of this example.
# Typically, one would use video/audio encoding libraries to generate these.

with open(flv_file_path, 'wb') as flv_file:
    flv_file.write(flv_header)
    flv_file.write(previous_tag_size0)

    # Normally, here you would write FLV tags for video and audio data
    # For example purposes, no actual media data is included

print(f'FLV file created at {flv_file_path}')