import cv2
import numpy as np
import os

def generate_frame(i, width, height, total_frames):
    """
    Generate a frame with variable content based on the current frame index.
    """
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate progress
    progress = i / total_frames
    
    # Draw different shapes based on progress
    if progress < 0.25:
        # Draw a rectangle
        cv2.rectangle(frame, (50, 100), (width-50, height-100), (255, 0, 0), -1)
    elif progress < 0.5:
        # Draw a circle
        cv2.circle(frame, (width//2, height//2), 100, (0, 255, 0), -1)
    elif progress < 0.75:
        # Draw an ellipse
        cv2.ellipse(frame, (width//2, height//2), (100, 150), 0, 0, 180, (0, 0, 255), -1)
    else:
        # Draw polygons
        pts = np.array([[100, 50], [200, 300], [700, 200], [500, 100]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255), 3)
    
    # Add varying text
    cv2.putText(frame, f'Frame {i+1}', (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Apply a fade-in effect based on progress for visual interest
    fade_value = int(255 * (i / total_frames))
    frame = cv2.addWeighted(frame, fade_value/255, frame, 0, 0)
    
    return frame

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video properties
width, height = 640, 480
fps = 24
duration = 10  # seconds, longer duration for more content
video_file_path = os.path.join(output_dir, 'output_complex_features.mp4')

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Using 'mp4v' for wider compatibility
out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height), isColor=True)

total_frames = fps * duration

# Generate frames with variable content
for i in range(total_frames):
    frame = generate_frame(i, width, height, total_frames)
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f'Video saved to {video_file_path}')

# Note: This code generates an MP4 file with variable content in each frame, 
# including shapes, text, and a fade-in effect. For even more complex features,
# consider integrating with external tools like ffmpeg for post-processing effects
# and file manipulations.