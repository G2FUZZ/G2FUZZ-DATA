import numpy as np

def create_tga_file(file_path, width, height, pixel_format, metadata=None, color_correction=None):
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
        
        # Write metadata if available
        if metadata:
            f.write(b'\nMetadata: ' + metadata.encode())
        
        # Apply color correction if specified
        if color_correction:
            pixels = color_correction(pixels)
        
        # Write pixel data if pixels is not None
        if pixels is not None:
            f.write(pixels.tobytes())

# Define the output directory
output_dir = './tmp/'

# Create a TGA file with color correction
def apply_color_correction(pixels):
    # Example color correction function (inverting colors)
    return 255 - pixels

create_tga_file(output_dir + 'color_corrected.tga', 512, 512, 'true_color', metadata='Image with color correction', color_correction=apply_color_correction)