import os
import struct

class FLVMetadata:
    def __init__(self, duration, creation_date, tags):
        self.duration = duration
        self.creation_date = creation_date
        self.tags = tags

    def to_bytes(self):
        duration_bytes = struct.pack('>I', self.duration)
        creation_date_bytes = struct.pack('>I', self.creation_date)
        tags_bytes = self.tags.encode('utf-8')

        data = b'\x02' + struct.pack('>I', len(duration_bytes)) + duration_bytes + \
               b'\x03' + struct.pack('>I', len(creation_date_bytes)) + creation_date_bytes + \
               b'\x08' + struct.pack('>I', len(tags_bytes)) + tags_bytes

        return data

def save_flv_with_metadata(duration, creation_date, tags):
    metadata = FLVMetadata(duration, creation_date, tags)
    flv_data = b'FLV' + b'\x01' + b'\x00\x00\x00\x09' + metadata.to_bytes()
    
    file_path = './tmp/{}.flv'.format(tags.replace(' ', '_'))
    
    with open(file_path, 'wb') as file:
        file.write(flv_data)

# Generate FLV file with metadata
duration = 3600  # in seconds
creation_date = 1635591600  # October 30, 2021 12:00:00 AM UTC
tags = 'example_video'

save_flv_with_metadata(duration, creation_date, tags)