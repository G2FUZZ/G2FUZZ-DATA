import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a PPM file with a specific pattern
def create_ppm(filename, width, height):
    # Header for a PPM file: P3 = RGB color image in ASCII
    header = f'P3\n{width} {height}\n255\n'
    # Create a simple pattern: alternating red and green pixels
    pixels = ''
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                # Red pixel
                pixels += '255 0 0 '
            else:
                # Green pixel
                pixels += '0 255 0 '
        pixels += '\n'
    
    # Write the PPM file
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write(header + pixels)

# Example usage: create a 100x100 PPM file
create_ppm('example.ppm', 100, 100)