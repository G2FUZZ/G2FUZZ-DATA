import os

def generate_flv_file(file_path, content):
    with open(file_path, 'wb') as f:
        f.write(content)

def create_flv_with_script_data(file_path):
    script_data = b'\x46\x4C\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00'  # Example script data
    generate_flv_file(file_path, script_data)

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

file_path = './tmp/script_data.flv'
create_flv_with_script_data(file_path)

print(f'FLV file with script data created at: {file_path}')