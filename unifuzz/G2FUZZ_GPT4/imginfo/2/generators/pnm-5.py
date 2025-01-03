import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# PBM example - A simple black and white checkerboard
pbm_data = """
P1
# This is an example of a PBM (Portable BitMap) file
8 8
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
"""
with open(os.path.join(output_dir, 'example.pbm'), 'w') as f:
    f.write(pbm_data.strip())

# PGM example - A simple gradient
pgm_data = """
P2
# This is an example of a PGM (Portable GrayMap) file
16 8
255
0   32  64  96  128 160 192 224 255 224 192 160 128 96  64  32
32  64  96  128 160 192 224 255 224 192 160 128 96  64  32  0
64  96  128 160 192 224 255 224 192 160 128 96  64  32  0   32
96  128 160 192 224 255 224 192 160 128 96  64  32  0   32  64
128 160 192 224 255 224 192 160 128 96  64  32  0   32  64  96
160 192 224 255 224 192 160 128 96  64  32  0   32  64  96  128
192 224 255 224 192 160 128 96  64  32  0   32  64  96  128 160
224 255 224 192 160 128 96  64  32  0   32  64  96  128 160 192
"""
with open(os.path.join(output_dir, 'example.pgm'), 'w') as f:
    f.write(pgm_data.strip())

# PPM example - A simple color gradient
ppm_data = """
P3
# This is an example of a PPM (Portable PixMap) file
16 8
255
255 0   0     255 32  0     255 64  0     255 96  0     255 128 0     255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 0
255 32  0     255 64  0     255 96  0     255 128 0     255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 32
255 64  0     255 96  0     255 128 0     255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 64
255 96  0     255 128 0     255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 96
255 128 0     255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 128
255 160 0     255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 160
255 192 0     255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 192
255 224 0     255 255 0     224 255 0     192 255 0     160 255 0     128 255 0     96  255 0     64  255 0     32  255 0     0   255 224
"""
with open(os.path.join(output_dir, 'example.ppm'), 'w') as f:
    f.write(ppm_data.strip())