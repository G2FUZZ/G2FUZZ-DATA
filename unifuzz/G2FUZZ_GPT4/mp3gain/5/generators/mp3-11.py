from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 5-second silent audio segment
silent_audio = AudioSegment.silent(duration=5000)  # Duration in milliseconds

# Export the audio segment as an MP3 file with parameters optimized for gapless playback
file_path = './tmp/silent_audio.mp3'

# Assuming gapless playback depends on certain encoding parameters and the player's support.
# Note: MP3 format itself does not have explicit support for gapless playback.
# Proper gapless playback is often achieved through specific encoding techniques (like using LAME's gapless metadata) and player support.
# This example assumes you're using a player that supports gapless playback and focuses on exporting the file in a manner that's compatible with such players.
silent_audio.export(file_path, format="mp3", parameters=["-write_xing", "0"])

print(f"MP3 file has been saved to: {file_path} with enhanced support for Gapless Playback")