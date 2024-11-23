import cv2
import numpy as np
import subprocess
import os

# Define the resolutions to create video versions for, adding a 3D feature example resolution
resolutions = [
    (640, 480),   # Standard Definition
    (1280, 720),  # HD
    (1920, 1080), # Full HD
    (640, 480)    # Example resolution for BIFS feature video
]

# Text to display in the video
text = "Scalability in MP4"
font = cv2.FONT_HERSHEY_SIMPLEX

# Directory to save generated MP4 files
output_dir = "./tmp/"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a video with a specific resolution
def generate_video(resolution, include_bifs=False, include_lossless_audio=False):
    width, height = resolution
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    video_file_name = f"video_{width}x{height}{'_BIFS' if include_bifs else ''}{'_Lossless' if include_lossless_audio else ''}.mp4"
    output_path = os.path.join(output_dir, video_file_name)
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    
    for i in range(100):  # Number of frames to generate
        # Create a black image
        img = np.zeros((height, width, 3), np.uint8)
        # Calculate text size, to position it in the center
        text_size = cv2.getTextSize(text, font, 1, 2)[0]
        text_x = (width - text_size[0]) // 2
        text_y = (height + text_size[1]) // 2
        # Put the text on the image
        cv2.putText(img, text, (text_x, text_y), font, 1, (255, 255, 255), 2)
        
        if include_bifs:
            # Simulating BIFS feature by adding a simple 3D-like effect on the text
            cv2.putText(img, text, (text_x - 2, text_y - 2), font, 1, (0, 255, 0), 2)
        
        # Write the frame into the file
        out.write(img)
    
    out.release()  # Release the VideoWriter object

    # Add lossless audio if requested
    if include_lossless_audio:
        temp_video_path = output_path
        # Corrected line: Use `video_file_name` instead of `video_file_id`
        output_path_with_audio = os.path.join(output_dir, f"{os.path.splitext(video_file_name)[0]}_with_audio.mp4")
        
        # Sample silent ALAC encoded audio file (replace with actual ALAC audio file path)
        alac_audio_file = 'path_to_silent_alac.m4a'  # This file should be ALAC encoded and silent or containing desired audio
        
        # Combine the video and audio using ffmpeg
        cmd = f'ffmpeg -i {temp_video_path} -i {alac_audio_file} -c:v copy -c:a copy {output_path_with_audio}'
        subprocess.call(cmd, shell=True)
        
        # Remove the original video file without audio
        os.remove(temp_video_path)
        # Update the output path to the new file with audio
        output_path = output_path_with_audio

# Generate videos with different resolutions and an extra video with the Lossless Audio feature
for resolution in resolutions:
    generate_video(resolution, include_bifs=(resolution == (640, 480)), include_lossless_audio=True)

print("Videos with Lossless Audio Support generated successfully.")