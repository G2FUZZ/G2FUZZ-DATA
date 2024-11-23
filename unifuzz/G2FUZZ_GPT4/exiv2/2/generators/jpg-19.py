from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Perform a lossless crop and rotate operation
# For demonstration, let's crop the image to 50x50 pixels and rotate it by 90 degrees
# Note: These operations are not truly lossless in the context of this PIL manipulation,
# because we're not operating on encoded JPEG bytes but on the decoded image data.
# True lossless operations require manipulating the JPEG's internal structure, which is beyond PIL's capabilities.
crop_box = (25, 25, 75, 75)
cropped_image = image.crop(crop_box)
rotated_image = cropped_image.rotate(90)

# Save the cropped and rotated image with an optimization option that includes Huffman coding
rotated_image.save('./tmp/simple_image_with_huffman_cropped_rotated.jpg', 'JPEG', optimize=True)

print("Cropped and rotated image was saved with Huffman Coding as part of the JPEG optimization.")