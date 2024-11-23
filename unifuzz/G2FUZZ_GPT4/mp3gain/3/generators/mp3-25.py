import os
from pydub import AudioSegment
from pydub.generators import Sine
import eyed3

# Ensure the tmp directory exists
os.makedirs("./tmp/", exist_ok=True)

# Generate a simple sine wave audio segment for 5 seconds
duration_in_milliseconds = 5000
frequency_hz = 440  # A4 note
audio_segment = Sine(frequency_hz).to_audio_segment(duration=duration_in_milliseconds)

# Define the path for the new mp3 file
mp3_file_path = "./tmp/generated_audio.mp3"

# Adjustable Quality Levels parameters
bit_rate = "192k"  # Bit rate for the output MP3 file
# Other parameters like sample rate (in Hz) could also be adjusted if needed, e.g., sample_rate=44100

# Export the audio segment to an MP3 file with specified quality levels
audio_segment.export(mp3_file_path, format="mp3", bitrate=bit_rate)

# Load the MP3 file using eyed3 for editing ID3 tags
audio_file = eyed3.load(mp3_file_path)

# If the file had no ID3 tag, one will be created
if audio_file.tag is None:
    audio_file.initTag()

# Set various ID3 tags
audio_file.tag.title = "Generated Sine Wave"
audio_file.tag.artist = "Python Script"
audio_file.tag.album = "Python Generated"
audio_file.tag.genre = "Experimental"
audio_file.tag.save()

print("MP3 file with ID3 tags and adjustable quality levels generated and saved.")