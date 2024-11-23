import cv2
import numpy as np
import os
import subprocess  # For executing the command to enable Fast Start

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

    # Optimize video file for Fast Start if not fragmented
    if not fragmented:
        optimize_for_fast_start(filename)

# Optimize video file for Fast Start
def optimize_for_fast_start(filename):
    temp_filename = filename + ".temp"
    # Use ffmpeg to move the 'moov atom' to the beginning of the file
    result = subprocess.call(["ffmpeg", "-i", filename, "-movflags", "+faststart", "-codec", "copy", temp_filename])
    # Check if ffmpeg command was successful
    if result == 0:
        # Check if the temporary file was created
        if os.path.exists(temp_filename):
            # Replace the original file with the optimized one
            os.replace(temp_filename, filename)
        else:
            print(f"Error: Temporary file {temp_filename} was not created.")
    else:
        print("Error: ffmpeg command failed.")

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
    generate_video(video_path, fragmented=False)  # Adjusted to control Fast Start optimization
    simple_encrypt_decrypt(video_path)
    print(f"Generated and 'encrypted' video saved as {video_path}")