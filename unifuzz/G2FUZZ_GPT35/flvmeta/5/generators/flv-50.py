import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_extended_flv_file(file_path):
    video_tag = b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    audio_tag = b'\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    metadata_tag = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'

    flv_content = video_tag + audio_tag + metadata_tag
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/extended_flv_file.flv'
create_extended_flv_file(file_path)

print(f'Extended FLV file created at: {file_path}')