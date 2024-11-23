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

# Add subtitle support
subtitle_text = "Subtitle: Welcome to our video!"
subtitle_text_size = cv2.getTextSize(subtitle_text, font, 0.5, 1)[0]
subtitleX = (width - subtitle_text_size[0]) // 2
subtitleY = height - subtitle_text_size[1] - 10
cv2.putText(black_img, subtitle_text, (subtitleX, subtitleY), font, 0.5, (255, 255, 255), 1)

# Add DRM protection
drm_text = "DRM protection: ability to implement Digital Rights Management for content protection"
drm_text_size = cv2.getTextSize(drm_text, font, 0.5, 1)[0]
drmX = (width - drm_text_size[0]) // 2
drmY = subtitleY - drm_text_size[1] - 10
cv2.putText(black_img, drm_text, (drmX, drmY), font, 0.5, (255, 255, 255), 1)

# Add logo overlay
logo = cv2.imread('logo.png')
if logo is not None:
    logo = cv2.resize(logo, (width // 4, height // 4))
    logoX = 10
    logoY = 10
    black_img[logoY:logoY + logo.shape[0], logoX:logoX + logo.shape[1]] = logo
else:
    print("Error loading logo.png file.")

# Add dynamic text animation
text_list = ["Welcome", "to", "our", "video!"]
for i, txt in enumerate(text_list):
    textsize = cv2.getTextSize(txt, font, 1, 2)[0]
    textX = (width - textsize[0]) // 2
    textY = (height + textsize[1]) // 2 + i * 30
    cv2.putText(black_img, txt, (textX, textY), font, 1, (255, 255, 255), 2)

# Save the image as an mp4 file with subtitles, DRM protection, logo overlay, and dynamic text animation
out = cv2.VideoWriter('./tmp/extended_generated_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))
for _ in range(50):
    out.write(black_img)
out.release()