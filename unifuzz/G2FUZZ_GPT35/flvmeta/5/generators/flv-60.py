import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_complex_flv(file_path):
    # Example additional metadata
    metadata = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' 
    
    # Example video data
    video_data = b'\x00\x00\x00\x0A\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02' 
    
    # Example audio data
    audio_data = b'\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00' 
    
    flv_content = metadata + video_data + audio_data
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/complex_flv_file.flv'
create_complex_flv(file_path)

print(f'Complex FLV file created at: {file_path}')