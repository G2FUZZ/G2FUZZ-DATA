import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a video with specified resolution
def create_video_with_resolution(width, height, output_path):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the video
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    
    # Create a sample animation inside the video
    for i in range(100):  # Number of frames
        # Create an image with 3 channels (RGB) and the specified resolution
        img = np.zeros((height, width, 3), np.uint8)
        
        # Add moving circle to the frames
        cv2.circle(img, (width//2 + i*3 % width, height//2), 50, (255, 105, 180), -1)
        
        # Write the frame into the file
        out.write(img)
    
    out.release()  # Release the file

# Example resolutions
resolutions = [
    (640, 480),  # Standard Definition
    (1280, 720),  # HD
    (1920, 1080),  # Full HD
    (3840, 2160),  # 4K
]

# Create a video for each resolution
for width, height in resolutions:
    output_path = os.path.join(output_dir, f'video_{width}x{height}.mp4')
    create_video_with_resolution(width, height, output_path)

print("Videos have been created.")