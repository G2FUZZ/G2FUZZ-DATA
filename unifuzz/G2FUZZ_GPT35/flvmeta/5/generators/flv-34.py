import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_complex_flv_file(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    cue_points = b'\x00\x00\x00\x0F\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01'  # Example cue points
    embedded_fonts = b'\x0A\x00\x00\x00\x00\x00\x00\x00'  # Example embedded fonts
    additional_metadata = b'\x0B\x00\x00\x00\x00\x00\x00\x00'  # Additional metadata
    multiple_cue_points = b'\x00\x00\x00\x0F\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x20\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x02'  # Multiple cue points
    advanced_audio_video_data = b'\x0C\x00\x00\x00\x00\x00\x00\x00'  # Advanced audio/video data

    flv_content = script_data + cue_points + embedded_fonts + additional_metadata + multiple_cue_points + advanced_audio_video_data
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/complex_flv_file.flv'
create_complex_flv_file(file_path)

print(f'Complex FLV file created at: {file_path}')