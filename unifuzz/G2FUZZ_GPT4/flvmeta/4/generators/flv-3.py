import os
from moviepy.editor import concatenate_audioclips, AudioFileClip
from moviepy.audio.fx.all import volumex
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave audio clip (440 Hz) for 10 seconds
sine_wave = Sine(440).to_audio_segment(duration=10000)

# Save the sine wave as an MP3 file temporarily
temp_mp3_path = os.path.join(output_dir, "temp_sine_wave.mp3")
sine_wave.export(temp_mp3_path, format="mp3")

# Create an audio clip using moviepy from the generated MP3
audio_clip = AudioFileClip(temp_mp3_path)

# Apply audio compression using moviepy (example: volume change)
compressed_audio_clip = volumex(audio_clip, 0.5)

# Concatenate the audio clip with itself to demonstrate handling multiple clips
final_audio_clip = concatenate_audioclips([compressed_audio_clip, compressed_audio_clip])

# Export the final audio. Adjusting the path and method for audio export
final_audio_path = os.path.join(output_dir, "output_audio_compressed.mp3")
final_audio_clip.write_audiofile(final_audio_path, codec="libmp3lame")

# Clean up temporary MP3 file
os.remove(temp_mp3_path)

print(f"Generated MP3 file with compressed audio at: {final_audio_path}")