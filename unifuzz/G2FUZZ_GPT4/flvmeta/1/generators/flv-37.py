import os
from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips, TextClip, concatenate_audioclips
import numpy as np
from scipy.io import wavfile
from moviepy.video.fx import fadein, fadeout

# Set the path to the ImageMagick binary directly in the script
# For Windows, it might look like this (adjust the path as necessary):
# os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"
# For macOS or Linux, if 'convert' command is available directly, this might not be needed.
# If you need to specify it, it might look like this:
# os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/convert"

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration=1, sample_rate=44100):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 32767).astype(np.int16)

# Function to create a temporary audio file given frequency and duration
def create_temp_audio_file(frequency, duration, filename):
    audio_data = generate_tone(frequency, duration)
    wavfile.write(filename, 44100, audio_data)
    return AudioFileClip(filename)

# Function to create a video clip with background, text overlay, and audio
def create_video_clip(text, background_color, frequency, duration, fps=24):
    # Create a temporary audio file
    temp_audio_filename = os.path.join(output_dir, f'temp_audio_{frequency}.wav')
    audio_clip = create_temp_audio_file(frequency, duration, temp_audio_filename)
    
    # Create a background image
    background_image = np.ones((360, 640, 3), dtype=np.uint8) * np.array(background_color)[None, None, :]
    
    # Create an image clip with the text overlay
    image_clip = ImageClip(background_image, duration=duration).set_fps(fps)
    text_clip = TextClip(text, fontsize=70, color='white', size=image_clip.size).set_duration(duration).set_position("center")
    
    # Combine the text and the background video clips
    video_clip = CompositeVideoClip([image_clip, text_clip], size=(640,360)).set_audio(audio_clip)
    
    # Apply fadein and fadeout effects
    video_clip = fadein(video_clip, 1).fx(fadeout, 1)
    
    # Clean up the temporary WAV file
    os.remove(temp_audio_filename)
    
    return video_clip

# The rest of your script remains unchanged...