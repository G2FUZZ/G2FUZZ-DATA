import cv2
import numpy as np

# Define the resolutions to create video versions for
resolutions = [
    (640, 480),  # Standard Definition
    (1280, 720), # HD
    (1920, 1080) # Full HD
]

# Text to display in the video
text = "Scalability in MP4"
font = cv2.FONT_HERSHEY_SIMPLEX

# Directory to save generated MP4 files
output_dir = "./tmp/"

# Function to generate a video with a specific resolution
def generate_video(resolution):
    width, height = resolution
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # MP4 codec
    output_path = f"{output_dir}video_{width}x{height}.mp4"
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
        # Write the frame into the file
        out.write(img)
    
    out.release()  # Release the VideoWriter object

# Generate videos with different resolutions
for resolution in resolutions:
    generate_video(resolution)

print("Videos generated successfully.")