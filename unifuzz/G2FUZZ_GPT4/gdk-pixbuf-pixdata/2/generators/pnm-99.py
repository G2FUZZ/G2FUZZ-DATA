import os

def generate_pbm(size, pattern_size):
    header = "P1\n# Checkerboard PBM\n"
    data = [header + f"{size} {size}"]
    for y in range(size):
        row = []
        for x in range(size):
            cell = (x // pattern_size + y // pattern_size) % 2
            row.append(str(cell))
        data.append(' '.join(row))
    return '\n'.join(data)

def generate_pgm(size, pattern_size, max_shade):
    header = "P2\n# Checkerboard PGM\n"
    data = [header + f"{size} {size}\n{max_shade}"]
    for y in range(size):
        row = []
        for x in range(size):
            shade = (((x // pattern_size + y // pattern_size) % 2) * max_shade) // 1
            row.append(str(shade))
        data.append(' '.join(row))
    return '\n'.join(data)

def generate_ppm(size, pattern_size, max_color_value):
    header = "P3\n# Checkerboard PPM\n"
    data = [header + f"{size} {size}\n{max_color_value}"]
    for y in range(size):
        row = []
        for x in range(size):
            base_color = (x // pattern_size + y // pattern_size) % 2
            r = (base_color * max_color_value) % 256
            g = ((1 - base_color) * max_color_value) % 256
            b = (base_color * max_color_value) % 256
            row.append(f"{r} {g} {b}")
        data.append(' '.join(row))
    return '\n'.join(data)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and write the PBM file
pbm_data = generate_pbm(10, 2)
with open('./tmp/complex_example.pbm', 'w') as file:
    file.write(pbm_data)

# Generate and write the PGM file
pgm_data = generate_pgm(10, 2, 255)
with open('./tmp/complex_example.pgm', 'w') as file:
    file.write(pgm_data)

# Generate and write the PPM file
ppm_data = generate_ppm(10, 2, 255)
with open('./tmp/complex_example.ppm', 'w') as file:
    file.write(ppm_data)