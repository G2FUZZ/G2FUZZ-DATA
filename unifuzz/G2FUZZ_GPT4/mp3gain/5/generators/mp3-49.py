import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a tone with specified frequency, duration, and volume
def generate_tone(frequency, duration_ms, volume_db=-20):
    tone = Sine(frequency).to_audio_segment(duration=duration_ms).apply_gain(volume_db)
    return tone

# Generate different tones
tone1 = generate_tone(440, 5000)  # A4 for 5 seconds
tone2 = generate_tone(880, 3000, -10)  # A5 for 3 seconds, a bit louder
tone3 = generate_tone(660, 2000)  # E5 for 2 seconds

# Create a silence segment
silence = AudioSegment.silent(duration=1000)  # 1 second of silence

# Combine all the tones with silence in between
combined_tones = tone1 + silence + tone2 + silence + tone3

# You might also create more complex structures, like looping a segment
looped_tone = tone3 * 2  # Repeat the tone3 segment twice

# Add the looped tone to the end, with silence in between
final_audio = combined_tones + silence + looped_tone

# Export the combined tones as an MP3 file
final_audio.export("./tmp/complex_structure_tone.mp3", format="mp3")

print("Exported a complex structured tone as MP3.")