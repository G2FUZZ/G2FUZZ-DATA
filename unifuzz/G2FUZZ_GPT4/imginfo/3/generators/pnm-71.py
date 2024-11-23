import os

def create_directory(path='./tmp/'):
    """Ensure the directory exists."""
    if not os.path.exists(path):
        os.makedirs(path)

def generate_gradient_ppm(width, height, filename, direction='horizontal'):
    """Generate a horizontal or vertical gradient PPM image."""
    max_color = 255
    with open(filename, 'w') as f:
        f.write(f'P3\n{width} {height}\n{max_color}\n')
        for row in range(height):
            for col in range(width):
                if direction == 'horizontal':
                    red = int((col / width) * max_color)
                    green = int((col / width) * max_color)
                    blue = 255 - int((col / width) * max_color)
                else:  # Vertical gradient
                    red = int((row / height) * max_color)
                    green = int((row / height) * max_color)
                    blue = 255 - int((row / height) * max_color)
                f.write(f'{red} {green} {blue}\n')

def generate_gradient_pbm(width, height, filename, direction='horizontal'):
    """Generate a horizontal or vertical gradient PBM image."""
    with open(filename, 'wb') as f:
        f.write(b'P4\n')
        f.write(f'{width} {height}\n'.encode())
        for row in range(height):
            for col in range(width):
                # Create a simple black-to-white gradient
                if direction == 'horizontal':
                    value = int((col / width) * 255)
                else:  # Vertical gradient
                    value = int((row / height) * 255)
                # PBM format uses monochrome values, so we just decide if a pixel is black or white
                pixel = 0 if value < 128 else 1
                f.write(bytes([pixel]))

def generate_pnm_files(width, height, format='P3', direction='horizontal'):
    """Generate PNM files based on the specified format and gradient direction."""
    create_directory()
    if format == 'P3':  # PPM format
        filename = './tmp/gradient_ppm.ppm'
        generate_gradient_ppm(width, height, filename, direction)
    elif format == 'P4':  # PBM format
        filename = './tmp/gradient_pbm.pbm'
        generate_gradient_pbm(width, height, filename, direction)
    else:
        print(f'Unsupported format: {format}')

if __name__ == '__main__':
    # Generate a 100x100 PPM file with a horizontal gradient
    generate_pnm_files(100, 100, format='P3', direction='horizontal')
    # Generate a 100x100 PBM file with a vertical gradient
    generate_pnm_files(100, 100, format='P4', direction='vertical')
    print("PNM files have been generated and saved in './tmp/'.")