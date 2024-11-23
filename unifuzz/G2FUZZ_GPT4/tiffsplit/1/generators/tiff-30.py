from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create multiple images to be stored in a single TIFF file
image1 = Image.new('RGB', (100, 100), color = 'red')
image2 = Image.new('RGB', (100, 100), color = 'green')
image3 = Image.new('RGB', (100, 100), color = 'blue')

# Create a floating-point image
width, height = 100, 100
float_data = np.random.rand(height, width).astype('float32')

# Scale the floating-point data to the 0-255 range
scaled_data = (255 * (float_data - np.min(float_data)) / np.ptp(float_data)).astype('uint8')

# Replicate the scaled data across three channels to create an 'RGB' image
rgb_data = np.stack((scaled_data,)*3, axis=-1)

# Convert the RGB data to an 'RGB' image
image4 = Image.fromarray(rgb_data, 'RGB')

# Function to add a simple watermark to an image
def add_watermark(image, text="Confidential", position=(0, 0), opacity=128):
    watermark = Image.new('RGBA', image.size)
    draw = ImageDraw.Draw(watermark, 'RGBA')
    
    # Try loading a font, or default to PIL's built-in font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text(position, text, fill=(255, 255, 255, opacity), font=font)
    
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)
    
    return watermarked_image.convert('RGB')

# Apply watermark to all the images
image1 = add_watermark(image1, text="Secured", position=(10, 10))
image2 = add_watermark(image2, text="Secured", position=(10, 10))
image3 = add_watermark(image3, text="Secured", position=(10, 10))
image4 = add_watermark(image4, text="Secured", position=(10, 10))

# Save the images as a multipage TIFF with JPEG Compression
image1.save('./tmp/multiple_images_with_security_features.tiff', save_all=True, compression="jpeg", append_images=[image2, image3, image4])

print("TIFF file with multiple images, including converted floating-point data and security features, created successfully.")