from PIL import Image, TiffImagePlugin
import os  # Make sure this import statement is included

# Define image sizes and tile sizes for multiple pages
image_sizes = [(800, 600), (640, 480)]  # Width, Height for each page
tile_size = (256, 256)  # Width, Height

# Define patterns or colors for each page
def draw_pattern(image, pattern_id):
    width, height = image.size
    for x in range(0, width, 100):
        for y in range(0, height, 100):
            for i in range(100):
                for j in range(100):
                    if x + i < width and y + j < height:
                        if pattern_id % 2 == 0:
                            image.putpixel((x+i, y+j), (x % 255, y % 255, (x+y) % 255))
                        else:
                            image.putpixel((x+i, y+j), ((x+y) % 255, x % 255, y % 255))

# Specify the directory and filename for the TIFF
output_dir = './tmp/'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize a list to hold individual images (pages)
images = []

# Create multiple images for each page
for idx, image_size in enumerate(image_sizes):
    # Create a new image with RGB mode
    image = Image.new("RGB", image_size)
    
    # Apply a different pattern or color scheme based on page index
    draw_pattern(image, idx)
    
    # Append to list of images
    images.append(image)

# Define a custom TIFF tag for demonstration
custom_tag = {
    65000: (TiffImagePlugin.IFDRational(42, 1),),  # Example with a rational number
}

# Save the images as a multi-page TIFF
output_filename = 'multi_page_tiled_image.tiff'
with TiffImagePlugin.AppendingTiffWriter(os.path.join(output_dir, output_filename), True) as tf:
    for idx, img in enumerate(images):
        # Define page-specific TIFF info
        info = TiffImagePlugin.ImageFileDirectory_v2()
        for tag, value in custom_tag.items():
            info[tag] = value
        
        # Use a different compression method for each page as a demonstration
        compression_method = 'tiff_adobe_deflate' if idx % 2 == 0 else 'tiff_lzw'
        
        # Save the current page
        img.save(tf,
                 format='TIFF',
                 tile=tile_size,
                 compression=compression_method,
                 tiffinfo=info,
                 save_all=True)
        tf.newFrame()

print(f"Multi-page TIFF image saved as {output_filename} in {output_dir}")