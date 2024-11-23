import cv2
import numpy as np
from mutagen.mp4 import MP4, MP4Cover

# Create a directory to store the generated mp4 files
import os
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create two blank images to simulate different angles
height, width = 720, 1280

# First angle - White background
blank_image1 = np.zeros((height, width, 3), np.uint8)
blank_image1[:] = (255, 255, 255)

# Second angle - Black background
blank_image2 = np.zeros((height, width, 3), np.uint8)
blank_image2[:] = (0, 0, 0)

# Define the path of the mp4 file
mp4_file_path = os.path.join(output_dir, "sample_with_metadata_and_angles.mp4")

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec
video_writer = cv2.VideoWriter(mp4_file_path, fourcc, 1.0, (width, height))

# Write 10 frames for each angle to the video
# Here, we simulate "angle switching" by alternating between two images
for i in range(10):
    if i % 2 == 0:
        video_writer.write(blank_image1)  # Angle 1
    else:
        video_writer.write(blank_image2)  # Angle 2

# Release the video writer
video_writer.release()

# Add metadata to the mp4 file using mutagen
video = MP4(mp4_file_path)
video['\xa9nam'] = "Sample Video Title with Multiple Angles"  # Title
video['\xa9ART'] = "Artist Name"  # Artist
video['\xa9alb'] = "Album Title"  # Album
video['\xa9day'] = "2023"  # Year

# To add album art, first, we need an image
# Here, we reuse the blank_image1 to create a simple album art
album_art_path = os.path.join(output_dir, 'album_art.jpg')
cv2.imwrite(album_art_path, blank_image1)
with open(album_art_path, 'rb') as img_file:
    video['covr'] = [MP4Cover(img_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]

# Save the modified metadata
video.save()