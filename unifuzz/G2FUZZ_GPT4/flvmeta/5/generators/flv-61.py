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

def create_segment(checker_size, text, duration=5, width=320, height=240):
    """Creates a video segment with specified checkerboard and text."""
    checkerboard = create_checkerboard(width, height, checker_size)
    alpha_background = np.zeros((height, width, 4), dtype=np.uint8)
    
    alpha_background[checkerboard == 1] = [255, 255, 255, 0]  # Fully transparent white
    alpha_background[checkerboard == 0] = [0, 0, 0, 255]  # Opaque black

    bgr_frame = cv2.cvtColor(alpha_background, cv2.COLOR_RGBA2BGRA)
    add_text_with_opencv(bgr_frame, text, position=(width // 2, int(height * 0.4)))

    return ImageClip(bgr_frame, duration=duration)

def generate_complex_video_with_audio(output_path='./tmp/complex_alpha_video.flv', loop_duration=10, audio_path='audio.mp3'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create different video segments
    segment1 = create_segment(10, "First Segment", duration=5)
    segment2 = create_segment(20, "Second Segment", duration=5)
    segment3 = create_segment(30, "Third Segment", duration=5)
    
    # Apply fade transitions between segments
    transition_duration = 1
    clip1 = CompositeVideoClip([segment1])
    clip2 = CompositeVideoClip([segment2]).set_start(transition_duration).crossfadein(transition_duration)
    clip3 = CompositeVideoClip([segment3]).set_start(2*transition_duration).crossfadein(transition_duration)
    
    # Concatenate clips with transitions
    final_clip = concatenate_videoclips([clip1, clip2, clip3], method="compose")

    # Set fps for the final clip
    final_clip = final_clip.set_fps(24)

    # Add an audio track to the final video
    if audio_path and os.path.exists(audio_path):
        final_clip = final_clip.set_audio(AudioFileClip(audio_path))

    # Export the video
    final_clip.write_videofile(output_path, codec='libx264', ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p'])

# Example call to the function
generate_complex_video_with_audio()