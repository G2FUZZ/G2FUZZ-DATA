import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an MP4 file with variable background colors, text overlays, and a circle
def generate_complex_video(filename):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480), True)

    # Create 120 frames with variable background colors and overlays
    for i in range(120):
        # Cycle through different background colors
        frame = np.zeros((480, 640, 3), np.uint8)
        color = ((i * 2) % 255, (i * 5) % 255, (i * 3) % 255)  # Generate a variable color
        frame[:] = color

        # Add a simple shape - circle that moves
        cv2.circle(frame, (320 + int(100 * np.cos(i * np.pi / 60)), 240 + int(100 * np.sin(i * np.pi / 60))), 50, (255, 255, 255), -1)

        # Include dynamic text overlay
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'Frame {i+1}', (10, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

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