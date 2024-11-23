import numpy as np

def create_tga_file(file_path, width, height, pixel_format):
    # Generate random pixel values based on the specified pixel format
    if pixel_format == 'indexed_color':
        pixels = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    elif pixel_format == 'true_color':
        pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    elif pixel_format == 'grayscale':
        pixels = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    elif pixel_format == 'compressed':
        # Generate compressed pixel data (not implemented for this example)
        pixels = None
    else:
        raise ValueError("Unsupported pixel format")
    
    # Save the pixel data to a TGA file
    with open(file_path, 'wb') as f:
        # Write TGA header
        f.write(b'TGA HEADER')
        
        # Write pixel data if pixels is not None
        if pixels is not None:
            f.write(pixels.tobytes())

# Define the output directory
output_dir = './tmp/'

# Create TGA files with different pixel formats
create_tga_file(output_dir + 'indexed_color.tga', 512, 512, 'indexed_color')
create_tga_file(output_dir + 'true_color.tga', 512, 512, 'true_color')
create_tga_file(output_dir + 'grayscale.tga', 512, 512, 'grayscale')
create_tga_file(output_dir + 'compressed.tga', 512, 512, 'compressed')