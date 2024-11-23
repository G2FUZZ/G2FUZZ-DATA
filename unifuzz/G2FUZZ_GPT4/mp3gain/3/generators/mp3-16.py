from pydub import AudioSegment
from pydub.generators import Sine
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequency=440, duration_ms=3000):
    """Generate a sine wave tone of a given frequency and duration."""
    return Sine(frequency).to_audio_segment(duration=duration_ms)

def split_tone_into_files(tone, split_duration_ms=1000, directory="./tmp/", prefix="part", format="mp3", crossfade_ms=500):
    """Split a tone into multiple parts, apply crossfade effect between parts, and save them as MP3 files."""
    parts = []
    for i, chunk in enumerate(tone[::split_duration_ms]):
        filename = f"{directory}{prefix}{i+1}.{format}"
        if i > 0:
            # Apply crossfade with the previous chunk
            parts[-1] = parts[-1].append(chunk, crossfade=crossfade_ms)
        else:
            parts.append(chunk)
        chunk.export(filename, format=format)
        print(f"Exported {filename}")
    return parts

def merge_files_with_crossfade(parts, output_filename="merged_with_crossfade.mp3", format="mp3"):
    """Merge audio segments with crossfade and save to a single MP3 file."""
    combined = parts[0]
    for part in parts[1:]:
        combined = combined.append(part, crossfade=500)  # Apply crossfade between consecutive parts
    combined.export(output_filename, format=format)
    print(f"Merged file with crossfade saved as {output_filename}")

# Generate a 3-second sine wave tone
tone = generate_tone()

# Split the tone into 3 parts of 1 second each, apply crossfade, and save as MP3
parts = split_tone_into_files(tone, 1000, crossfade_ms=500)

# Merge saved parts with crossfade into a single file
merge_files_with_crossfade(parts)

print("MP3 files generated and merged with crossfade successfully.")