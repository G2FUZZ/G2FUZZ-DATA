import numpy as np
import os

def create_complex_pgx_file(filename, width, height, bit_depth, color_mode='grayscale', endian='little', include_metadata=False):
    """
    Creates a complex PGX file with additional features such as support for multiple color channels,
    variable endianness, and optional metadata comments.

    Parameters:
    - filename: Name of the file to save, including path.
    - width: Width of the image.
    - height: Height of the image.
    - bit_depth: Bit depth of the image.
    - color_mode: Color mode of the image ('grayscale', 'RGB', or 'RGBA').
    - endian: Endianness of the data ('little' or 'big').
    - include_metadata: Whether to include metadata comments in the file.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    channel_count = {'grayscale': 1, 'RGB': 3, 'RGBA': 4}[color_mode]
    max_val = 2**bit_depth - 1
    
    # Generate a gradient image for each channel
    img = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))
    if color_mode != 'grayscale':
        img = np.stack([img for _ in range(channel_count)], axis=-1)
    
    # Open file in binary mode to write
    with open(filename, 'wb') as file:
        # Write optional metadata as comments
        if include_metadata:
            metadata = f'# Created with {color_mode} mode, {bit_depth}-bit depth, {endian} endianness\n'.encode()
            file.write(metadata)
        
        # Write the PGX header
        endian_flag = 'M' if endian == 'big' else 'L'
        header = f'PG {endian_flag} {bit_depth} {width} {height}\n'.encode()
        file.write(header)
        
        # Write the image data
        if bit_depth > 8:
            # For bit depths greater than 8, adjust endianness if necessary
            if endian == 'big':
                img_bytes = img.astype(np.uint16).byteswap().tobytes()
            else:
                img_bytes = img.astype(np.uint16).tobytes()
        else:
            img_bytes = img.astype(np.uint8).tobytes()
        
        file.write(img_bytes)
        
# Example usage
create_complex_pgx_file('./tmp/complex_example.pgx', 256, 256, 16, color_mode='RGBA', endian='little', include_metadata=True)