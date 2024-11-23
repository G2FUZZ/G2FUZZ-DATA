import os

def save_pnm_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

def generate_pnm_no_metadata(width, height, max_val):
    pnm_header = f"P5\n{width} {height}\n{max_val}\n".encode('ascii')
    pixel_data = bytearray([0]*width*height)  # Generating dummy pixel data
    return pnm_header + pixel_data

# Create tmp directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

width = 100
height = 100
max_val = 255
pnm_data = generate_pnm_no_metadata(width, height, max_val)

file_path = './tmp/no_metadata.pnm'
save_pnm_file(file_path, pnm_data)

print(f"Generated 'pnm' file with no metadata at: {file_path}")