from pydub import AudioSegment
from pydub.generators import Sine
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_stereo_tone(frequencies=(440, 444), duration_ms=3000, volume_changes=(0, 0), fade_in_ms=500, fade_out_ms=500):
    """
    Generate a stereo sine wave tone with different frequencies for each channel,
    apply volume changes, and add fade in and out effects.
    """
    tone_left = Sine(frequencies[0]).to_audio_segment(duration=duration_ms).apply_gain(volume_changes[0]).fade_in(fade_in_ms).fade_out(fade_out_ms)
    tone_right = Sine(frequencies[1]).to_audio_segment(duration=duration_ms).apply_gain(volume_changes[1]).fade_in(fade_in_ms).fade_out(fade_out_ms)
    stereo_tone = AudioSegment.from_mono_audiosegments(tone_left, tone_right)
    return stereo_tone

def combine_tones(*tones, format="mp3"):
    """
    Combine multiple tones by overlaying them on top of each other.
    """
    combined_tone = tones[0]
    for tone in tones[1:]:
        combined_tone = combined_tone.overlay(tone)
    return combined_tone

def export_tone(tone, filename="./tmp/complex_stereo_tone.mp3", format="mp3"):
    """
    Export the given tone to a file.
    """
    tone.export(filename, format=format)
    print(f"Exported tone to {filename}")

def generate_and_export_complex_tone():
    """
    Generate a complex tone by combining multiple stereo tones with different frequencies, volume levels, and fades,
    and export it to a file.
    """
    # Generate individual tones
    tone1 = generate_stereo_tone(frequencies=(440, 554), volume_changes=(0, -2), fade_in_ms=500, fade_out_ms=500)
    tone2 = generate_stereo_tone(frequencies=(660, 668), duration_ms=1500, volume_changes=(-3, -5), fade_in_ms=250, fade_out_ms=250)
    
    # Combine tones
    combined_tone = combine_tones(tone1, tone2)
    
    # Export the combined tone
    export_tone(combined_tone)

# Example usage
generate_and_export_complex_tone()

print("Complex MP3 file generated successfully.")