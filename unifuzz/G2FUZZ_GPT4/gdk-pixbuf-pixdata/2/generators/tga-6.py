import os

def create_tga_with_footer():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define a simple 2x2 pixel image (RGBA, 32 bits per pixel)
    width, height = 2, 2
    pixels = [
        0xFF, 0x00, 0x00, 0xFF,  # Red pixel
        0x00, 0xFF, 0x00, 0xFF,  # Green pixel
        0x00, 0x00, 0xFF, 0xFF,  # Blue pixel
        0xFF, 0xFF, 0x00, 0xFF   # Yellow pixel
    ]
    
    # Convert the pixel data to bytes
    pixel_data = bytes(pixels)
    
    # TGA Header for 32 bits per pixel image
    tga_header = bytes([
        0,                      # ID length
        0,                      # Color map type
        2,                      # Image type (2 for uncompressed true-color image)
        0, 0, 0, 0, 0,          # Color map specification
        0, 0,                   # X-origin (low, high)
        0, 0,                   # Y-origin (low, high)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (low, high)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (low, high)
        32,                     # Pixel depth
        0                       # Image descriptor
    ])
    
    # TGA Footer
    tga_footer = bytes([
        0, 0, 0, 0,             # Extension area offset
        0, 0, 0, 0,             # Developer directory offset
        ord('T'), ord('R'), ord('U'), ord('E'), ord('V'), ord('I'), ord('S'), ord('I'), ord('O'), ord('N'), ord('-'), ord('X'), ord('F'), ord('I'), ord('L'), ord('E'), ord('.'), ord('0'), ord('0')
    ])
    
    # Write the TGA file
    with open('./tmp/example.tga', 'wb') as f:
        f.write(tga_header + pixel_data + tga_footer)

create_tga_with_footer()