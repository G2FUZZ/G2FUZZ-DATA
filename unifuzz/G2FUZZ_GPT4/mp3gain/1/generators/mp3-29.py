from pydub import AudioSegment
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an audio segment of silence
silence = AudioSegment.silent(duration=1000)  # 1 second of silence

# Speed adjustment
speed_adjusted_silence = silence.speedup(playback_speed=1.5) # Increase speed by 50%

# Export the audio segment as an MP3 file
speed_adjusted_silence.export("./tmp/speed_adjusted_silent_mp3.mp3", format="mp3")

print("MP3 file with Speed Adjustment generated without DRM.")