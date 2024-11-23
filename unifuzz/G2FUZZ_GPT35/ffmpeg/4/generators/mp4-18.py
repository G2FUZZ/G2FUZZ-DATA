import cv2
import numpy as np
import subprocess

# Create a black image
frame = np.zeros((720, 1280, 3), dtype=np.uint8)

# Add text for closed captions
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50, 700)
fontScale = 1
fontColor = (255, 255, 255)
lineType = 2

cv2.putText(frame, 'Closed Captions', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

# Save the frame as an mp4 file with text tracks
out = cv2.VideoWriter('./tmp/closed_captions_text_tracks.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (1280, 720), True)
for _ in range(100):
    out.write(frame)

out.release()

# Add text tracks to the mp4 file
subprocess.call(['ffmpeg', '-i', './tmp/closed_captions_text_tracks.mp4', '-f', 'srt', '-i', 'subtitle.srt', '-c', 'copy', '-c:s', 'mov_text', 'output_with_text_tracks.mp4'])