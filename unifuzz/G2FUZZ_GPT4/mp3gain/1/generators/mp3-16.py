import os
from pydub import AudioSegment
from pydub.generators import Sine
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TRCK, TYER, APIC, COMM
from mutagen.mp3 import MP3

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone for 5 seconds, 440 Hz
tone = Sine(440).to_audio_segment(duration=5000)

# Save the generated tone to a file, attempting to optimize for high efficiency
file_path = './tmp/generated_tone_with_sbr.mp3'

# For demonstration, using lower bit rates with VBR to simulate efficiency improvements
bit_rate = "64k"  # Lower bit rates may benefit from SBR-like efficiency improvements
vbr = "4"  # VBR quality, aiming for efficient compression

# Exporting with VBR settings, which is closest to what we can achieve for SBR simulation in MP3
tone.export(file_path, format="mp3", parameters=["-q:a", vbr])

# Add metadata to the mp3 file
audio = MP3(file_path, ID3=ID3)

# Add various metadata
audio.tags.add(TIT2(encoding=3, text='Generated Tone with SBR Simulation'))
audio.tags.add(TPE1(encoding=3, text='Python Script'))
audio.tags.add(TALB(encoding=3, text='Generated Sounds'))
audio.tags.add(TCON(encoding=3, text='Synth'))
audio.tags.add(TRCK(encoding=3, text='1'))
audio.tags.add(TYER(encoding=3, text='2023'))

# Optional: Add a comment
audio.tags.add(COMM(encoding=3, lang=u'eng', desc='desc', text='This MP3 simulates SBR-like efficiency using VBR settings'))

audio.save()

print(f"Generated MP3 with SBR simulation (via VBR settings) and metadata saved to {file_path}")