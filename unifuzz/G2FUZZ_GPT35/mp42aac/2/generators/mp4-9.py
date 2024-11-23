import numpy as np
import cv2

# Create a black image
height, width = 240, 320
black_img = np.zeros((height, width, 3), np.uint8)

# Write text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello, mp4!"
textsize = cv2.getTextSize(text, font, 1, 2)[0]
textX = (width - textsize[0]) // 2
textY = (height + textsize[1]) // 2
cv2.putText(black_img, text, (textX, textY), font, 1, (255, 255, 255), 2)

# Save the image as an mp4 file
out = cv2.VideoWriter('./tmp/generated.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))
for _ in range(50):
    out.write(black_img)
out.release()