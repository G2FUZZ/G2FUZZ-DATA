import os

def create_pbm_image(filename):
    """Creates a PBM (Portable Bitmap) file with a simple pattern"""
    header = "P1\n# This is a PBM example\n10 10\n"
    pattern = ["0 1 " * 5, "1 0 " * 5] * 5  # Simple checkerboard pattern
    with open(filename, 'w') as f:
        f.write(header + "\n".join(pattern))

def create_pgm_image(filename):
    """Creates a PGM (Portable Graymap) file with a gradient pattern"""
    header = "P2\n# This is a PGM example\n10 10\n255\n"
    gradient = [[str((x + y) % 256) for x in range(10)] for y in range(10)]
    with open(filename, 'w') as f:
        f.write(header + "\n".join([" ".join(row) for row in gradient]))

def create_ppm_image(filename):
    """Creates a PPM (Portable Pixmap) file with a simple color pattern"""
    header = "P3\n# This is a PPM example\n10 10\n255\n"
    pattern = []
    for i in range(10):
        row = []
        for j in range(10):
            r = (i * 25) % 256
            g = (j * 25) % 256
            b = ((i + j) * 12) % 256
            row.append(f"{r} {g} {b}")
        pattern.append(" ".join(row))
    with open(filename, 'w') as f:
        f.write(header + "\n".join(pattern))

# Create the tmp/ directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate PNM files
create_pbm_image('./tmp/example.pbm')
create_pgm_image('./tmp/example.pgm')
create_ppm_image('./tmp/example.ppm')