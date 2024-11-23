import cv2
import numpy as np
import os

def generate_frame(width, height, t, duration):
    """Generates complex frames with moving shapes and text."""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Moving shapes
    size = int(50 + 10 * np.sin(t))
    x = int((width - size) * (t / duration))
    y = int((height - size) / 2 + 50 * np.cos(t))
    frame[y:y+size, x:x+size] = (255, 0, 0)  # Red square

    # Text overlay
    cv2.putText(frame, f"Time: {t:.2f}s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Transition effects (e.g., fade-in for the first second)
    if t < 1:
        alpha = t  # Gradually increase opacity
        frame = cv2.addWeighted(frame, alpha, frame, 0, 0)

    return frame

def create_video(output_filename, width, height, duration, fps):
    """Creates a video file with complex structures."""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
    
    total_frames = int(fps * duration)
    for i in range(total_frames):
        t = i / fps
        frame = generate_frame(width, height, t, duration)
        video.write(frame)
    
    video.release()

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the video
width, height = 640, 480
fps = 30  # Fixed FPS for simplicity
duration = 10  # seconds
output_filename = os.path.join(output_dir, "complex_structure_video.mp4")

# Create the video
create_video(output_filename, width, height, duration, fps)

print(f"Video saved to {output_filename}")