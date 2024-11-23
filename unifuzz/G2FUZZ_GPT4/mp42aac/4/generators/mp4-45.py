import cv2
import numpy as np
import os

# Define the resolutions to create video versions for
resolutions = [
    (640, 480),  # Standard Definition
    (1280, 720), # HD
    (1920, 1080), # Full HD
]

# Directory to save generated MP4 files
output_dir = "./tmp/"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Font for text display
font = cv2.FONT_HERSHEY_SIMPLEX

# Function to generate a scene with text
def scene_text(img, text, color=(255, 255, 255)):
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = (img.shape[0] + text_size[1]) // 2
    cv2.putText(img, text, (text_x, text_y), font, 1, color, 2)

# Function to generate a scene with a color transition
def scene_color_transition(width, height, start_color, end_color, frames=30):
    for i in range(frames):
        t = i / frames
        color = tuple((start_color[j] * (1 - t) + end_color[j] * t) for j in range(3))
        img = np.full((height, width, 3), color, np.uint8)
        yield img

# Function to generate a scene with moving geometric shapes
def scene_geometric_shapes(width, height, frames=50):
    for i in range(frames):
        img = np.zeros((height, width, 3), np.uint8)
        # Moving circle
        cv2.circle(img, (int((np.sin(i * 0.1) + 1) / 2 * width), int(height / 2)), 50, (0, 255, 0), -1)
        # Moving rectangle
        cv2.rectangle(img, (int((np.cos(i * 0.1) + 1) / 2 * width) - 50, height - 150), 
                      (int((np.cos(i * 0.1) + 1) / 2 * width) + 50, height - 100), (255, 0, 0), -1)
        yield img

# Function to generate video with scenes
def generate_video_with_scenes(resolution, video_path):
    width, height = resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (width, height))
    
    # Scene 1: Text display
    img = np.zeros((height, width, 3), np.uint8)
    scene_text(img, "Welcome to the Video", (0, 255, 255))
    for _ in range(50):  # Display for 50 frames
        out.write(img)
    
    # Scene 2: Color transition
    for img in scene_color_transition(width, height, (0, 255, 255), (255, 0, 255)):
        out.write(img)
    
    # Scene 3: Geometric shapes
    for img in scene_geometric_shapes(width, height):
        out.write(img)
    
    out.release()

# Generate videos with different resolutions
for resolution in resolutions:
    video_path = f"{output_dir}video_{resolution[0]}x{resolution[1]}.mp4"
    generate_video_with_scenes(resolution, video_path)

print("Videos with complex scenes generated successfully.")