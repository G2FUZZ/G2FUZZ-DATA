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

def generate_video_with_additional_features(output_path='./tmp/extended_alpha_video_with_vp6.flv', frame_rate=24):
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
    add_text_with_opencv(bgr_frame, "Alpha Channel & Frame Rate Flex", position=(width // 2, int(height * 0.4)))

    # Convert back to a format suitable for moviepy
    final_clip = ImageClip(bgr_frame, duration=5).set_fps(frame_rate)

    # Export the video with flexible frame rate
    # Note: For actual VP6 encoding and advanced frame rate flexibility, direct use of ffmpeg with appropriate parameters is recommended.
    # Here, we use 'libx264' as a placeholder with ffmpeg_params to simulate the output for demonstration purposes.
    final_clip.write_videofile(output_path, codec='libx264', ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p', '-vf', f'scale=640:480,fps={frame_rate}'])

# Example usage: Generate video with a frame rate of 30 for higher quality production
generate_video_with_additional_features(frame_rate=30)