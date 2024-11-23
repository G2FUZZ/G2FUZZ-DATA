import os

def generate_pnm_file_with_color(metadata, filename):
    header = f"P3\n{metadata['width']} {metadata['height']}\n{metadata['max_pixel_value']}\n"
    data = ""
    
    for i in range(metadata['height']):
        for j in range(metadata['width']):
            r = i % metadata['max_pixel_value']
            g = j % metadata['max_pixel_value']
            b = (i + j) % metadata['max_pixel_value']
            data += f"{r} {g} {b} "

    with open(filename, 'w') as f:
        f.write(header + data)

metadata = {
    'width': 10,
    'height': 10,
    'max_pixel_value': 255
}

output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

filename = os.path.join(output_dir, 'output_color.pnm')
generate_pnm_file_with_color(metadata, filename)