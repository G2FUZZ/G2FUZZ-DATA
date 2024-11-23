import cv2
import numpy as np
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an MP4 file
def generate_video(filename, fragmented=False):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))
    
    # Create 60 frames of red color
    for _ in range(60):
        frame = np.zeros((480, 640, 3), np.uint8)
        frame[:] = (0, 0, 255)  # BGR format, red frame
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
    video_path = './tmp/sample_video.mp4'
    generate_video(video_path, fragmented=True)  # Note: 'fragmented' flag has no effect now
    simple_encrypt_decrypt(video_path)
    print(f"Generated and 'encrypted' video saved as {video_path}")