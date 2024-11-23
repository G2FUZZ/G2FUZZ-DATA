import os

def generate_complex_pnm_file(metadata, filename):
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'# Metadata: {metadata}\n')
        f.write('10 10\n')
        f.write('255\n')
        
        for y in range(10):
            for x in range(10):
                r = x * 25
                g = y * 25
                b = (x + y) * 13 % 256
                f.write(f'{r} {g} {b} # Pixel at ({x},{y})\n')

metadata = 'Width: 10, Height: 10, Max Pixel Value: 255'

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

filename = './tmp/complex_test.pnm'
generate_complex_pnm_file(metadata, filename)

print(f'Complex PNM file generated and saved at {filename}')