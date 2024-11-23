import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple sine wave tones with varying frequencies, durations, and volumes
tones = [
    {'frequency': 440, 'duration': 1000, 'volume': -5.0},  # A4 note, 1 second, quieter
    {'frequency': 494, 'duration': 500, 'volume': -2.0},   # B4 note, 0.5 seconds, a bit quieter
    {'frequency': 523, 'duration': 1500, 'volume': 0.0},   # C5 note, 1.5 seconds, normal volume
    {'frequency': 587, 'duration': 500, 'volume': -2.0},   # D5 note, 0.5 seconds, a bit quieter
    {'frequency': 659, 'duration': 1000, 'volume': -5.0},  # E5 note, 1 second, quieter
]

# Create an empty AudioSegment for combining the tones
combined_tones = AudioSegment.empty()

# Generate and combine the tones
for tone in tones:
    generated_tone = Sine(tone['frequency']).to_audio_segment(duration=tone['duration']).apply_gain(tone['volume'])
    combined_tones += generated_tone

# Optionally, add a fade-in at the beginning and a fade-out at the end
combined_tones = combined_tones.fade_in(200).fade_out(200)

# Specify the parameters for MPEG-2.5 Extension
file_path = './tmp/complex_audio_mpeg2_5.mp3'
# The combined tones are exported with a constant bitrate and MPEG-2.5 Extension by manually setting a low sample rate (8 kHz),
# which is one of the features MPEG-2.5 allows for. This simulates the effect of MPEG-2.5.
combined_tones.set_frame_rate(8000).export(file_path, format="mp3", bitrate="192k", parameters=["-ar", "8000"])

print(f"Generated a complex MP3 file with varying tones and MPEG-2.5 Extension at {file_path}")