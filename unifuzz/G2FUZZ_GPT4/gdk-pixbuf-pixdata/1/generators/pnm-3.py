import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example: A simple 8x8 checkerboard pattern
# Corrected by wrapping the generator expression in square brackets to form a list comprehension
pbm_data = [
    "P1",  # Magic number for PBM
    "8 8",  # Width and Height
] + [" ".join("0 1" if (x + y) % 2 == 0 else "1 0" for x in range(4)) for y in range(8)]  # Corrected line

with open('./tmp/checkerboard.pbm', 'w') as f:
    f.write('\n'.join(pbm_data))

# PGM example: A gradient from black to white
# Corrected by wrapping the generator expression in square brackets to form a list comprehension
pgm_data = [
    "P2",  # Magic number for PGM
    "256 10",  # Width and Height
    "255",  # Max gray value
] + [" ".join(str(x) for x in range(256)) for _ in range(10)]  # Corrected line

with open('./tmp/gradient.pgm', 'w') as f:
    f.write('\n'.join(pgm_data))

# PPM example: A simple RGB color bar
ppm_data = [
    "P3",  # Magic number for PPM
    "300 100",  # Width and Height
    "255",  # Max color value
]
# Generating the color bars
for _ in range(100):
    for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
        ppm_data.append(" ".join(f"{value} {value} {value}" for value in color for _ in range(100)))

with open('./tmp/colorbar.ppm', 'w') as f:
    f.write('\n'.join(ppm_data))