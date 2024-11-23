from PIL import Image
import numpy as np
import os
import cv2

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with a gradient
width, height = 800, 600
image = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        # Gradient from black to white
        value = int((x / width) * 255)
        image.putpixel((x, y), (value, value, value))

# Save the original image with JPEG compression
image_path = './tmp/gradient_image.jpg'
image.save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

# Apply Discrete Cosine Transform (DCT) on the image
def apply_dct(image_path):
    # Convert image to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Convert to float32 for higher precision before applying DCT
    img_float32 = np.float32(img)
    
    # Perform DCT
    dct_img = cv2.dct(img_float32)
    
    # Normalize the results to 0-255
    dct_img = cv2.normalize(dct_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    # Convert back to uint8
    dct_img_uint8 = np.uint8(dct_img)
    
    # Save the DCT image
    dct_image_path = './tmp/gradient_image_dct.jpg'
    cv2.imwrite(dct_image_path, dct_img_uint8)
    return dct_image_path

# Apply DCT and save the new image
dct_image_path = apply_dct(image_path)

print(f"Original image saved to {image_path}")
print(f"DCT image saved to {dct_image_path}")