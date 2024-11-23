import os

def generate_pnm_file(metadata, filename):
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'# Metadata: {metadata}\n')
        f.write('5 5\n')
        f.write('255\n')
        
        for _ in range(5):
            line = ' '.join([' '.join(str((i+j)%256) for i in range(5)) for j in range(0, 5*5, 5)])
            f.write(f'{line}\n')

metadata = 'Width: 5, Height: 5, Max Pixel Value: 255'

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

filename = './tmp/test.pnm'
generate_pnm_file(metadata, filename)

print(f'PNM file generated and saved at {filename}')