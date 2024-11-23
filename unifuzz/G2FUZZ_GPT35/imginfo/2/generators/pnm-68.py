import numpy as np

def generate_pnm(width, height, max_val, pnm_type='P6'):
    if pnm_type not in ['P5', 'P6']:
        raise ValueError("Unsupported PNM type. Only P5 (PGM) and P6 (PPM) are supported.")
    
    if pnm_type == 'P5':
        data = np.random.randint(0, max_val + 1, (height, width), dtype=np.uint8)
    else:
        data = np.random.randint(0, max_val + 1, (height, width, 3), dtype=np.uint8)
    
    return data

def save_pnm(data, filename, max_val, pnm_type='P6'):
    if pnm_type not in ['P5', 'P6']:
        raise ValueError("Unsupported PNM type. Only P5 (PGM) and P6 (PPM) are supported.")
    
    with open(filename, 'wb') as file:
        file.write(f'{pnm_type}\n'.encode())
        file.write(f'{data.shape[1]} {data.shape[0]}\n'.encode())
        file.write(f'{max_val}\n'.encode())
        
        if pnm_type == 'P5':
            data.tofile(file)
        else:
            data.tofile(file)

# Generate and save more complex PNM file
width, height = 10, 10
max_val = 255

# Generate and save PGM file (more complex)
pgm_data = generate_pnm(width, height, max_val, 'P5')
pgm_filename = './tmp/complex_image.pgm'
save_pnm(pgm_data, pgm_filename, max_val, 'P5')

# Generate and save a more complex PPM file
ppm_data = generate_pnm(width, height, max_val, 'P6')
ppm_filename = './tmp/complex_image.ppm'
save_pnm(ppm_data, ppm_filename, max_val, 'P6')