import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a continuous sine wave for 10 seconds
tone1 = Sine(440).to_audio_segment(duration=10000)
# Generate another sine wave for 10 seconds, slightly higher pitch for differentiation
tone2 = Sine(444).to_audio_segment(duration=10000)

# Concatenate the two sine waves to simulate gapless playback
combined = tone1 + tone2

# Export the combined audio to an MP3 file, ensuring gapless playback by setting parameters appropriately
# Note: The gapless playback feature is more about how players handle MP3 files rather than the MP3 encoding itself.
# However, using constant bitrate (CBR) can help some players manage gapless playback more effectively.
combined.export("./tmp/gapless_playback.mp3", format="mp3", bitrate="192k")

print("MP3 file with simulated gapless playback generated successfully.")