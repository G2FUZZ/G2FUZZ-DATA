import cv2
import numpy as np
from moviepy.editor import *
import os

def create_checkerboard(width=320, height=240, checker_size=10):
    """Creates a checkerboard pattern."""
    def checker(x, y): return (x//checker_size % 2) == (y//checker_size % 2)
    return np.fromfunction(np.vectorize(checker), (height, width), dtype=int)

def add_text_with_opencv(frame, text="Alpha Channel", position=(160, 120), font_scale=1, font_thickness=2, color=(255, 255, 255)):
    """Adds text to an OpenCV image."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = position[0] - text_size[0] // 2
    text_y = position[1] + text_size[1] // 2
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, font_thickness)

def generate_video_with_alpha_channel_and_vp6_scaling(output_path='./tmp/alpha_video_with_vp6.flv', loop_duration=10):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create a checkerboard pattern
    width, height = 320, 240
    checkerboard = create_checkerboard(width, height)
    alpha_background = np.zeros((height, width, 4), dtype=np.uint8)
    
    # Set checkerboard pattern to white and fully transparent
    alpha_background[checkerboard == 1] = [255, 255, 255, 0]  # Fully transparent white
    alpha_background[checkerboard == 0] = [0, 0, 0, 255]  # Opaque black

    # Convert alpha_background to an image that OpenCV can work with
    bgr_frame = cv2.cvtColor(alpha_background, cv2.COLOR_RGBA2BGRA)

    # Add text with OpenCV
    add_text_with_opencv(bgr_frame, "Alpha Channel VP6", position=(width // 2, int(height * 0.4)))

    # Create a single frame clip
    single_frame_clip = ImageClip(bgr_frame, duration=5)

    # Loop the single frame clip to achieve the desired looping duration
    looped_clip = concatenate_videoclips([single_frame_clip] * (loop_duration // single_frame_clip.duration))

    # Set fps for the looped clip
    final_clip = looped_clip.set_fps(24)

    # Export the video with On2 VP6 codec, which is known for its efficiency in scaling
    # Note: moviepy does not directly support exporting using the VP6 codec via the write_videofile method.
    # This operation typically requires direct use of ffmpeg with appropriate parameters.
    # As a fallback, we'll adjust parameters to mimic lower bitrate output for demonstration purposes.
    final_clip.write_videofile(output_path, codec='libx264', ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p', '-vf', 'scale=640:480'])

generate_video_with_alpha_channel_and_vp6_scaling()