import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, CompositeAudioClip

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_complex_video(filename):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    # Generate frames with different colors
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    for color in colors:
        for _ in range(20):  # 20 frames per color
            frame = np.zeros((480, 640, 3), np.uint8)
            frame[:] = color  # BGR format
            video_writer.write(frame)

    video_writer.release()
    
    # Initialize video_clip for further processing
    video_clip = VideoFileClip(filename)
    audio_file_path = "./tmp/sample_audio.mp3"
    
    # Check if the audio file exists
    if os.path.exists(audio_file_path):
        # Add an audio track to the video
        audio_clip = AudioFileClip(audio_file_path)
        final_audio = CompositeAudioClip([video_clip.audio, audio_clip])
        video_clip.audio = final_audio
        output_video_path = "./tmp/video_with_audio.mp4"
        video_clip.write_videofile(output_video_path)
    else:
        print(f"Audio file {audio_file_path} not found. Proceeding without adding audio.")
        output_video_path = filename  # Use the original video if no audio is added

    # Since we're avoiding ImageMagick and TextClip, we'll consider this the final step
    # If you need to add subtitles, consider using another tool or manually editing the video afterwards

def simple_encrypt_decrypt(filename):
    key = 123  # Simple key for XOR operation
    with open(filename, 'rb') as original_file:
        data = original_file.read()

    encrypted_data = bytearray(d ^ key for d in data)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Main function
if __name__ == "__main__":
    video_path = './tmp/complex_sample_video.mp4'
    generate_complex_video(video_path)
    simple_encrypt_decrypt(video_path)  # Encrypt the original complex video
    print(f"Generated and 'encrypted' complex video is ready at {video_path}")