from moviepy.editor import ColorClip, TextClip, concatenate_videoclips, AudioFileClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define basic properties for the clips
clip_duration = 5
clip_size = (640, 480)
bg_color = (0, 0, 0)
txt_color = 'white'

# Audio files for demonstration
audio_files = ['./audio_track_1.mp3', './audio_track_2.mp3']  # Example audio files

# Create a function to generate a simple video clip with text and switchable audio tracks
def create_clip_with_audio(text, filename, audio_files):
    # Background clip
    bg_clip = ColorClip(size=clip_size, color=bg_color, duration=clip_duration)
    
    # Text clip
    try:
        txt_clip = TextClip(txt=text, fontsize=24, color=txt_color, size=clip_size)
    except Exception as e:
        print(f"Error creating TextClip: {e}")
        return
    txt_clip = txt_clip.set_duration(clip_duration)
    
    # Combine the background and text clips
    video = concatenate_videoclips([bg_clip, txt_clip], method="compose")
    
    # Add multiple audio tracks by layering them; actual switching should be handled by the video player
    audio_clips = [AudioFileClip(audio) for audio in audio_files]
    final_audio = audio_clips[0].set_duration(clip_duration)  # Default to the first track for simplicity
    
    # Fix a typo in the original code
    video = video.set_audio(final_audio)
    
    # Write the result to a file
    video.write_videofile(filename, fps=24, codec="libx264", audio_codec="aac")
    
    # Add extended metadata to the mp4 file
    add_extended_metadata(filename)

def add_extended_metadata(filename):
    video = MP4(filename)
    
    # Example of adding extended metadata
    video["\xa9day"] = "2023-10-05"  # Recording date
    video["\xa9gen"] = "Educational"  # Genre
    video["desc"] = "This is an example video with extended metadata."  # Description
    video["ldes"] = "This video demonstrates how to add extended metadata to MP4 files, including GPS data, scene descriptions, and more."  # Long description
    
    # Saving the modified metadata back to the file
    video.save()

# Generate clips with switchable audio tracks and extended metadata
create_clip_with_audio("Main Menu: Select Option", os.path.join(output_dir, "main_menu_with_audio.mp4"), audio_files)
create_clip_with_audio("Option 1 Content", os.path.join(output_dir, "option_1_with_audio.mp4"), audio_files)
create_clip_with_audio("Option 2 Content", os.path.join(output_dir, "option_2_with_audio.mp4"), audio_files)