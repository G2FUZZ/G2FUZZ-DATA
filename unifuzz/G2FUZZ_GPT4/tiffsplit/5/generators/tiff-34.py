from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image for demonstration purposes
def create_image(width, height, color):
    image = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Sample", fill="black")
    return image

# Create multiple images
image1 = create_image(100, 100, "red")
image2 = create_image(100, 100, "green")
image3 = create_image(100, 100, "blue")

# Save images as a multi-page TIFF with LZW compression and Predictor Tag
tiff_path = os.path.join(output_dir, 'multi_image_with_predictor.tiff')

# When saving the TIFF, specify compression as 'tiff_lzw' (LZW compression) and predictor as '2'
# Also include SMinSampleValue and SMaxSampleValue tags
# 340 (SMinSampleValue) and 341 (SMaxSampleValue) tags are used to specify the minimum and maximum sample values
image1.save(
    tiff_path, 
    save_all=True, 
    compression="tiff_lzw", 
    append_images=[image2, image3],
    tiffinfo={317: 2,  # 317 is the tag number for Predictor
              340: (0,),  # Assuming the minimum sample value is 0 for all samples
              341: (255,)}  # Assuming the maximum sample value is 255 for all samples
)