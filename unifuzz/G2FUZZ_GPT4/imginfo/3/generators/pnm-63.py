import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def write_pnm(filename, width, height, data, format='P3', maxval=255):
    """
    General function to write PBM, PGM, or PPM files.
    - filename: Name of the file to save.
    - width, height: Dimensions of the image.
    - data: Pixel data, formatted as a list of rows, where each row is a list of values (or tuples for PPM).
    - format: 'P1' for PBM, 'P2' for PGM, 'P3' for PPM.
    - maxval: Maximum value for a pixel (for PGM and PPM).
    """
    header = f'{format}\n{width} {height}\n'
    if format != 'P1':  # PBM doesn't have a maxval line
        header += f'{maxval}\n'

    # Convert pixel data to string
    pixels = ''
    for row in data:
        for pixel in row:
            if isinstance(pixel, tuple):  # For PPM
                pixels += ' '.join(map(str, pixel)) + ' '
            else:  # For PBM and PGM
                pixels += str(pixel) + ' '
        pixels += '\n'
    
    # Write the file
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write(header + pixels)

def create_horizontal_gradient(width, height, format='P3', maxval=255):
    """
    Create a horizontal gradient.
    - width, height: Dimensions of the gradient.
    - format: 'P1' for PBM (binary gradient), 'P2' for PGM, 'P3' for PPM.
    - maxval: Maximum value for a pixel (for PGM and PPM).
    """
    data = []
    for y in range(height):
        row = []
        for x in range(width):
            if format == 'P3':
                # Horizontal gradient from red to green
                red = int((x / width) * maxval)
                green = maxval - red
                blue = 0
                row.append((red, green, blue))
            elif format == 'P2':
                # Horizontal grayscale gradient
                value = int((x / width) * maxval)
                row.append(value)
            elif format == 'P1':
                # Simple binary pattern for PBM: left half black, right half white
                value = 1 if x > width / 2 else 0
                row.append(value)
        data.append(row)
    return data

def create_checkerboard(width, height, cell_size, format='P3', maxval=255):
    """
    Create a checkerboard pattern.
    - width, height: Dimensions of the checkerboard.
    - cell_size: Size of each cell in the checkerboard.
    - format: 'P1' for PBM, 'P2' for PGM, 'P3' for PPM.
    - maxval: Maximum value for a pixel (for PGM and PPM).
    """
    data = []
    for y in range(height):
        row = []
        for x in range(width):
            if ((x // cell_size) + (y // cell_size)) % 2 == 0:
                if format == 'P3':
                    color = (maxval, 0, 0)  # Red
                else:
                    color = maxval  # White for PBM and PGM
            else:
                if format == 'P3':
                    color = (0, maxval, 0)  # Green
                else:
                    color = 0  # Black for PBM and PGM
            row.append(color)
        data.append(row)
    return data

# Example usage
filename = 'gradient.ppm'
width, height = 100, 100
gradient_data = create_horizontal_gradient(width, height, 'P3')
write_pnm(filename, width, height, gradient_data, 'P3')

filename = 'checkerboard.pbm'
width, height, cell_size = 100, 100, 10
checkerboard_data = create_checkerboard(width, height, cell_size, 'P1')
write_pnm(filename, width, height, checkerboard_data, 'P1')