import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_script_data_and_alpha_channel(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    alpha_channel_data = b'\x00\x00\x00\x00\x00\x00\x12\x00'  # Alpha Channel Support data
    generate_flv_file(file_path, script_data + alpha_channel_data)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/script_data_with_alpha_channel.flv'
create_flv_with_script_data_and_alpha_channel(file_path)

print(f'FLV file with script data and Alpha Channel Support created at: {file_path}')