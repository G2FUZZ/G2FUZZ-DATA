from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 5-second silent audio segment
silent_audio = AudioSegment.silent(duration=5000)  # Duration in milliseconds

# Export the audio segment as an MP3 file with frequency cut-off options
file_path = './tmp/silent_audio_with_cutoff.mp3'

# Set parameters for frequency cut-off
# These parameters can be adjusted to suit specific requirements for the cut-off frequency
parameters = {
    "bitrate": "192k",  # Bitrate of the output file
    "parameters": ["-ar", "16000"]  # `-ar` specifies the audio sampling rate which affects the frequency cut-off
}

silent_audio.export(file_path, format="mp3", **parameters)

print(f"MP3 file with frequency cut-off has been saved to: {file_path}")