import numpy as np
import os

def create_advanced_pgx_file(filename, width, height, bit_depth, endian="little", gradient_type="horizontal", metadata=None):
    """
    Creates a PGX file with a gradient demonstrating bit-depth support, and allows for more complex features.

    Parameters:
    - filename: Name of the file to save, including path.
    - width: Width of the image.
    - height: Height of the image.
    - bit_depth: Bit depth of the image.
    - endian: Byte order ('little' or 'big'). Defaults to 'little'.
    - gradient_type: Type of gradient ('horizontal', 'vertical', or 'diagonal'). Defaults to 'horizontal'.
    - metadata: Optional metadata string to include as a comment in the PGX file header.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Generate a gradient image
    max_val = 2**bit_depth - 1
    if gradient_type == "horizontal":
        img = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))
    elif gradient_type == "vertical":
        img = np.tile(np.linspace(0, max_val, height, dtype=np.uint16), (width, 1)).T
    elif gradient_type == "diagonal":
        img = np.linspace(0, max_val, max(width, height), dtype=np.uint16)
        img = np.outer(img, img) / max_val
        img = img[:height, :width]  # Adjust the diagonal gradient to fit the image size
    
    # Open file in binary mode to write
    with open(filename, 'wb') as file:
        # Write the PGX header
        endian_indicator = "ML" if endian == "little" else "MM"
        header_lines = [
            f"PG {endian_indicator} {bit_depth} {width} {height}\n"
        ]
        if metadata:
            header_lines.append(f"# {metadata}\n")
        header = ''.join(header_lines).encode()
        file.write(header)
        
        # Adjust byte order based on the endian parameter
        if endian == "little":
            dtype = np.uint16 if bit_depth > 8 else np.uint8
        else:
            dtype = ">u2" if bit_depth > 8 else ">u1"
        
        # Write the image data
        img_bytes = img.astype(dtype).tobytes()
        file.write(img_bytes)
        
# Example usage
create_advanced_pgx_file(
    './tmp/advanced_example.pgx', 
    256, 
    256, 
    16, 
    endian="big", 
    gradient_type="diagonal",
    metadata="Example PGX with diagonal gradient and big-endian format"
)