import numpy as np

def create_pnm_file(width, height):
    max_val = 255
    image = np.random.randint(0, max_val+1, size=(height, width, 3), dtype=np.uint8)
    
    header = f'P3\n{width} {height}\n{max_val}\n'
    data = ''
    for row in image:
        for pixel in row:
            data += f'{pixel[0]} {pixel[1]} {pixel[2]}\n'
    
    pnm_data = header + data
    
    file_path = f'./tmp/image_{width}x{height}.pnm'
    with open(file_path, 'w') as file:
        file.write(pnm_data)

# Generate a pnm file with specified width and height
width = 800
height = 600
create_pnm_file(width, height)