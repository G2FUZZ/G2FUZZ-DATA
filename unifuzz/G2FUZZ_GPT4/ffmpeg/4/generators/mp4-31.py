import cv2
import numpy as np
import os

def add_text_to_frame(frame, text, position=(30, 30), font_scale=1, color=(255, 255, 255)):
    """
    Adds text to an individual frame
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, position, font, font_scale, color, 2, cv2.LINE_AA)

def add_image_overlay(frame, image_path, position=(0, 0), scale=1.0):
    """
    Adds an image overlay to an individual frame
    """
    # Load the image to overlay
    overlay_img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    overlay_img = cv2.resize(overlay_img, (0, 0), fx=scale, fy=scale)
    
    # Overlay image dimensions
    oh, ow = overlay_img.shape[:2]
    
    # Positioning overlay image
    sx, sy = position
    ex, ey = sx + ow, sy + oh
    
    # Split out the alpha mask from the colour info
    overlay_img_bgr = overlay_img[..., :3]  # Grab the BRG planes
    overlay_mask = overlay_img[..., 3:]  # And the alpha plane
    
    # Turn the mask into a binary mask
    overlay_mask = cv2.merge([overlay_mask] * 3)
    
    # Calculate the inverse mask
    background_mask = 255 - overlay_mask
    
    # Turn the masks into three channel, so we can use them as weights
    overlay_part = (frame[sy:ey, sx:ex] * (background_mask * 0.01)).astype(np.uint8)
    overlay_img_part = (overlay_img_bgr * (overlay_mask * 0.01)).astype(np.uint8)
    
    # Combine the two
    frame[sy:ey, sx:ex] = cv2.add(overlay_part, overlay_img_part)

# Ensure the tmp directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize video settings
frame_width = 640
frame_height = 480
fps = 24
output_filename = output_directory + 'complex_features_video.mp4'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Generate a basic video with 120 frames (5 seconds at 24 FPS)
for i in range(120):
    # Create a frame with random colors
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    
    if i < 30:  # First second: Fade-in effect
        alpha = i / 30.0
        frame = (frame * alpha).astype(np.uint8)
    elif i > 90:  # Last second: Fade-out effect
        alpha = (120 - i) / 30.0
        frame = (frame * alpha).astype(np.uint8)
    
    # Sinusoidal motion for the circle
    x = int((frame_width / 2) + (100 * np.sin(i * np.pi / 15)))
    y = int((frame_height / 2) + (100 * np.cos(i * np.pi / 15)))
    cv2.circle(frame, (x, y), 50, (255, 105, 180), -1)  # Drawing a circle
    
    # Adding text overlay
    add_text_to_frame(frame, "Demo Video", position=(50, 50), font_scale=1.5)
    
    # Adding image overlay (Make sure to replace 'path_to_image.png' with an actual image path)
    # add_image_overlay(frame, 'path_to_image.png', position=(frame_width - 150, 10), scale=0.5)
    
    out.write(frame)

# Release everything when the job is finished
out.release()
cv2.destroyAllWindows()

print(f"Video created: {output_filename}")