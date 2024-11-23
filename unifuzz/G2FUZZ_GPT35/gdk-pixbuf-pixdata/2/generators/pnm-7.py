import os

def generate_pnm_file(metadata, filename):
    header = f"P2\n{metadata['width']} {metadata['height']}\n{metadata['max_pixel_value']}\n"
    data = " ".join(str(i) for i in range(1, metadata['width']*metadata['height']+1))

    with open(filename, 'w') as f:
        f.write(header + data)

metadata = {
    'width': 10,
    'height': 10,
    'max_pixel_value': 255
}

output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

filename = os.path.join(output_dir, 'output.pnm')
generate_pnm_file(metadata, filename)