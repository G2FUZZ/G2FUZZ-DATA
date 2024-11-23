import os

def save_pbm(filename, width, height, data, binary=True):
    """Save a PBM file."""
    header = "P4\n" if binary else "P1\n"
    mode = 'wb' if binary else 'w'
    with open(filename, mode) as f:
        f.write(header.encode() if binary else header)
        f.write(f"{width} {height}\n".encode() if binary else f"{width} {height}\n")
        if binary:
            for row in data:
                byte = 0
                for i, pixel in enumerate(row):
                    byte = byte | (pixel << (7 - i % 8))
                    if i % 8 == 7:
                        f.write(byte.to_bytes(1, 'big'))
                        byte = 0
                if len(row) % 8 != 0:  # Handle incomplete bytes
                    f.write(byte.to_bytes(1, 'big'))
        else:
            for row in data:
                f.write(' '.join(str(pixel) for pixel in row) + '\n')

def save_pgm(filename, width, height, max_gray, data, binary=True):
    """Save a PGM file."""
    header = "P5\n" if binary else "P2\n"
    mode = 'wb' if binary else 'w'
    with open(filename, mode) as f:
        f.write(header.encode() if binary else header)
        f.write(f"{width} {height}\n".encode() if binary else f"{width} {height}\n")
        f.write(f"{max_gray}\n".encode() if binary else f"{max_gray}\n")
        if binary:
            for row in data:
                row_bytes = bytearray(row)
                f.write(row_bytes)
        else:
            for row in data:
                f.write(' '.join(str(pixel) for pixel in row) + '\n')

def save_ppm(filename, width, height, max_color, data, binary=True):
    """Save a PPM file."""
    header = "P6\n" if binary else "P3\n"
    mode = 'wb' if binary else 'w'
    with open(filename, mode) as f:
        f.write(header.encode() if binary else header)
        f.write(f"{width} {height}\n".encode() if binary else f"{width} {height}\n")
        f.write(f"{max_color}\n".encode() if binary else f"{max_color}\n")
        if binary:
            for row in data:
                for pixel in row:
                    f.write(bytearray(pixel))
        else:
            for row in data:
                for pixel in row:
                    f.write(' '.join(str(channel) for channel in pixel) + ' ')
                f.write('\n')

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Example data for PBM
pbm_data = [[0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]]
save_pbm('./tmp/example_binary.pbm', 5, 4, pbm_data, binary=True)
save_pbm('./tmp/example_ascii.pbm', 5, 4, pbm_data, binary=False)

# Example data for PGM
pgm_data = [[10, 60, 90, 60, 10],
            [60, 110, 140, 110, 60],
            [90, 140, 255, 140, 90],
            [60, 110, 140, 110, 60]]
save_pgm('./tmp/example_binary.pgm', 5, 4, 255, pgm_data, binary=True)
save_pgm('./tmp/example_ascii.pgm', 5, 4, 255, pgm_data, binary=False)

# Example data for PPM
ppm_data = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [255, 255, 255], [0, 255, 255]],
            [[255, 0, 255], [0, 0, 0], [100, 100, 100]]]
save_ppm('./tmp/example_binary.ppm', 3, 3, 255, ppm_data, binary=True)
save_ppm('./tmp/example_ascii.ppm', 3, 3, 255, ppm_data, binary=False)