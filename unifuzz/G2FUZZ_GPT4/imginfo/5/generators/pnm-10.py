import os

def generate_ppm_file(path, width, height):
    """
    Generate a PPM file with a simple gradient from black to red, green, and blue across the width.
    """
    header = f"P3\n{width} {height}\n255\n"
    content = []

    for y in range(height):
        row = []
        for x in range(width):
            r = (x * 255) // width
            g = ((x * 255) // width) * (y // (height // 2)) if y >= height // 2 else 0
            b = ((x * 255) // width) * ((height - y) // (height // 2)) if y < height // 2 else 0
            row.append(f"{r} {g} {b}")
        content.append(" ".join(row))

    with open(path, 'w') as f:
        f.write(header + "\n".join(content))

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple PPM file
generate_ppm_file('./tmp/direct_color_representation.ppm', 256, 256)