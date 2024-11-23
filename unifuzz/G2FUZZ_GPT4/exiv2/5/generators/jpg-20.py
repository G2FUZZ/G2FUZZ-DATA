from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import numpy as np

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

def create_image_with_text(filename, text, iterations):
    # Create an image with white background
    img = Image.new('RGB', (400, 200), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Try to use a default font
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()
    
    # Add text to the image
    d.text((10,50), text, fill=(0,0,0), font=font)

    # Save the image initially
    img.save(filename, 'JPEG', quality=95)

    # Open, re-save the image to simulate quality loss from re-compression
    for _ in range(iterations):
        img = Image.open(filename)
        img.save(filename, 'JPEG', quality=95)  # Reduce quality to simulate loss over re-edits

def create_motion_jpeg(video_filename, image_filename, frame_count):
    # Load the image
    img = cv2.imread(image_filename)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(video_filename, fourcc, 10.0, (400, 200))

    # Convert PIL image to OpenCV format
    img_array = np.array(img)
    for _ in range(frame_count):
        out.write(img_array)  # Writing the same image as each frame

    # Release everything when done
    out.release()

# Text to add to the image
text = "Repeated Editing Leads to Quality Loss"

# File path for the image
filename = './tmp/loss_of_quality.jpg'

# Number of times the image is re-saved to simulate loss of quality
iterations = 10

create_image_with_text(filename, text, iterations)

# File path for the video
video_filename = './tmp/loss_of_quality_mjpeg.avi'

# Number of frames for the motion JPEG video
frame_count = 30

create_motion_jpeg(video_filename, filename, frame_count)