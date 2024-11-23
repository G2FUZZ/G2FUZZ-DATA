import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_complex_data(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    audio_data = b'\x00\x00\x00\x01\x00\x02\x00\x00\x00\x03'  # Example audio data
    video_data = b'\x00\x00\x00\x02\x00\x03\x00\x00\x00\x04'  # Example video data
    
    complex_data = script_data + audio_data + video_data
    generate_flv_file(file_path, complex_data)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/complex_data.flv'
create_flv_with_complex_data(file_path)

print(f'FLV file with complex data created at: {file_path}')