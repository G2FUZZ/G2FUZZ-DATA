from pydub import AudioSegment
from pydub.generators import Sine
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequency=440, duration_ms=3000):
    """Generate a sine wave tone of a given frequency and duration."""
    return Sine(frequency).to_audio_segment(duration=duration_ms)

def split_tone_into_files(tone, split_duration_ms=1000, directory="./tmp/", prefix="part", format="mp3"):
    """Split a tone into multiple parts and save them as MP3 files."""
    for i, chunk in enumerate(tone[::split_duration_ms]):
        filename = f"{directory}{prefix}{i+1}.{format}"
        chunk.export(filename, format=format)
        print(f"Exported {filename}")

# Generate a 3-second sine wave tone
tone = generate_tone()

# Split the tone into 3 parts of 1 second each and save as MP3
split_tone_into_files(tone, 1000)

print("MP3 files generated successfully.")