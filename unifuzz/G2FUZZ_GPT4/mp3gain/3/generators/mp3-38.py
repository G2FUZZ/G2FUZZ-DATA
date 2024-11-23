from pydub import AudioSegment
from pydub.generators import Sine
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_stereo_tone(frequency_left=440, frequency_right=440, duration_ms=3000, fade_in_ms=500, fade_out_ms=500):
    """Generate a stereo sine wave tone with specified frequencies for left and right channels, and with fade in and out."""
    tone_left = Sine(frequency_left).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    tone_right = Sine(frequency_right).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    return AudioSegment.from_mono_audiosegments(tone_left, tone_right)

def split_tone_into_files(tone, split_duration_ms=1000, directory="./tmp/", prefix="part", format="mp3"):
    """Split a tone into multiple parts and save them as MP3 files, with enhanced naming including frequency information."""
    split_count = len(tone) // split_duration_ms
    for i in range(split_count):
        start_ms = i * split_duration_ms
        end_ms = start_ms + split_duration_ms
        chunk = tone[start_ms:end_ms]
        filename = f"{directory}{prefix}_{i+1}_of_{split_count}.{format}"
        chunk.export(filename, format=format)
        print(f"Exported {filename}")

# Generate a 3-second stereo sine wave tone with different frequencies for each channel and with fades
tone = generate_stereo_tone(frequency_left=440, frequency_right=554, duration_ms=3000)

# Split the tone into 3 parts of 1 second each and save as MP3
split_tone_into_files(tone, 1000)

print("MP3 files generated successfully.")