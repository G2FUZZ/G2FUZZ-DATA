import os
from pydub import AudioSegment
from pydub.generators import Sine
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TRCK, TYER, USLT
from mutagen.mp3 import MP3

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple sine wave tones for 2 seconds each, with different frequencies
tones = [Sine(frequency).to_audio_segment(duration=2000) for frequency in [440, 550, 660]]

# Combine tones into a single track
combined_tone = AudioSegment.silent(duration=0)
for tone in tones:
    combined_tone += tone

# Apply a fade in and fade out to the combined tone
combined_tone = combined_tone.fade_in(200).fade_out(200)

# Adjust volume, making the first half quieter
first_half, second_half = combined_tone[:len(combined_tone)//2], combined_tone[len(combined_tone)//2:]
first_half = first_half - 10  # Decrease volume by 10 dB
combined_tone = first_half + second_half

# Ensure combined_tone is mono before proceeding
combined_tone = combined_tone.set_channels(1)

# Create left and right channels by panning
left_channel = combined_tone.pan(-1)  # Pan fully to the left
right_channel = combined_tone.pan(1)  # Pan fully to the right

# Create a silent stereo track to overlay the left and right channels onto
silent_stereo = AudioSegment.silent(duration=combined_tone.duration_seconds * 1000, frame_rate=combined_tone.frame_rate).set_channels(2)

# Overlay the left and right channels onto the silent stereo track
stereo_tone = silent_stereo.overlay(left_channel).overlay(right_channel, position=0)

# Save the generated tone to a file with adjustable quality settings
file_path = './tmp/complex_generated_tone.mp3'

# Export the stereo tone with VBR quality settings
stereo_tone.export(file_path, format="mp3", parameters=["-q:a", "5"])

# Add metadata to the mp3 file
audio = MP3(file_path, ID3=ID3)

# Add various metadata
audio.tags.add(TIT2(encoding=3, text='Complex Generated Tone'))
audio.tags.add(TPE1(encoding=3, text='Advanced Python Script'))
audio.tags.add(TALB(encoding=3, text='Complex Generated Sounds'))
audio.tags.add(TCON(encoding=3, text='Experimental Synth'))
audio.tags.add(TRCK(encoding=3, text='1'))
audio.tags.add(TYER(encoding=3, text='2023'))

# Optional: Add lyrics
audio.tags.add(USLT(encoding=3, lang=u'eng', desc='desc', text='This is a complex generated MP3 file with multiple tones and stereo effects.'))

audio.save()

print(f"Complex generated MP3 with advanced features and metadata saved to {file_path}")