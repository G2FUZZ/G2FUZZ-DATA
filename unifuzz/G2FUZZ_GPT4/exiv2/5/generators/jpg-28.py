import numpy as np
import cv2
import os

def add_watermark(image, watermark_text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, font_thickness=2, color=(255, 255, 255), opacity=0.3):
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
    - opacity: The opacity of the watermark text.
    """
    overlay = image.copy()
    cv2.putText(overlay, watermark_text, position, font, font_scale, color, font_thickness)
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)
    return image

def add_printing_support(image, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, font_thickness=1, color=(255, 255, 255), position=None):
    """
    Adds a 'Support for Printing' watermark to indicate the image is suitable for printing.

    Parameters:
    - image: The image to add the printing support watermark to.
    - font: The font type of the printing support watermark.
    - font_scale: The scale of the font used.
    - font_thickness: The thickness of the font used.
    - color: The color of the font.
    - position: The position to place the watermark. If None, it's placed at the bottom right corner.
    """
    if position is None:
        text = "Support for Printing"
        # Calculate the size of the text box
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        position = (image.shape[1] - text_size[0] - 10, image.shape[0] - 10)
    image = add_watermark(image, "Support for Printing", position, font, font_scale, font_thickness, color, opacity=0.5)
    return image

def add_wide_range_use_cases(image, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, font_thickness=1, color=(255, 255, 255), position=None):
    """
    Adds a 'Wide Range of Use Cases' watermark to indicate the JPEG format's versatility.

    Parameters:
    - image: The image to add the 'Wide Range of Use Cases' watermark to.
    - font: The font type of the watermark.
    - font_scale: The scale of the font used.
    - font_thickness: The thickness of the font used.
    - color: The color of the font.
    - position: The position to place the watermark. If None, it's placed at the top right corner.
    """
    if position is None:
        text = "Wide Range of Use Cases"
        # Calculate the size of the text box
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        position = (image.shape[1] - text_size[0] - 10, 30)  # Adjust the Y position as needed
    image = add_watermark(image, "Wide Range of Use Cases", position, font, font_scale, font_thickness, color, opacity=0.5)
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

# Add 'Support for Printing' feature
gradient_with_printing_support = add_printing_support(gradient_with_watermark)

# Add 'Wide Range of Use Cases' feature
gradient_with_all_features = add_wide_range_use_cases(gradient_with_printing_support)

# Save the image with high compression (low quality)
cv2.imwrite('./tmp/gradient_low_quality_with_all_features.jpg', gradient_with_all_features, [int(cv2.IMWRITE_JPEG_QUALITY), 10])

print("Image generated and saved with lossy compression, digital watermarking, support for printing feature, and wide range of use cases feature.")