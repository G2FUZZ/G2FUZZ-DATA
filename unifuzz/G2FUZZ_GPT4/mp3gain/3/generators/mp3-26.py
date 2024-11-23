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

def generate_looped_tone(frequency=440, duration_ms=3000, loop_duration_ms=1000, directory="./tmp/", prefix="looped_part", format="mp3"):
    """
    Generate a sine wave tone, split it into multiple parts,
    and save each part as an MP3 file designed for seamless looping.
    The last part is crossfaded with the first part to create a seamless loop point.
    """
    tone = Sine(frequency).to_audio_segment(duration=duration_ms)
    full_loop = tone[:loop_duration_ms]

    # Crossfade the end and start of the loop to create a seamless loop point
    crossfade_duration = int(loop_duration_ms * 0.1)  # 10% of the loop duration
    looped_tone = full_loop.fade_out(crossfade_duration).fade_in(crossfade_duration)

    # Export the looped tone
    filename = f"{directory}{prefix}.{format}"
    looped_tone.export(filename, format=format)
    print(f"Exported looped tone {filename}")

# Example usage
generate_tone()

# Split the tone into 3 parts of 1 second each and save as MP3
split_tone_into_files(generate_tone(), 1000)

# Generate a 3-second tone designed for seamless looping
generate_looped_tone()

print("MP3 files generated successfully.")