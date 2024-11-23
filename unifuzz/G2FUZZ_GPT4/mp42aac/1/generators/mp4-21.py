import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

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

# Add "Edit Lists" feature to mp4 file
def add_edit_lists(original_file):
    edit_video_path = './tmp/edited_video.mp4'
    
    # Decrypt the file before processing
    simple_encrypt_decrypt(original_file)  # Decrypt the file to its original state
    
    # Load original video
    clip = VideoFileClip(original_file)
    
    # Example edit list: Repeat the first 2 seconds twice, then play the rest of the video
    first_part = clip.subclip(0, 2).loop(2)
    second_part = clip.subclip(2)
    
    # Concatenate clips according to the edit list
    final_clip = concatenate_videoclips([first_part, second_part])
    
    # Write the result
    final_clip.write_videofile(edit_video_path, codec='libx264')
    
    # Optionally, re-encrypt the edited file if needed
    simple_encrypt_decrypt(edit_video_path)
    
    return edit_video_path

# Main function
if __name__ == "__main__":
    video_path = './tmp/sample_video.mp4'
    generate_video(video_path, fragmented=True)  # Note: 'fragmented' flag has no effect now
    simple_encrypt_decrypt(video_path)  # Encrypt the original video
    edited_video_path = add_edit_lists(video_path)  # Process includes decryption and optional re-encryption
    print(f"Generated and 'encrypted' video saved as {edited_video_path}")