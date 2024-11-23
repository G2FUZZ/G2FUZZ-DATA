import numpy as np
import cv2

# Generate a random video frame with text overlay
def add_text_overlay(img, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottom_left_corner = (10, 30)
    font_scale = 1
    font_color = (255, 255, 255)
    line_type = 2
    cv2.putText(img, text, bottom_left_corner, font, font_scale, font_color, line_type)

height, width = 240, 320
frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
quiz_frame = np.zeros((height, width, 3), dtype=np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/random_video_with_quiz_extended.flv', fourcc, 30, (width, height))

for i in range(100):
    out.write(frame)
    if i % 10 == 0:
        add_text_overlay(quiz_frame, "Question: What is the capital of France?")
        out.write(quiz_frame)

# Varying frame durations
frame_duration = [30] * 90 + [60] * 10  # Set frame duration to 60ms for quiz frames
for i, duration in enumerate(frame_duration):
    for _ in range(duration):
        out.write(frame)

out.release()
