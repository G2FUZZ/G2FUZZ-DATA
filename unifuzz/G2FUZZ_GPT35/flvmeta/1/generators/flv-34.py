import cv2
import numpy as np

# Create a VideoWriter object with Dynamic streaming feature
video_codec = cv2.VideoWriter_fourcc(*'FLV1')
output = cv2.VideoWriter('./tmp/generated_video_complex_structure.flv', video_codec, 30, (640, 480))

# Generate a sample frame with Dynamic streaming and audio data
frame = np.zeros((480, 640, 3), dtype=np.uint8) + 255  # Create a white image
frame = cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), -1)  # Draw a red filled rectangle

# Simulated audio data
audio_data = np.random.randint(0, 255, size=(480, 640, 3)).astype(np.uint8)

# Write the frame with audio data to the video
for _ in range(100):
    output.write(np.concatenate((frame, audio_data), axis=2))

# Release the VideoWriter object
output.release()