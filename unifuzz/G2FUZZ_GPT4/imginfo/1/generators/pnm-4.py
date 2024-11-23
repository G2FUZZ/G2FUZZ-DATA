import os

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generating a simple PBM file
pbm_data = """P1
# This is a simple PBM example
4 4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
with open('./tmp/simple.pbm', 'w') as f:
    f.write(pbm_data)

# Generating a simple PPM file
ppm_data = """P3
# This is a simple PPM example
4 2
255
255   0   0     0 255   0     0   0 255   255 255   0
255 255 255   255 255 255   0   0   0     0   0   0
"""
with open('./tmp/simple.ppm', 'w') as f:
    f.write(ppm_data)

print("PNM files have been generated and saved in './tmp/'.")