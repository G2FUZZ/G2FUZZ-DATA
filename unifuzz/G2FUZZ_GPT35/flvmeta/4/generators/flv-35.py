import os
import numpy as np
import cv2

# Create a new directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample video frame with audio data
frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
audio_data = np.random.randint(-32768, 32767, 44100)  # Audio data for 1 second at 44.1 kHz

# Write the sample video frame and audio data to an FLV file
output_file = os.path.join(output_dir, 'sample_complex.flv')
fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # FLV codec
out = cv2.VideoWriter(output_file, fourcc, 30.0, (640, 480))

# Simulate writing video frames with corresponding audio data
for _ in range(100):
    out.write(frame)
    out.write(np.zeros((480, 640, 3), dtype=np.uint8))  # Simulate blank frames
out.release()

# Write audio data to a separate file for FLV format
audio_file = os.path.join(output_dir, 'audio_data.flv')
with open(audio_file, 'wb') as audio_out:
    audio_out.write(audio_data.tobytes())

print(f'Complex FLV file generated with audio: {output_file}')