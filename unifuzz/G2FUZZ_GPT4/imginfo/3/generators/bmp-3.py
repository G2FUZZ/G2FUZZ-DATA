import os

def create_rle_bmp(filename):
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)
    
    # BMP Header + DIB Header for an 8-bit RLE compressed image of 2x2 pixels
    bmp_header = bytes([
        0x42, 0x4D, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x3E, 0x00, 0x00, 0x00, 0x28, 0x00, 
        0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 
        0x00, 0x00, 0x01, 0x00, 0x08, 0x00, 0x01, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x13, 0x0B, 
        0x00, 0x00, 0x13, 0x0B, 0x00, 0x00, 0x02, 0x00, 
        0x00, 0x00, 0x02, 0x00, 0x00, 0x00])
    
    # Color Table (Palette): 2 colors
    color_table = bytes([
        0xFF, 0x00, 0x00, 0x00,  # Red
        0x00, 0xFF, 0x00, 0x00   # Green
    ])
    
    # Pixel Data with RLE Compression: 2x2 image, 2 pixels of each color
    # Format: [Count, ColorIndex]
    pixel_data = bytes([
        0x02, 0x00,  # 2 red pixels
        0x02, 0x01,  # 2 green pixels
        0x00, 0x00,  # End of line
        0x00, 0x00,  # End of line
        0x00, 0x01   # End of RLE bitmap
    ])
    
    with open(filepath, 'wb') as f:
        f.write(bmp_header)
        f.write(color_table)
        f.write(pixel_data)

    print(f"RLE compressed BMP file saved as: {filepath}")

# Create a simple 2x2 RLE compressed BMP file
create_rle_bmp('rle_image.bmp')