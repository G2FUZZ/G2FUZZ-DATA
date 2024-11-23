from PIL import Image, ImageDraw, ImageSequence
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a simple image for demonstration purposes
def generate_image(mode, size, color, text):
    image = Image.new(mode, size, color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill='black')
    return image

# Generate different images for the TIFF pages
image1 = generate_image("RGB", (100, 100), "red", "Image 1: RGB Red")
image2 = generate_image("RGB", (100, 100), "green", "Image 2: RGB Green")
image3 = generate_image("RGB", (100, 100), "blue", "Image 3: RGB Blue")

# Create a floating-point image
width, height = 100, 100
float_data = np.random.rand(height, width).astype('float32')

# Scale the floating-point data to the 0-255 range
scaled_data = (255 * (float_data - np.min(float_data)) / np.ptp(float_data)).astype('uint8')

# Replicate the scaled data across three channels to create an 'RGB' image
rgb_data = np.stack((scaled_data,)*3, axis=-1)

# Convert the RGB data to an 'RGB' image with text
image4 = Image.fromarray(rgb_data, 'RGB')
draw = ImageDraw.Draw(image4)
draw.text((10, 10), "Image 4: Floating-point Data", fill='black')

# Path for the output TIFF
tiff_output_path = './tmp/multiple_images_with_float_data.tiff'

# Save as multi-page TIFF
image1.save(
    tiff_output_path,
    save_all=True,
    append_images=[image2, image3, image4],
    compression="tiff_deflate",
    dpi=(300.0, 300.0),
    tiffinfo={
        317: 2,
        270: "Multi-page TIFF with varying content and custom metadata."
    }
)

print("TIFF file with multiple images, including converted floating-point data, created successfully.")

# If needed, here's how to read and inspect the generated TIFF file
with Image.open(tiff_output_path) as img:
    for i, page in enumerate(ImageSequence.Iterator(img)):
        print(f"Page {i+1}: Mode={page.mode}, Size={page.size}")
        # Perform operations per page here
        # page.show()  # Uncomment to display each page