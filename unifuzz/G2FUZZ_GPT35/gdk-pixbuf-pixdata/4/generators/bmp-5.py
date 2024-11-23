import numpy as np
import cv2

# Define text and font properties
text = "Platform Independence: BMP files are widely supported across different platforms and applications."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (255, 255, 255)  # white color
font_thickness = 1

# Create a blank image
height, width = 100, 700
image = np.zeros((height, width, 3), dtype=np.uint8)

# Add text to the image
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Save the image as a BMP file
filename = "./tmp/platform_independence.bmp"
cv2.imwrite(filename, image)

print(f"Image saved as {filename}")