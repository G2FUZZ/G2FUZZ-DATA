import os
from moviepy.editor import *
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave audio clip
def generate_sine_wave(frequency, duration_ms):
    sine_wave = Sine(frequency).to_audio_segment(duration=duration_ms)
    return sine_wave

# Generate two sine waves of different frequencies
sine_wave1 = generate_sine_wave(440, 5000)  # 440 Hz for 5 seconds
sine_wave2 = generate_sine_wave(540, 5000)  # 540 Hz for 5 seconds

# Mix the sine waves together
mixed_sine_waves = sine_wave1.overlay(sine_wave2)

# Save the mixed sine waves as an MP3 file temporarily
temp_mixed_sine_path = os.path.join(output_dir, "temp_mixed_sine.mp3")
mixed_sine_waves.export(temp_mixed_sine_path, format="mp3")

# Define the correct paths to your image files
correct_path_to_image1 = "correct_path_to_image1.jpg"
correct_path_to_image2 = "correct_path_to_image2.jpg"

# Function to safely create an ImageClip if the file exists
def safe_image_clip(path, duration):
    if os.path.exists(path):
        return ImageClip(path).set_duration(duration)
    else:
        print(f"Error: The file {path} does not exist.")
        return None

# Create a sequence of images to generate a video clip
image_clip1 = safe_image_clip(correct_path_to_image1, 5)
image_clip2 = safe_image_clip(correct_path_to_image2, 5)

if image_clip1 is None or image_clip2 is None:
    print("One or more image clips could not be created due to missing files.")
else:
    # Concatenate the image clips to form a video
    video_clip = concatenate_videoclips([image_clip1, image_clip2])

    # Create an audio clip using moviepy from the mixed sine waves MP3
    audio_clip = AudioFileClip(temp_mixed_sine_path)

    # Set the audio of the video clip
    final_video = video_clip.set_audio(audio_clip)

    # Export the final video as an FLV file
    final_flv_path = os.path.join(output_dir, "output_video.flv")
    final_video.write_videofile(final_flv_path, codec="libx264", audio_codec="aac")

    # Clean up temporary files
    os.remove(temp_mixed_sine_path)

    print(f"Generated FLV file with complex audio-visual structure at: {final_flv_path}")