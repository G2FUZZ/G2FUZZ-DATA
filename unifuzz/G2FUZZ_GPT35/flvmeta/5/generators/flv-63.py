import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_complex_data(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    audio_data = b'\x00\x00\x00\x01\x00\x02\x00\x00\x00\x03'  # Example audio data
    video_data = b'\x00\x00\x00\x02\x00\x03\x00\x00\x00\x04'  # Example video data
    
    # More complex file structures with additional audio and video tags
    audio_data2 = b'\x00\x00\x00\x01\x00\x02\x00\x00\x00\x05'  # Additional audio data
    video_data2 = b'\x00\x00\x00\x02\x00\x03\x00\x00\x00\x06'  # Additional video data
    
    complex_data = script_data + audio_data + video_data + audio_data2 + video_data2
    generate_flv_file(file_path, complex_data)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/complex_data_extended.flv'
create_flv_with_complex_data(file_path)

print(f'FLV file with more complex data structures created at: {file_path}')