from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def generate_tone(frequency, duration_ms, pan=None):
    """
    Generate a sine wave tone with the given frequency and duration.
    If pan is specified (value between -1 and 1), the tone will be panned accordingly.
    """
    tone = Sine(frequency).to_audio_segment(duration=duration_ms)
    if pan is not None:
        tone = tone.pan(pan)
    return tone

# Generate several tones with different properties
tone1 = generate_tone(440, 2000)  # A 2-second tone at 440 Hz
tone2 = generate_tone(660, 3000, pan=-0.5)  # A 3-second tone at 660 Hz, panned left
tone3 = generate_tone(880, 4000, pan=0.5)  # A 4-second tone at 880 Hz, panned right

# Overlay the tones to create a complex sound
complex_sound = tone1.overlay(tone2).overlay(tone3)

# Generate another tone and concatenate it to the complex sound
tone4 = generate_tone(330, 5000)  # A 5-second tone at 330 Hz
complex_sound = complex_sound.append(tone4, crossfade=1000)  # Crossfade of 1 second

# Export the complex sound to an MP3 file
file_path = './tmp/complex_sine_wave.mp3'
complex_sound.export(file_path, format="mp3", bitrate="192k")

print(f"Complex file has been saved to {file_path}")