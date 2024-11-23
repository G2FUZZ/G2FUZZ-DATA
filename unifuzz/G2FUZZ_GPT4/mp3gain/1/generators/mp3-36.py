import os
import subprocess
import time
from pydub import AudioSegment
from pydub.generators import Sine
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB, USLT, COMM

# Ensure the tmp directory exists
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Define file paths
background_mp3_path = os.path.join(tmp_dir, "background.mp3")
temp_wav_path = os.path.join(tmp_dir, "temp_combined.wav")
final_mp3_path = os.path.join(tmp_dir, "complex_mp3_with_features.mp3")
cover_image_path = os.path.join(tmp_dir, "cover.png")

# Generate or check for background.mp3
if not os.path.exists(background_mp3_path):
    tone = Sine(440).to_audio_segment(duration=10000)  # A 440 Hz tone for 10 seconds
    tone.export(background_mp3_path, format="mp3")
    print("Generated placeholder background.mp3")

# Load and process the background music
background_music = AudioSegment.from_file(background_mp3_path)
background_music = background_music - 20  # Reduce volume by 20 dB
silence = AudioSegment.silent(duration=5000).fade_in(3000)
combined = silence.overlay(background_music, position=0)
combined.export(temp_wav_path, format="wav")

# FFmpeg command to convert WAV to MP3
ffmpeg_command = [
    "ffmpeg", "-i", temp_wav_path, "-codec:a", "libmp3lame",
    "-q:a", "2", "-ar", "44100", "-ac", "6", final_mp3_path
]

# Execute FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print("FFmpeg processing completed.")
except subprocess.CalledProcessError as e:
    print(f"FFmpeg error: {e}")
    exit()

# Wait a bit for the filesystem to catch up
time.sleep(1)

# Load the MP3 file with Mutagen
try:
    audio = MP3(final_mp3_path, ID3=ID3)
except Exception as e:
    print(f"Error loading MP3 file with Mutagen: {e}")
    exit()

# Add metadata and save
try:
    if os.path.exists(cover_image_path):
        with open(cover_image_path, 'rb') as img_file:
            audio.tags.add(APIC(encoding=3, mime='image/png', type=3, desc='Cover', data=img_file.read()))
    audio.tags.add(TIT2(encoding=3, text='Title of the Track'))
    audio.tags.add(TPE1(encoding=3, text='Artist Name'))
    audio.tags.add(TALB(encoding=3, text='Album Name'))
    audio.tags.add(TRCK(encoding=3, text='1'))
    audio.tags.add(USLT(encoding=3, text='Lyrics of the track go here'))
    audio.tags.add(COMM(encoding=3, lang='eng', desc='Comment', text='This is a custom comment'))
    audio.save()
except Exception as e:
    print(f"Error adding metadata: {e}")

# Cleanup
os.remove(temp_wav_path)
print("Complex MP3 file with advanced features generated.")