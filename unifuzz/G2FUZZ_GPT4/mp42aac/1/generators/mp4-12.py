import cv2
import numpy as np
import os
import subprocess

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an MP4 file with video frames
def generate_video(filename):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))
    
    # Create 60 frames of red color
    for _ in range(60):
        frame = np.zeros((480, 640, 3), np.uint8)
        frame[:] = (0, 0, 255)  # BGR format, red frame
        out.write(frame)
    
    out.release()

# Generate a WAV file with lossless audio
def generate_lossless_audio(audio_filename, duration=3):
    # Generate a silent lossless audio file using ffmpeg
    # We use ALAC codec for Apple Lossless Audio
    cmd = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', str(duration),
           '-acodec', 'alac', audio_filename]
    subprocess.run(cmd)

# Combine video and audio
def combine_video_audio(video_filename, audio_filename, output_filename):
    cmd = ['ffmpeg', '-y', '-i', video_filename, '-i', audio_filename, '-c:v', 'copy', '-c:a', 'copy', output_filename]
    subprocess.run(cmd)

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
    audio_path = './tmp/sample_audio.m4a'  # M4A for ALAC format
    output_video_path = './tmp/final_video.mp4'
    
    generate_video(video_path)
    generate_lossless_audio(audio_path)
    combine_video_audio(video_path, audio_path, output_video_path)
    simple_encrypt_decrypt(output_video_path)
    
    print(f"Generated and 'encrypted' video with lossless audio saved as {output_video_path}")