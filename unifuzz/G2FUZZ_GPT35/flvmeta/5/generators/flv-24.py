import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_script_data_cue_points_and_user_data(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    cue_points = b'\x00\x00\x00\x0F\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01'  # Example cue points
    user_data = b'\x55\x73\x65\x72\x20\x44\x61\x74\x61\x3A\x20\x43\x75\x73\x74\x6F\x6D\x20\x55\x73\x65\x72\x20\x44\x61\x74\x61'  # Example user data
    flv_content = script_data + cue_points + user_data
    generate_flv_file(file_path, flv_content)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/script_data_cue_points_user_data.flv'
create_flv_with_script_data_cue_points_and_user_data(file_path)

print(f'FLV file with script data, cue points, and user data created at: {file_path}')