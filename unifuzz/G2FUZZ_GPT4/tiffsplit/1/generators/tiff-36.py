from PIL import Image, ImageDraw
import os

def create_patterned_image(color_space, size=(800, 600)):
    # Create a new image with the specified color space and size
    image = Image.new(color_space, size)

    # Draw some simple patterns or colors as an example
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0], 100):
        for y in range(0, size[1], 100):
            color = tuple((x % 255, y % 255, (x + y) % 255)[:len(image.getbands())])  # Adapt color based on color space
            draw.rectangle([x, y, x + 99, y + 99], fill=color)
    
    return image

def convert_color_space(image, color_space):
    # Converting the image to the specified color space
    return image.convert(color_space)

def save_multi_page_tiff(images, file_path, tile_size=(256, 256)):
    # Save the images in TIFF format with tiling enabled and in the specified color spaces
    images[0].save(file_path, save_all=True, append_images=images[1:], 
                   format='TIFF', tile=tile_size, compression='tiff_deflate')

# Define the base image size
image_size = (800, 600)

# Create images in different color spaces
rgb_image = create_patterned_image("RGB", image_size)
cmyk_image = convert_color_space(rgb_image, "CMYK")
grayscale_image = convert_color_space(rgb_image, "L")

# Specify the directory and filename for the TIFF
output_dir = './tmp/'
output_filename = 'complex_structure_image.tiff'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Combine the images into a multi-page TIFF
save_multi_page_tiff([rgb_image, cmyk_image, grayscale_image], os.path.join(output_dir, output_filename))

print(f"Multi-page TIFF saved as {output_filename} in {output_dir}")