import numpy as np
import os

def create_pnm_image(filename, width, height, maxval=255):
    """
    Create a simple PNM image with basic pattern and save it to filename.
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)
    
    # Creating a simple pattern: a gradient for R, G, and B
    x = np.linspace(0, 1, width, endpoint=True)
    y = np.linspace(0, 1, height, endpoint=True)
    xv, yv = np.meshgrid(x, y)
    
    # Simple pattern - gradient for each channel
    red_channel = (xv * maxval).astype(np.uint8)
    green_channel = (yv * maxval).astype(np.uint8)
    blue_channel = (((xv + yv) / 2) * maxval).astype(np.uint8)
    
    # Stack the channels to create an RGB image
    img = np.dstack((red_channel, green_channel, blue_channel))
    
    # Write PPM header
    with open(filepath, 'wb') as f:
        f.write(bytearray(f"P6\n{width} {height}\n{maxval}\n", 'ascii'))
        
        # Flatten the image array and write the binary data
        img.tofile(f)

# Example usage
create_pnm_image('example.ppm', 256, 256)