import cv2
import numpy as np
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a frame with specific characteristics
def create_frame(width, height, color_bg, color_shape, shape, text):
    frame = np.zeros((height, width, 3), np.uint8)
    frame[:] = color_bg  # Background color

    # Draw shapes on the frame
    if shape == 'circle':
        cv2.circle(frame, (width // 2, height // 2), 100, color_shape, -1)
    elif shape == 'rectangle':
        cv2.rectangle(frame, (width // 4, height // 4), (3 * width // 4, 3 * height // 4), color_shape, -1)

    # Add text to the frame
    if text:
        cv2.putText(frame, text, (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame

# Generate an MP4 file with Progressive Sample Access and more complex structures
def generate_complex_video(filename):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480), True)

    # Title screen
    for _ in range(30):  # 1.5 seconds at 20 fps
        frame = create_frame(640, 480, (0, 0, 0), (0, 0, 0), None, "Title Screen")
        out.write(frame)

    # Sequence of different colored frames with shapes
    colors_bg = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    colors_shape = [(0, 255, 255), (255, 0, 255), (255, 255, 0)]
    shapes = ['circle', 'rectangle']

    for color_bg, color_shape in zip(colors_bg, colors_shape):
        for shape in shapes:
            for _ in range(20):  # 1 second per scene
                frame = create_frame(640, 480, color_bg, color_shape, shape, "")
                out.write(frame)

    # Ending screen
    for _ in range(30):  # 1.5 seconds at 20 fps
        frame = create_frame(640, 480, (0, 0, 0), (0, 0, 0), None, "The End")
        out.write(frame)

    out.release()

# Simple "encryption" - XOR operation on file bytes
def simple_encrypt_decrypt(filename):
    key = 123  # Simple key for XOR operation
    with open(filename, 'rb') as original_file:
        data = original_file.read()

    encrypted_data = bytearray(d ^ key for d in data)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Main function
if __name__ == "__main__":
    video_path = './tmp/complex_video.mp4'
    generate_complex_video(video_path)
    simple_encrypt_decrypt(video_path)
    print(f"Generated and 'encrypted' complex video saved as {video_path}")