from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image for demonstration purposes
def create_image(width, height, color, text, color_space="RGB"):
    if color_space == "L":  # Grayscale
        image = Image.new("L", (width, height), color=1)  # 1 for white in grayscale
    else:  # Default to RGB
        image = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black" if color_space == "RGB" else 255)
    return image

# Create multiple images with varying properties
image1 = create_image(100, 100, "red", "Page 1")
image2 = create_image(150, 150, 0, "Page 2", color_space="L")  # Grayscale
image3 = create_image(200, 100, "blue", "Page 3")

# Save images as a multi-page TIFF with varying resolutions, color spaces, and custom metadata
tiff_path = os.path.join(output_dir, 'multi_feature_tiff.tiff')

# Define custom tags for each page to demonstrate complex file structures
# Custom tags can include unique metadata per page such as descriptions or page-specific information
custom_tags_page1 = {
    270: "First page description",  # 270 is the tag for ImageDescription
}
custom_tags_page2 = {
    270: "Second page, grayscale",
}
custom_tags_page3 = {
    270: "Third page with more info",
}

# Save the first image with its specific tags and setup for the rest of the images
image1.save(
    tiff_path,
    save_all=True,
    compression="tiff_lzw",
    dpi=(300.0, 300.0),  # Example of setting resolution for the first page
    append_images=[image2, image3],
    resolution=[(150.0, 150.0), (600.0, 300.0)],  # Varying resolutions for the subsequent pages
    tiffinfo={
        317: 2,  # Predictor tag for all pages
        **custom_tags_page1,
    }
)

# Unfortunately, PIL doesn't directly support setting varying tiffinfo or color modes per appended image out of the box.
# This limitation means that the additional complexity, such as per-page color space and custom per-page metadata,
# would need a more manual handling or a different library that supports these TIFF complexities in depth.

print(f"Generated TIFF with complex file structures at {tiff_path}")