import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone as an example audio
tone = Sine(440).to_audio_segment(duration=5000)  # 440 Hz for 5 seconds

# Export the audio to an MP3 file with error protection enabled
# Note: The PyDub library itself does not expose MP3 encoding options such as error protection directly.
# Error protection (CRC) can be enabled in MP3 files using specific encoding options available in the
# underlying encoding library/tool (like LAME) if you are using it directly. However, PyDub abstracts these
# details away and does not provide direct access to such low-level encoding options through its API.
# As a result, we will simulate the process of exporting an MP3 file here without actual error protection.
file_path = './tmp/example_tone.mp3'
tone.export(file_path, format="mp3")

print(f"Generated MP3 file saved to: {file_path}")