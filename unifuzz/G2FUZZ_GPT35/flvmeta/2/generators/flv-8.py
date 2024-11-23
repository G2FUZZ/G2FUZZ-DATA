import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with the specified feature
with open('./tmp/editable_file.flv', 'wb') as f:
    f.write(b'FLV file with editable feature: FLV files can be edited using various video editing software.')