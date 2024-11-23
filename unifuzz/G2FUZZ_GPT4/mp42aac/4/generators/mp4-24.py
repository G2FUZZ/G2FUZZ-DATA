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

# Directory to save generated MP4 files and subtitles
output_dir = "./tmp/"

# Function to generate a video with a specific resolution and an optional Timed Text feature
def generate_video(resolution, include_bifs=False, include_timed_text=False):
    width, height = resolution
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    output_path = f"{output_dir}video_{width}x{height}{'_BIFS' if include_bifs else ''}{'_TimedText' if include_timed_text else ''}.mp4"
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    
    # Prepare Timed Text (subtitles)
    if include_timed_text:
        subtitle_path = f"{output_dir}video_{width}x{height}{'_BIFS' if include_bifs else ''}{'_TimedText' if include_timed_text else ''}.srt"
        subtitles = open(subtitle_path, "w")
    
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
        
        # Add Timed Text for the current frame if enabled
        if include_timed_text:
            # Each subtitle shows for a second, calculate the current time range
            start_seconds = i // 20
            end_seconds = (i + 19) // 20
            subtitles.write(f"{i+1}\n")
            subtitles.write(f"00:00:{start_seconds:02d},000 --> 00:00:{end_seconds:02d},000\n")
            subtitles.write(f"{text}\n\n")
    
    out.release()  # Release the VideoWriter object
    
    if include_timed_text:
        subtitles.close()  # Close the subtitles file

# Generate videos with different resolutions and an extra video with the BIFS and Timed Text features
for resolution in resolutions:
    generate_video(resolution, include_bifs=(resolution == (640, 480)), include_timed_text=True)

print("Videos and Timed Texts generated successfully.")