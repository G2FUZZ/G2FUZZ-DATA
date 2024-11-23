from PIL import Image, TiffTags, TiffImagePlugin, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create images with varying properties
def create_image(size, color, text, color_space="RGB"):
    if color_space == "L":  # Grayscale
        image = Image.new("L", size, color=1)  # 1 for white in grayscale
    else:  # Default to RGB
        image = Image.new("RGB", size, color=color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black" if color_space == "RGB" else 255)
    return image

# Create multiple images with varying properties
image1 = create_image((100, 100), (255, 0, 0), "Page 1")
image2 = create_image((150, 150), 0, "Page 2", color_space="L")  # Grayscale
image3 = create_image((200, 100), (0, 0, 255), "Page 3")

# Save images as a multi-page TIFF
tiff_path = './tmp/multi_feature_tiff_with_metadata.tiff'
image1.save(
    tiff_path,
    save_all=True,
    compression="tiff_lzw",
    append_images=[image2, image3]
)

print(f"Generated TIFF with complex file structures at {tiff_path}")