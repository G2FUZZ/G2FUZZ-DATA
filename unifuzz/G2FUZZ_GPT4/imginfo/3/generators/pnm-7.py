import os

def create_pnm_with_extra_channels(filename, width, height, channels):
    """
    Create a PNM file with arbitrary channels. This example will create a PNM-like file
    with 4 channels (RGB + Alpha) for demonstration purposes.

    Parameters:
    - filename: str. The path to save the file.
    - width: int. The width of the image.
    - height: int. The height of the image.
    - channels: int. The number of channels in the image.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Header for a PPM-like file with an extended number of channels
    # 'P6' indicates the PPM format; we use it as a base for our extension.
    header = f"P6\n{width} {height}\n255\n"
    
    # Create a simple pattern with arbitrary values for demonstration
    # Here, each pixel will cycle through values for each channel
    pattern = [((x * y) % 256 for _ in range(channels)) for y in range(height) for x in range(width)]
    
    with open(filename, 'wb') as f:
        f.write(header.encode('ascii'))
        
        for pixel in pattern:
            for channel_value in pixel:
                # Corrected variable name from channel_byte to channel_value
                f.write(int(channel_value).to_bytes(1, byteorder='big'))

# File parameters
filename = "./tmp/custom_channels.pnm"
width, height = 100, 100  # Image dimensions
channels = 4  # Including RGB + Alpha

create_pnm_with_extra_channels(filename, width, height, channels)