import numpy as np
import cv2

# Define text and font properties
text = "Platform Independence: BMP files are widely supported across different platforms and applications."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (255, 255, 255)  # white color
font_thickness = 1

# Create a blank image
height, width = 200, 800
image = np.zeros((height, width, 3), dtype=np.uint8)

# Add a gradient background to the image
for i in range(height):
    for j in range(width):
        image[i, j] = [i // 3, j // 3, 255]  # Gradient from blue to white

# Add a rectangle to the image
rectangle_color = (0, 255, 0)  # green color
cv2.rectangle(image, (50, 50), (250, 150), rectangle_color, -1)  # Filled rectangle

# Add text to the image
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Save the image as a BMP file
filename = "./tmp/complex_structure.bmp"
cv2.imwrite(filename, image)

print(f"Image with complex file structures saved as {filename}")