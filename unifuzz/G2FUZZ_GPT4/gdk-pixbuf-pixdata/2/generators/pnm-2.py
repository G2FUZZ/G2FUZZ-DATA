import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Define a simple function to generate PNM files
def generate_pnm(filename, width, height, data):
    """
    Generate a PNM file with specified dimensions and data.
    :param filename: The filename to save the PNM file as.
    :param width: The width of the image.
    :param height: The height of the image.
    :param data: A list of tuples representing pixel data in RGB format.
    """
    path = os.path.join('./tmp/', filename)
    with open(path, 'w') as f:
        # P3 means this is a PPM file in ASCII format
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        # Max color value
        f.write('255\n')
        for row in data:
            for pixel in row:
                f.write(' '.join(map(str, pixel)) + ' ')
            f.write('\n')

# Example usage
width, height = 3, 2
data = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
    [(255, 255, 0), (255, 255, 255), (0, 0, 0)]
]
generate_pnm('example.ppm', width, height, data)