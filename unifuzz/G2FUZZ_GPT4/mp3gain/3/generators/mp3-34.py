import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate two 1-minute sine waves at different frequencies
duration_in_milliseconds = 60 * 1000  # 1 minute in milliseconds
frequency_a4 = 440  # Frequency in Hertz for A4
frequency_c5 = 523.25  # Frequency in Hertz for C5

# Generate sine waves
tone_a4 = Sine(frequency_a4).to_audio_segment(duration=duration_in_milliseconds)
tone_c5 = Sine(frequency_c5).to_audio_segment(duration=duration_in_milliseconds)

# Apply fade-in to the first tone and fade-out to both tones
fade_duration = 5000  # 5 seconds in milliseconds
tone_a4 = tone_a4.fade_in(fade_duration).fade_out(fade_duration)
tone_c5 = tone_c5.fade_out(fade_duration)

# Create stereo tracks by panning tones
# Pan A4 to center (no change needed for mono to stereo conversion)
stereo_tone_a4 = tone_a4.set_channels(2)

# Pan C5 from left to right
# Note: Pydub doesn't directly support panning a mono track to stereo with variable panning over time,
# so as an approximation, we'll split the tone into segments and adjust their panning progressively.
segments_count = 10
segment_duration = duration_in_milliseconds // segments_count
stereo_segments = []

for i in range(segments_count):
    segment = tone_c5[i * segment_duration:(i + 1) * segment_duration]
    pan_position = (i / (segments_count - 1)) * 2 - 1  # Scale from -1 to 1
    stereo_segment = segment.pan(pan_position).set_channels(2)
    stereo_segments.append(stereo_segment)

# Combine segments back to a single track
stereo_tone_c5 = sum(stereo_segments)

# Mix both stereo tracks
combined_tones = stereo_tone_a4.overlay(stereo_tone_c5)

# Export to MP3 with default parameters
file_path = './tmp/complex_sine_wave.mp3'
combined_tones.export(file_path, format="mp3")

print(f"Generated complex MP3 file saved at: {file_path}")