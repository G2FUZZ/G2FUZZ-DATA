import os
import struct

class FLVMetadata:
    def __init__(self, duration, creation_date, tags, chapter_data, has_3d_support, resolution):
        self.duration = duration
        self.creation_date = creation_date
        self.tags = tags
        self.chapter_data = chapter_data
        self.has_3d_support = has_3d_support
        self.resolution = resolution

    def to_bytes(self):
        duration_bytes = struct.pack('>I', self.duration)
        creation_date_bytes = struct.pack('>I', self.creation_date)
        tags_bytes = self.tags.encode('utf-8')
        chapter_data_bytes = b''
        for chapter_name, timestamp in self.chapter_data.items():
            chapter_data_bytes += struct.pack('>I', len(chapter_name)) + chapter_name.encode('utf-8') + struct.pack('>I', timestamp)
        
        has_3d_support_byte = b'\x0A' + struct.pack('?', self.has_3d_support)
        resolution_bytes = struct.pack('>I', self.resolution)

        data = b'\x02' + struct.pack('>I', len(duration_bytes)) + duration_bytes + \
               b'\x03' + struct.pack('>I', len(creation_date_bytes)) + creation_date_bytes + \
               b'\x08' + struct.pack('>I', len(tags_bytes)) + tags_bytes + \
               b'\x09' + struct.pack('>I', len(chapter_data_bytes)) + chapter_data_bytes + \
               has_3d_support_byte + \
               b'\x0B' + struct.pack('>I', len(resolution_bytes)) + resolution_bytes

        return data

def save_flv_with_metadata(duration, creation_date, tags, chapter_data, has_3d_support, resolution):
    metadata = FLVMetadata(duration, creation_date, tags, chapter_data, has_3d_support, resolution)
    flv_data = b'FLV' + b'\x01' + b'\x00\x00\x00\x0D' + metadata.to_bytes()
    
    file_path = './tmp/{}.flv'.format(tags.replace(' ', '_'))
    
    with open(file_path, 'wb') as file:
        file.write(flv_data)

# Generate FLV file with extended metadata and multiple chapters with timestamps
duration = 7200  # in seconds
creation_date = 1635591600  # October 30, 2021 12:00:00 AM UTC
tags = 'extended_video_example'
chapter_data = {'Chapter 1: Introduction': 0, 'Chapter 2: Main Content': 1800, 'Chapter 3: Conclusion': 3600}
has_3d_support = True
resolution = 1080

save_flv_with_metadata(duration, creation_date, tags, chapter_data, has_3d_support, resolution)