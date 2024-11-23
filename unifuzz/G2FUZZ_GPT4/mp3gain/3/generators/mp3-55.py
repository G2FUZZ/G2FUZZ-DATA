from pydub import AudioSegment
from pydub.generators import Sine
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_stereo_tone(frequencies=(440, 444), duration_ms=3000, volume_changes=(0, -3)):
    """
    Generate a stereo sine wave tone with different frequencies and volume levels for each channel.
    frequencies: A tuple containing the frequencies for the left and right channels.
    duration_ms: Duration of the tone in milliseconds.
    volume_changes: A tuple containing the volume changes (in dB) for the left and right channels.
    """
    tone_left = Sine(frequencies[0]).to_audio_segment(duration=duration_ms).apply_gain(volume_changes[0])
    tone_right = Sine(frequencies[1]).to_audio_segment(duration=duration_ms).apply_gain(volume_changes[1])
    stereo_tone = AudioSegment.from_mono_audiosegments(tone_left, tone_right)
    return stereo_tone

def split_stereo_tone_into_files(tone, split_duration_ms=1000, directory="./tmp/", prefix="part", format="mp3", crossfade_ms=500):
    """
    Split a stereo tone into multiple parts, apply crossfade effect between parts, 
    and save them as MP3 files with stereo channels.
    """
    parts = []
    for i, chunk in enumerate(tone[::split_duration_ms]):
        filename = f"{directory}{prefix}{i+1}.{format}"
        if i > 0:
            # Apply crossfade with the previous chunk
            parts[-1] = parts[-1].append(chunk, crossfade=crossfade_ms)
        else:
            parts.append(chunk)
        chunk.export(filename, format=format, parameters=["-write_xing", "0"])  # Disable Xing header for streaming support
        print(f"Exported {filename}")
    return parts

def combine_stereo_tones(*tones, format="mp3"):
    """
    Combine multiple stereo tones by overlaying them on top of each other.
    tones: A list of AudioSegment objects.
    """
    combined_tone = tones[0]
    for tone in tones[1:]:
        combined_tone = combined_tone.overlay(tone)
    return combined_tone

def export_stereo_tone(tone, filename="./tmp/combined_stereo_tone.mp3", format="mp3"):
    """
    Export the given stereo tone to a file.
    """
    tone.export(filename, format=format)
    print(f"Exported tone to {filename}")

def generate_and_export_complex_stereo_tone():
    """
    Generate a complex stereo tone by combining multiple stereo tones with different frequencies 
    and volume levels, and export it to a file.
    """
    # Generate individual tones
    tone1 = generate_stereo_tone(frequencies=(440, 442), volume_changes=(0, -2))
    tone2 = generate_stereo_tone(frequencies=(660, 664), duration_ms=1500, volume_changes=(-3, -5))
    
    # Combine tones
    combined_tone = combine_stereo_tones(tone1, tone2)
    
    # Export the combined tone
    export_stereo_tone(combined_tone)

# Example usage
generate_and_export_complex_stereo_tone()

print("Complex MP3 file generated and merged with crossfade successfully.")