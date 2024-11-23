import os

def generate_pnm_file(file_path):
    with open(file_path, 'wb') as f:
        f.write(b'P6\n# Lossless Compression: PNM files use lossless compression, preserving the image quality without any loss of information\n1 1\n255\n\xFF\x00\x00')

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_path = './tmp/example.pnm'
generate_pnm_file(file_path)
print(f'PNM file generated at: {file_path}')