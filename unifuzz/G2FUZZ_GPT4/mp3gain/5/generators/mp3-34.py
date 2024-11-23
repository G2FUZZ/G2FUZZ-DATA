import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple sine wave tones with varying frequencies, durations, and volumes
tones = [
    {'frequency': 440, 'duration': 1000, 'volume': -3.0},  # A4 note, 1 second, slightly quieter
    {'frequency': 494, 'duration': 500, 'volume': -1.0},   # B4 note, 0.5 seconds, a bit quieter
    {'frequency': 523, 'duration': 1500, 'volume': 0.0},   # C5 note, 1.5 seconds, normal volume
    {'frequency': 587, 'duration': 500, 'volume': -1.0},   # D5 note, 0.5 seconds, a bit quieter
    {'frequency': 659, 'duration': 1000, 'volume': -3.0},  # E5 note, 1 second, slightly quieter
]

# Create an empty AudioSegment for combining the tones
combined_tones = AudioSegment.empty()

# Generate and combine the tones
for tone in tones:
    generated_tone = Sine(tone['frequency']).to_audio_segment(duration=tone['duration']).apply_gain(tone['volume'])
    combined_tones += generated_tone

# Optionally, add a fade-in at the beginning and a fade-out at the end
combined_tones = combined_tones.fade_in(200).fade_out(200)

# Export the combined tones sequence to an MP3 file
combined_tones.export("./tmp/complex_tone_structure.mp3", format="mp3")

print("Exported a more complex MP3 file structure with multiple tones.")