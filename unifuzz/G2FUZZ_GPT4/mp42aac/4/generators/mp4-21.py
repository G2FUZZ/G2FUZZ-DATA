import cv2
import numpy as np

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

# Function to generate a video with a specific resolution
def generate_video(resolution, include_bifs=False):
    width, height = resolution
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    output_path = f"{output_dir}video_{width}x{height}{'_BIFS' if include_bifs else ''}.mp4"
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

# Generate videos with different resolutions and an extra video with the BIFS feature
for resolution in resolutions:
    generate_video(resolution, include_bifs=(resolution == (640, 480)))

print("Videos generated successfully.")