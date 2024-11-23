import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone as an example of audio data
tone = Sine(440).to_audio_segment(duration=3000)

# Check if the voice_over.mp3 file exists, if not, generate a placeholder
voice_over_path = "./tmp/voice_over.mp3"
if not os.path.exists(voice_over_path):
    # Generate a 1kHz sine wave (placeholder for voice-over) that lasts for 2 seconds
    voice_over_tone = Sine(1000).to_audio_segment(duration=2000)
    voice_over_tone.export(voice_over_path, format="mp3")

# Now, load the voice_over.mp3 file
voice_over = AudioSegment.from_mp3(voice_over_path)

# Assume background_music.mp3 exists in the ./tmp/ directory or generate similarly
background_music_path = "./tmp/background_music.mp3"
if not os.path.exists(background_music_path):
    # Generate a placeholder for background music if it doesn't exist
    background_music_tone = Sine(260).to_audio_segment(duration=10000)  # Longer duration for background
    background_music_tone.export(background_music_path, format="mp3")

background_music = AudioSegment.from_mp3(background_music_path)

# Lower the volume of the background music
background_music = background_music - 20

# Mix the tone with the voice-over
mixed = tone.overlay(voice_over, position=1000)

# Overlay the mixed audio on top of the background music
final_mix = background_music.overlay(mixed, position=0)

# Exporting the final mix to an MP3 file
final_mix.export("./tmp/complex_generated_tone.mp3", format="mp3")