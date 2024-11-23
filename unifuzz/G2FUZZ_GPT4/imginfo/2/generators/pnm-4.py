import os

def create_pnm_image(filename, width, height, maxval, pixels):
    """
    Create a PNM (P3 PPM format) file with the given parameters.

    Parameters:
    - filename: The name of the file to save the image to.
    - width: The width of the image.
    - height: The height of the image.
    - maxval: The maximum value for color components.
    - pixels: A list of tuples representing the pixels of the image in RGB format.
             This list should have width*height elements.
    """
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    with open(f'./tmp/{filename}', 'w') as file:
        # PPM header
        file.write(f'P3\n{width} {height}\n{maxval}\n')
        
        # Pixel data
        for i in range(height):
            for j in range(width):
                pixel_index = i * width + j
                # Ensure we don't go out of bounds
                if pixel_index < len(pixels):
                    r, g, b = pixels[pixel_index]
                    file.write(f'{r} {g} {b} ')
            file.write('\n')

# Example usage
# Creating a simple 3x3 image with random color values
width, height = 3, 3
maxval = 255
pixels = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 255, 255), (0, 255, 255),
    (255, 0, 255), (0, 0, 0), (128, 128, 128)
]

create_pnm_image('example.pnm', width, height, maxval, pixels)