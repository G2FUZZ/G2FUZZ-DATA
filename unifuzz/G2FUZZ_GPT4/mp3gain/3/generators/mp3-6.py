import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the tmp directory exists
os.makedirs("./tmp", exist_ok=True)  # Corrected the argument here

# Generate a 5-second sine wave tone at 440 Hz
tone = Sine(440).to_audio_segment(duration=5000)

# Export the audio segment to a VBR MP3 file
# Specifying parameters for VBR (Variable Bit Rate) using the 'parameters' argument with ffmpeg
tone.export("./tmp/vbr_sine_wave.mp3", format="mp3", parameters=["-q:a", "0"])  # '-q:a 0' specifies the highest VBR quality