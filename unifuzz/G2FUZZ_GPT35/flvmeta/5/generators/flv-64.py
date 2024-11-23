import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_complex_flv(file_path):
    # Example additional metadata
    metadata = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' 
    
    # Example video frames
    video_frame_1 = b'\x00\x00\x00\x0A\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02' 
    video_frame_2 = b'\x00\x00\x00\x0B\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03'
    
    # Example audio frames
    audio_frame_1 = b'\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00' 
    audio_frame_2 = b'\x0E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00'
    
    flv_content = metadata + video_frame_1 + audio_frame_1 + video_frame_2 + audio_frame_2
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/more_complex_flv_file.flv'
create_complex_flv(file_path)

print(f'More complex FLV file created at: {file_path}')