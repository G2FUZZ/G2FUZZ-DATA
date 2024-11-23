import os
import struct

# Create a directory to store the generated FLV files
os.makedirs('tmp', exist_ok=True)

for i in range(3):
    file_name = f'./tmp/video_{i}.flv'
    with open(file_name, 'wb') as file:
        # Write FLV header
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Add metadata tag
        metadata_tag = b'\x12\x00\x00\x00\x00\x00\x00\x02\x00\x0aonMetaData\x08\x00\x00\x00\x01\x00\x00\x00\x00\xb0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        file.write(struct.pack('>I', len(metadata_tag)))
        file.write(metadata_tag)
        
        # Add video tag
        video_tag = b'\x09\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00'
        file.write(struct.pack('>I', len(video_tag)))
        file.write(video_tag)
        
        # Add audio tag
        audio_tag = b'\x08\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00'
        file.write(struct.pack('>I', len(audio_tag)))
        file.write(audio_tag)
        
        # Add Timecode information
        timecode_info = b'Timecode information: 00:00:00:00'
        file.write(timecode_info)