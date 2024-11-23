from PIL import Image, ImageDraw
import numpy as np
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# HDR support in PNG through bit depth and color modes is limited and not natively supported as in formats like HDR or EXR.
# However, we can simulate a higher dynamic range by manipulating the image's contrast and brightness.
# For true HDR support, consider converting to a format that supports HDR natively.

# Create an image with transparent background
width, height = 400, 400
image = Image.new("RGBA", (width, height), (255, 0, 0, 0))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Draw a semi-transparent red circle in the center
circle_radius = 100
circle_center = (width // 2, height // 2)
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius], 
             fill=(255, 0, 0, 128))  # Semi-transparent red

# Convert image to an array for manipulation
img_array = np.array(image)

# Manipulate the array to simulate HDR:
# Increase contrast by scaling the differences from the mean, then clipping to valid range
mean = np.mean(img_array, axis=(0, 1), keepdims=True)
contrast_factor = 1.5  # Adjust this factor to simulate different levels of HDR effect
img_array = np.clip((img_array - mean) * contrast_factor + mean, 0, 255).astype(np.uint8)

# Convert back to PIL Image
hdr_image = Image.fromarray(img_array)

# Save the image with transparency and simulated HDR effect
hdr_image.save('./tmp/hdr_transparent_circle.png')