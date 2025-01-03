import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy FLV file with Cue Points, Metadata, and Cue Point Indexing
flv_data = b'FLV File Generated by Python'

# Adding Cue Points feature
cue_point_data = b'Cue Points: FLV files can contain cue points for navigation and synchronization.'

# Adding Metadata feature
metadata = {
    'title': 'Sample FLV File',
    'author': 'Python FLV Generator',
    'description': 'This is a sample FLV file generated using Python script.'
}

# Adding Cue Point Indexing feature
cue_point_index = {
    'cue_point_1': {'time': 5, 'description': 'First Cue Point'},
    'cue_point_2': {'time': 15, 'description': 'Second Cue Point'},
    'cue_point_3': {'time': 25, 'description': 'Third Cue Point'}
}

with open('./tmp/sample_with_cuepoints_metadata_cuepointindex.flv', 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')
    f.write(b'\x00\x00\x00\x09')  # PreviousTagSize0

    # FLV body
    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x0f')  # Tag Type: Cue Points, DataSize: 15
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
    f.write(b'\x00\x00\x00\x00\x00')  # StreamID
    f.write(cue_point_data)  # Cue Points

    f.write(b'\x00\x00\x00\x19')  # PreviousTagSize1

    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00')  # Tag Type: Metadata, DataSize: 0
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
    f.write(b'\x00\x00\x00\x00\x00')  # StreamID

    f.write(b'\x00\x00\x00\x1b')  # PreviousTagSize2

    for cue_name, cue_data in cue_point_index.items():
        f.write(b'\x00\x00\x00\x00\x08')  # Tag Type: Script Data, DataSize: 8
        f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp
        f.write(b'\x00\x00\x00\x00\x00')  # StreamID
        f.write(cue_data['description'].encode())  # Cue Point Description

    f.write(b'\x00\x00\x00(\x00\x00\x00\x00\x0b')  # PreviousTagSize3

    f.write(b'\x00\x00\x00\x00\x09')  # Tag Type: Video, DataSize: 9
    f.write(b'\x00\x00\x00\x00\x00\x00')  # Timestamp, StreamID

    f.write(flv_data)  # Existing FLV data

print("FLV file with Cue Points, Metadata, and Cue Point Indexing generated successfully!")