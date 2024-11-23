import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_stereo_tone(frequency_left=440, frequency_right=523.25, duration_ms=60000, fade_in_ms=5000, fade_out_ms=5000):
    """Generate a stereo sine wave tone with specified frequencies for left and right channels, and with fade in and out."""
    tone_left = Sine(frequency_left).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    tone_right = Sine(frequency_right).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    return AudioSegment.from_mono_audiosegments(tone_left, tone_right)

# Generate a 1-minute stereo sine wave tone with different frequencies for each channel and with fades
tone = generate_stereo_tone(frequency_left=440, frequency_right=523.25, duration_ms=60000)

# Pan C5 from left to right
# Note: Pydub doesn't directly support dynamic panning in stereo generation in the mutated code, so this step is simplified to stereo generation.
# If dynamic panning was a critical part of the original approach, consider incorporating it through more complex audio manipulation than provided here.

# Export to MP3 with enhanced naming
file_path = './tmp/complex_sine_wave_stereo.mp3'
tone.export(file_path, format="mp3")

print(f"Generated complex MP3 file saved at: {file_path}")