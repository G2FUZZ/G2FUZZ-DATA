import os

def create_gradient_pgm(size, max_val):
    """Create a vertical gradient for a PGM file."""
    data = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append(int((x / size) * max_val))
        data.append(row)
    return data

def create_checker_pattern_pbm(size, block_size):
    """Create a checkerboard pattern for a PBM file."""
    data = []
    for y in range(size):
        row = []
        for x in range(size):
            if (x // block_size) % 2 == (y // block_size) % 2:
                row.append(1)
            else:
                row.append(0)
        data.append(row)
    return data

def create_color_gradient_ppm(size):
    """Create a RGB color gradient for a PPM file."""
    data = []
    for y in range(size):
        row = []
        for x in range(size):
            r = int((x / size) * 255)
            g = int((y / size) * 255)
            b = 255 - r
            row.extend([r, g, b])
        data.append(row)
    return data

def write_pnm_file(filename, mode, data, max_val=None):
    """Write PNM file based on mode and data."""
    if mode == 'P1' or mode == 'P4':  # PBM
        with open(filename, 'w' if mode == 'P1' else 'wb') as f:
            header = f"{mode}\n{len(data[0])} {len(data)}\n"
            f.write(header.encode() if mode == 'P4' else header)
            for row in data:
                line = ' '.join(str(bit) for bit in row) + '\n'
                f.write(line.encode() if mode == 'P4' else line)
    elif mode == 'P2' or mode == 'P5':  # PGM
        with open(filename, 'w' if mode == 'P2' else 'wb') as f:
            header = f"{mode}\n{len(data[0])} {len(data)}\n{max_val}\n"
            f.write(header.encode() if mode == 'P5' else header)
            for row in data:
                line = ' '.join(str(val) for val in row) + '\n'
                f.write(line.encode() if mode == 'P5' else line)
    elif mode == 'P3' or mode == 'P6':  # PPM
        with open(filename, 'w' if mode == 'P3' else 'wb') as f:
            header = f"{mode}\n{len(data[0]) // 3} {len(data)}\n255\n"
            f.write(header.encode() if mode == 'P6' else header)
            for row in data:
                if mode == 'P3':
                    line = ' '.join(str(val) for val in row) + '\n'
                    f.write(line)
                else:
                    f.write(bytes(row))

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate complex PNM files
size = 100
max_val = 255
block_size = 10

# Generate and write complex PBM, PGM, and PPM files
pbm_data = create_checker_pattern_pbm(size, block_size)  # Corrected line
write_pnm_file('./tmp/complex_pbm_ascii.pbm', 'P1', pbm_data)
write_pnm_file('./tmp/complex_pbm_binary.pbm', 'P4', pbm_data)

pgm_data = create_gradient_pgm(size, max_val)
write_pnm_file('./tmp/complex_pgm_ascii.pgm', 'P2', pgm_data, max_val)
write_pnm_file('./tmp/complex_pgm_binary.pgm', 'P5', pgm_data, max_val)

ppm_data = create_color_gradient_ppm(size)
write_pnm_file('./tmp/complex_ppm_ascii.ppm', 'P3', ppm_data)
write_pnm_file('./tmp/complex_ppm_binary.ppm', 'P6', ppm_data)