import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example - A simple black and white pattern
pbm_data = [
    "P1",  # Magic number for PBM file format
    "4 4",  # Width and Height
    "0 1 0 1",
    "1 0 1 0",
    "0 1 0 1",
    "1 0 1 0"
]
# Save PBM file
with open('./tmp/example.pbm', 'w') as f:
    f.write('\n'.join(pbm_data))

# PGM example - A simple gradient from black to white
pgm_data = [
    "P2",  # Magic number for PGM file format
    "256 2",  # Width and Height
    "255"  # Maximum gray value
] + [' '.join([str(i) for i in range(256)]) for _ in range(2)]
# Save PGM file
with open('./tmp/example.pgm', 'w') as f:
    f.write('\n'.join(pgm_data))

# PPM example - A simple RGB color gradient
ppm_data = [
    "P3",  # Magic number for PPM file format
    "256 1",  # Width and Height
    "255"  # Maximum color value
]
# Generate a horizontal RGB gradient
ppm_data.append(' '.join([f"{i} {255-i} {i//2}" for i in range(256)]))
# Save PPM file
with open('./tmp/example.ppm', 'w') as f:
    f.write('\n'.join(ppm_data))