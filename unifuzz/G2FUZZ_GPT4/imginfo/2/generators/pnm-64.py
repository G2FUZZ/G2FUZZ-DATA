import os

def create_pnm_image(filename, width, height, maxval, pixels=None, format='P3'):
    """
    Create a PNM (PPM) file in either P3 (ASCII) or P6 (Binary) format with the given parameters.

    Parameters:
    - filename: The name of the file to save the image to.
    - width: The width of the image.
    - height: The height of the image.
    - maxval: The maximum value for color components.
    - pixels: A list of tuples representing the pixels of the image in RGB format or None.
              If None, a horizontal gradient image is generated.
              This list should have width*height elements if provided.
    - format: 'P3' for ASCII format or 'P6' for Binary format.
    """
    if format not in ['P3', 'P6']:
        raise ValueError("Unsupported format. Use 'P3' for ASCII or 'P6' for Binary.")

    if not pixels:
        # Generate a horizontal gradient if no pixels are provided
        pixels = []
        for i in range(height):
            for j in range(width):
                r = int((j / width) * maxval)
                g = int(((width - j) / width) * maxval)
                b = maxval // 2
                pixels.append((r, g, b))

    if len(pixels) != width * height:
        raise ValueError("The number of pixels does not match the specified width and height.")

    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    with open(f'./tmp/{filename}', 'wb' if format == 'P6' else 'w') as file:
        # PPM header
        file.write(f'{format}\n{width} {height}\n{maxval}\n'.encode() if format == 'P6' else f'{format}\n{width} {height}\n{maxval}\n')
        
        # Pixel data
        for pixel in pixels:
            if format == 'P3':
                file.write(f'{pixel[0]} {pixel[1]} {pixel[2]} ')
                if pixels.index(pixel) % width == width - 1:  # New line at the end of each row
                    file.write('\n')
            elif format == 'P6':
                file.write(bytearray(pixel))

# Example usage
# Creating a simple 3x3 image with random color values
width, height = 3, 3
maxval = 255
pixels = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 255, 255), (0, 255, 255),
    (255, 0, 255), (0, 0, 0), (128, 128, 128)
]

create_pnm_image('example_p3.pnm', width, height, maxval, pixels, format='P3')  # ASCII format
create_pnm_image('example_p6.pnm', width, height, maxval, pixels, format='P6')  # Binary format