import os
from pydub import AudioSegment
from pydub.generators import Sine
import eyed3

# Ensure the tmp directory exists
base_dir = "./tmp/"  # Adjusted to save files directly into ./tmp/
os.makedirs(base_dir, exist_ok=True)

# Define a simple melody as a list of chords, with each chord being a list of frequencies (in Hz)
melody = [
    [440, 554.37, 659.25],  # A major chord
    [523.25, 659.25, 783.99],  # C major chord
    [587.33, 739.99, 880.00],  # D major chord
    [659.25, 830.61, 987.77]  # E major chord
]

duration_in_milliseconds = 1000  # Duration of each chord
bit_rate = "192k"  # Bit rate for the output MP3 files

# Function to generate a chord from a list of frequencies
def generate_chord(frequencies, duration):
    chord = AudioSegment.silent(duration=duration)
    for freq in frequencies:
        sine_wave = Sine(freq).to_audio_segment(duration=duration)
        chord = chord.overlay(sine_wave)
    return chord

# Generate and save each chord in the melody
chord_files = []
for i, chord_frequencies in enumerate(melody):
    chord = generate_chord(chord_frequencies, duration_in_milliseconds)
    mp3_file_path = os.path.join(base_dir, f"chord_{i+1}.mp3")
    chord.export(mp3_file_path, format="mp3", bitrate=bit_rate)
    chord_files.append(mp3_file_path)

# Combine all the chord files into one final composition
final_composition = AudioSegment.silent(duration=0)
for file_path in chord_files:
    chord_segment = AudioSegment.from_mp3(file_path)  # Corrected variable here
    final_composition += chord_segment

# Define the path for the final mp3 file
final_mp3_file_path = os.path.join(base_dir, "final_composition.mp3")

# Export the final composition to an MP3 file
final_composition.export(final_mp3_file_path, format="mp3", bitrate=bit_rate)

# Load the final MP3 file using eyed3 for editing ID3 tags
audio_file = eyed3.load(final_mp3_file_path)

# If the file had no ID3 tag, one will be created
if audio_file.tag is None:
    audio_file.initTag()

# Set various ID3 tags for the final composition
audio_file.tag.title = "Generated Melody"
audio_file.tag.artist = "Python Script"
audio_file.tag.album = "Python Generated Music"
audio_file.tag.genre = "Experimental"
audio_file.tag.save()

print("Final composition MP3 file with ID3 tags generated and saved.")