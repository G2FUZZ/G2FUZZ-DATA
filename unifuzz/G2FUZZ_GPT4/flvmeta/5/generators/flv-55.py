from moviepy.editor import *
import os
import cv2
import numpy as np

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

def generate_complex_video(output_path='./tmp/complex_alpha_video.flv', mute=False, volume=0.8):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Settings
    width, height = 320, 240

    # Create a list of checkerboard patterns
    checkerboards = [create_checkerboard(width, height, checker_size=i*5) for i in range(1, 4)]

    # Create a list of clips
    clips = []
    for idx, checkerboard in enumerate(checkerboards):
        alpha_background = np.zeros((height, width, 4), dtype=np.uint8)
        alpha_background[checkerboard == 1] = [255, 255, 255, 0]  # Fully transparent white
        alpha_background[checkerboard == 0] = [0, 0, 0, 255]  # Opaque black

        # Convert alpha_background to an image that OpenCV can work with
        bgr_frame = cv2.cvtColor(alpha_background, cv2.COLOR_RGBA2BGRA)

        # Add text with OpenCV
        text = f"Pattern {idx + 1}"
        add_text_with_opencv(bgr_frame, text, position=(width // 2, int(height * 0.8)))

        # Convert back to a format suitable for moviepy
        clip = ImageClip(bgr_frame, duration=3).set_fps(24)
        clips.append(clip)

    # Create transition between clips
    final_clip = concatenate_videoclips(clips, method="compose")

    # Generate a custom audio clip from a file or programmatically
    # Here, we'll generate a silent audio for simplicity
    silent_audio = AudioClip(lambda t: [0]*2, duration=final_clip.duration)  # 2 channels

    # Adjust the volume if not muted
    if not mute:
        silent_audio = silent_audio.volumex(volume)

    # Set the audio to the final clip
    final_clip = final_clip.set_audio(silent_audio)

    # Export the video
    final_clip.write_videofile(output_path, codec='libx264', ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p', '-vf', 'scale=640:480'])

generate_complex_video(mute=True, volume=0.5)  # Example usage