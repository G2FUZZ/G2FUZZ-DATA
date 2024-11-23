from PIL import Image, ImageDraw
import os

# Helper function to generate resolution info
def generate_res_info(dpi):
    # Convert DPI to TIFF resolution unit (pixels per inch to pixels per centimeter)
    res = dpi * 2.54 / 10
    return (int(res), int(res))

def create_patterned_image(color_space, size=(800, 600), dpi=300):
    # Create a new image with the specified color space and size
    image = Image.new(color_space, size)
    
    # Draw some simple patterns or colors as an example
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0], 100):
        for y in range(0, size[1], 100):
            color = tuple((x % 255, y % 255, (x + y) % 255)[:len(image.getbands())])  # Adapt color based on color space
            draw.rectangle([x, y, x + 99, y + 99], fill=color)
    
    # Set DPI resolution
    res = generate_res_info(dpi)
    image.info['dpi'] = res
    
    return image

def convert_color_space(image, color_space):
    # Converting the image to the specified color space
    return image.convert(color_space)

def save_multi_page_tiff(images, file_path, resolutions, metadata):
    # Save the images in TIFF format with multiple pages, varying resolutions, and metadata
    images[0].save(
        file_path, 
        save_all=True, 
        append_images=images[1:], 
        format='TIFF', 
        compression='tiff_deflate',
        dpi=resolutions[0],  # Apply resolution for the first image
        tiffinfo={270: metadata["Description"], 315: metadata["Artist"], 305: metadata["Software"]}
    )

# Define the base image sizes and DPIs
image_sizes = [(800, 600), (1600, 1200), (400, 300)]
dpis = [300, 600, 150]

# Create images in different color spaces with varying sizes and resolutions
rgb_image = create_patterned_image("RGB", image_sizes[0], dpis[0])
cmyk_image = create_patterned_image("CMYK", image_sizes[1], dpis[1])
grayscale_image = create_patterned_image("L", image_sizes[2], dpis[2])

# Specify the directory and filename for the TIFF
output_dir = './tmp/'
output_filename = 'complex_structure_image.tiff'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Prepare resolutions list for images
resolutions = [generate_res_info(dpi) for dpi in dpis]

# Prepare metadata
metadata = {
    "Artist": "Python PIL",
    "Software": "Pillow",
    "Description": "Multi-page TIFF with varying color models, sizes, and resolutions"
}

# Combine the images into a multi-page TIFF with varying resolutions and metadata
save_multi_page_tiff([rgb_image, cmyk_image, grayscale_image], os.path.join(output_dir, output_filename), resolutions, metadata)

print(f"Multi-page TIFF saved as {output_filename} in {output_dir}")