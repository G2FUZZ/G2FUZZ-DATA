import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 256x256 gradient image
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    value = i
    gradient[i, :, :] = [value, value, value]

# Custom quantization tables optimized for human vision
# These tables are more heavily quantized in high-frequency areas where human eyes are less sensitive,
# following the principles of perceptual coding.
custom_quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
], dtype=np.uint8)

# Note on Optimization for Human Vision:
# To truly implement an optimization for human vision, one would ideally adjust the quantization tables based on 
# perceptual models, such as the JPEG psycho-visual model, which are designed to better align with human visual 
# sensitivity to different spatial frequencies. For this example, we use a custom table with the idea that it could 
# be optimized, but actual optimization would require a deeper integration with the JPEG encoding process and potentially
# use psychovisual tuning parameters or use a library specialized in perceptual encoding.

# Save the image with a simulated approach to 'Optimization for Human Vision'
# Since OpenCV does not expose direct control over the specific aspects of the JPEG compression algorithm such as 
# custom quantization tables directly in a way that would allow for perceptual optimization without additional steps,
# the demonstration here remains conceptual for the 'Optimization for Human Vision'. Advanced usage might require 
# directly manipulating the JPEG encoding process using a library that provides low-level access to the encoder settings.

cv2.imwrite('./tmp/gradient_optimized_for_human_vision.jpg', gradient, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

print("Image generated and potentially saved with an approach simulating 'Optimization for Human Vision'.")