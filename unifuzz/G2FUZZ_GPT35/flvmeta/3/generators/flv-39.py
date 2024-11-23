import os
import struct

class FLVGenerator:
    def __init__(self):
        self.file_path = './tmp/extended_sample.flv'

    def generate_flv_file(self):
        with open(self.file_path, 'wb') as file:
            # Write FLV header
            file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
            
            # Write video tag with H.264 codec
            video_tag = b'\x09\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00'
            file.write(video_tag)
            
            # Write audio tag with AAC codec
            audio_tag = b'\x08\x00\x00\x00\x00\x0A\x00\x00\x00\x00\x00\x00\x00'
            file.write(audio_tag)
            
            # Write metadata tag
            metadata_tag = b'\x12\x00\x00\x00\x00\x2D\x00\x00\x00\x00\x00\x00\x00'
            metadata = b'\x08onMetaData\x08durationAdouble\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            file.write(metadata_tag + metadata)
            
            print(f"Extended FLV file generated and saved at: {self.file_path}")

# Create a directory to save the extended FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate extended FLV file with multiple tracks, metadata, and timestamps
flv_generator = FLVGenerator()
flv_generator.generate_flv_file()