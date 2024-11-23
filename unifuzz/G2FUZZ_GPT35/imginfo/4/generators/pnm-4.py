import os

def generate_pnm_file(filename, width, height, max_pixel_value):
    header = f"P2\n{width} {height}\n{max_pixel_value}\n"
    data = " ".join(str(i % max_pixel_value) for i in range(width * height))
    
    with open(filename, 'w') as file:
        file.write(header + data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pnm_file('./tmp/example.pnm', 10, 10, 255)