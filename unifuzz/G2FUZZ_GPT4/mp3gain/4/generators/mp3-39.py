import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave for a specific channel
def generate_tone(frequency, duration_ms=1000, volume=-20):
    """
    Generates a sine wave audio segment with the specified frequency and duration.

    :param frequency: Frequency of the sine wave in Hz.
    :param duration_ms: Duration of the tone in milliseconds.
    :param volume: Volume of the tone in dB.
    :return: A pydub AudioSegment representing the generated tone.
    """
    tone = Sine(frequency).to_audio_segment(duration=duration_ms).apply_gain(volume)
    return tone

# Generate a stereo audio with different frequencies for left and right channels
left_channel = generate_tone(440, 2000)  # 440 Hz for 2 seconds
right_channel = generate_tone(554, 2000)  # 554 Hz (C#5) for 2 seconds

stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Apply effects to the stereo audio
# Fade in for the first 2 seconds, fade out for the last 2 seconds
stereo_sound_effect = stereo_sound.fade_in(2000).fade_out(2000)

# Pan the audio (left to right and then right to left)
panned_sound = stereo_sound_effect.pan(-1).append(stereo_sound_effect.pan(1))

# Save the generated stereo sound with effects to a file
file_path_stereo = './tmp/stereo_tone_with_effects.mp3'
panned_sound.export(file_path_stereo, format="mp3")

# Add more complex metadata
metadata = {
    "artist": "PyDub Generator",
    "album": "Automated Album",
    "comments": "Generated stereo sound with fades and pan effects."
}

# Save the file with metadata
enhanced_with_metadata_path = './tmp/stereo_with_metadata.mp3'
panned_sound.export(enhanced_with_metadata_path, format="mp3", tags=metadata)

print(f"Stereo MP3 file with effects and metadata saved to './tmp/'")