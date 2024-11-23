import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_video_audio_metadata_tags_and_custom_data(file_path):
    video_tag = b'\x00\x00\x00\x0A\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # Example video tag
    audio_tag = b'\x00\x00\x00\x0B\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # Example audio tag
    metadata_tag = b'\x00\x00\x00\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # Example metadata tag
    custom_data = b'\x43\x75\x73\x74\x6F\x6D\x20\x44\x61\x74\x61\x3A\x20\x43\x75\x73\x74\x6F\x6D\x20\x44\x61\x74\x61'  # Custom data
    flv_content = video_tag + audio_tag + metadata_tag + custom_data
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/video_audio_metadata_custom_data.flv'
create_flv_with_video_audio_metadata_tags_and_custom_data(file_path)

print(f'FLV file with video, audio, metadata tags, and custom data created at: {file_path}')