import numpy as np
import cv2

# Define text and font properties
text = "Advanced BMP File Generation: This BMP file includes additional metadata and color channel manipulation."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_color = (255, 255, 255)  # white color
font_thickness = 1

# Create a blank image with different color channels
height, width = 150, 800
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :width//3] = [255, 0, 0]  # Blue channel
image[:, width//3:2*width//3] = [0, 255, 0]  # Green channel
image[:, 2*width//3:] = [0, 0, 255]  # Red channel

# Add text to the image
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Save the image as a BMP file
cv2.imwrite("./tmp/advanced_bmp_file.bmp", image)

print("Advanced BMP file saved successfully.")