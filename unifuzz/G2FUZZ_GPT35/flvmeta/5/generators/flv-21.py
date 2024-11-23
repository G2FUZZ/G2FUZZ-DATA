import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_script_data_and_cue_points_and_timecode_support(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    cue_points = b'\x00\x00\x00\x0F\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01'  # Example cue points
    timecode_support = b'\x00\x00\x00\x13\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'  # Timecode Support data
    flv_content = script_data + cue_points + timecode_support
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/script_data_with_cue_points_and_timecode_support.flv'
create_flv_with_script_data_and_cue_points_and_timecode_support(file_path)

print(f'FLV file with script data, cue points, and Timecode Support created at: {file_path}')