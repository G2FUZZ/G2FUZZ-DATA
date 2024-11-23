import os
import subprocess
from gtts import gTTS
from moviepy.editor import ColorClip, AudioFileClip

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be converted to speech
text = "9. Popularity and Compatibility: Although the use of FLV has declined with the rise of HTML5 video and the discontinuation of Flash Player support, it remains a significant format for older web content and archives. Many video playback applications and multimedia converters still support FLV files."

# Convert text to speech
tts = gTTS(text=text, lang='en')
audio_path = './tmp/audio.mp3'
tts.save(audio_path)

# Load the audio file
audio_clip = AudioFileClip(audio_path)

# Create a video clip (black screen) of the same duration as the audio
video_clip = ColorClip(size=(640, 480), color=(0,0,0), duration=audio_clip.duration).set_audio(audio_clip)

# Export the video clip as an FLV file
flv_path = './tmp/video.flv'
video_clip.write_videofile(flv_path, codec='libx264', fps=24)

# Cleanup: Remove the temporary MP3 file
os.remove(audio_path)

print(f"FLV file has been saved to: {flv_path}")