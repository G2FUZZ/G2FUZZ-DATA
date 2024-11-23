import os

def save_pbm(filename, width, height, data):
    """Save a binary (P1) PBM file."""
    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        for row in data:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

def save_pgm(filename, width, height, max_gray, data):
    """Save a binary (P2) PGM file."""
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")
        for row in data:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

def save_ppm(filename, width, height, max_color, data):
    """Save a binary (P3) PPM file."""
    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_color}\n")
        for row in data:
            for pixel in row:
                f.write(' '.join(str(channel) for channel in pixel) + '  ')
            f.write('\n')

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Example data for PBM
pbm_data = [[0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]]
save_pbm('./tmp/example.pbm', 5, 4, pbm_data)

# Example data for PGM
pgm_data = [[10, 60, 90, 60, 10],
            [60, 110, 140, 110, 60],
            [90, 140, 255, 140, 90],
            [60, 110, 140, 110, 60]]
save_pgm('./tmp/example.pgm', 5, 4, 255, pgm_data)

# Example data for PPM
ppm_data = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [255, 255, 255], [0, 255, 255]],
            [[255, 0, 255], [0, 0, 0], [100, 100, 100]]]
save_ppm('./tmp/example.ppm', 3, 3, 255, ppm_data)