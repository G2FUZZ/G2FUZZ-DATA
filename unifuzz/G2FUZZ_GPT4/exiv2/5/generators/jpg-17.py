import numpy as np
import cv2
import os

def add_watermark(image, watermark_text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, font_thickness=2, color=(255, 255, 255)):
    """
    Adds a semi-transparent watermark text on the given image.

    Parameters:
    - image: The background image on which the watermark text is to be added.
    - watermark_text: The text of the watermark.
    - position: The position where the watermark text is to be placed.
    - font: The font type of the watermark text.
    - font_scale: The scale of the font used for the watermark text.
    - font_thickness: The thickness of the font used for the watermark text.
    - color: The color of the watermark text.
    """
    overlay = image.copy()
    cv2.putText(overlay, watermark_text, position, font, font_scale, color, font_thickness)
    # Adjust the opacity of the watermark (0.3 in this case)
    opacity = 0.3
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)
    return image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 256x256 gradient image
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    value = i
    gradient[i, :, :] = [value, value, value]

# Add a digital watermark
watermark_text = "Copyright 2023"
gradient_with_watermark = add_watermark(gradient, watermark_text, position=(10, height - 10))

# Save the image with high compression (low quality)
cv2.imwrite('./tmp/gradient_low_quality_with_watermark.jpg', gradient_with_watermark, [int(cv2.IMWRITE_JPEG_QUALITY), 10])

print("Image generated and saved with lossy compression and digital watermarking.")