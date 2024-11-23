import cv2
import numpy as np

# Create a black image
frame = np.zeros((720, 1280, 3), dtype=np.uint8)

# Add text for closed captions
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50, 700)
fontScale = 1
fontColor = (255, 255, 255)
lineType = 2

cv2.putText(frame, 'Closed Captions', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

# Add user-specific data
userDataText = 'User data: MP4 files can include user data fields for storing custom user-specific information.'
userDataPosition = (50, 50)
cv2.putText(frame, userDataText, userDataPosition, font, fontScale, fontColor, lineType)

# Save the frame as an mp4 file
out = cv2.VideoWriter('./tmp/closed_captions_with_user_data.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (1280, 720))
for _ in range(100):
    out.write(frame)

out.release()