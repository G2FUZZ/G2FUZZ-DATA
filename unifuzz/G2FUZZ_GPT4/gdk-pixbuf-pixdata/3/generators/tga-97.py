import os
import struct

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image metadata and settings
image_description = "Advanced TGA Demo"
width, height = 800, 400
pixels = [(255, 255, 255, 255) for _ in range(width * height)]  # White background

def create_tga_header(width, height, image_description):
    """
    Creates a TGA header with an image ID field for metadata.
    """
    # TGA Header fields
    id_length = len(image_description)
    colormap_type = 0
    image_type = 2  # Uncompressed, true-color image
    colormap_spec = (0, 0, 0, 0)  # Colormap specification (not used)
    x_origin = 0
    y_origin = 0
    pixel_depth = 32  # 32 bits per pixel (RGBA)
    image_descriptor = 8  # 8 bits of alpha channel information
    
    header = struct.pack('<BBBBHHBHHHHBB',
                         id_length,
                         colormap_type,
                         image_type,
                         *colormap_spec,
                         x_origin,
                         y_origin,
                         width,
                         height,
                         pixel_depth,
                         image_descriptor)
    
    return header

def create_tga_footer():
    """
    Creates a TGA footer for Truevision TGA files.
    """
    extension_area_offset = 0
    developer_directory_offset = 0
    signature = "TRUEVISION-XFILE.\x00"
    
    footer = struct.pack('<II18s',
                         extension_area_offset,
                         developer_directory_offset,
                         bytes(signature, 'ascii'))
    
    return footer

def save_tga(filename, width, height, pixels, image_description):
    """
    Saves an image as a TGA file with a header, pixel data, and footer.
    """
    header = create_tga_header(width, height, image_description)
    footer = create_tga_footer()
    
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(bytes(image_description, 'ascii'))
        
        # Write pixel data (BGRA)
        for pixel in pixels:
            b, g, r, a = pixel
            f.write(struct.pack('<BBBB', b, g, r, a))
        
        f.write(footer)

# Convert the image pixel data to BGRA format (if necessary)
# For this example, the pixels are already in RGBA format, which is suitable for TGA

# Save the image as a TGA file with metadata and a footer
tga_filename = './tmp/advanced_versatility_in_application.tga'
save_tga(tga_filename, width, height, pixels, image_description)

print(f"Saved advanced TGA file to {tga_filename}")