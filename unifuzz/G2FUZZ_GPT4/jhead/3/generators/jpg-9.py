import os
import cv2
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an original image with text
original_image = np.zeros((200, 400, 3), dtype=np.uint8)
original_image.fill(255)  # Make the background white

# Put some text on the image
cv2.putText(original_image, 'Original Image', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Save the original image
original_path = './tmp/original.jpg'
cv2.imwrite(original_path, original_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Load and re-save the image multiple times to simulate quality loss
for i in range(10):
    # Load the image
    img = cv2.imread(original_path)
    
    # Save it again with a quality of 90% to simulate loss
    edited_path = f'./tmp/edited_{i + 1}.jpg'
    cv2.imwrite(edited_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    
    # Update the original_path so the next iteration loads this newly saved image
    original_path = edited_path

print("Images have been saved in ./tmp/")