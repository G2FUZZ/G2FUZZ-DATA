import os
from pydub import AudioSegment
from pydub.generators import Sine, Square, WhiteNoise
from pydub.playback import play

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate different tones with Sine and Square waves as examples of audio data
tone_sine = Sine(440).to_audio_segment(duration=3000)
tone_square = Square(440).to_audio_segment(duration=3000)

# Generate a white noise segment
white_noise = WhiteNoise().to_audio_segment(duration=1000)

# Applying fading in and fading out to the tones
tone_sine_fade = tone_sine.fade_in(1000).fade_out(1000)
tone_square_fade = tone_square.fade_in(500).fade_out(500)

# Generate a voice-over placeholder with fading and stereo manipulation
voice_over_path = "./tmp/voice_over_complex.mp3"
if not os.path.exists(voice_over_path):
    voice_over_tone = Sine(1000).to_audio_segment(duration=2000).fade_in(200).fade_out(500)
    voice_over_tone_stereo = voice_over_tone.set_channels(2)  # Make it stereo
    voice_over_tone_stereo.export(voice_over_path, format="mp3")

voice_over = AudioSegment.from_mp3(voice_over_path)

# Assume complex_background_music.mp3 exists in the ./tmp/ directory or generate similarly
background_music_path = "./tmp/complex_background_music.mp3"
if not os.path.exists(background_music_path):
    background_music_tone = WhiteNoise().to_audio_segment(duration=10000).fade_in(2000).fade_out(2000)
    background_music_tone.export(background_music_path, format="mp3")

background_music = AudioSegment.from_mp3(background_music_path)

# Lower the volume of the background music and apply panning
background_music = background_music - 20
background_music = background_music.pan(-0.5)  # Pan to the left

# Mix the tones with voice-over, including silence at the beginning
silence = AudioSegment.silent(duration=1000)  # 1 second of silence
mixed = silence + tone_sine_fade.overlay(voice_over, position=500) + tone_square_fade

# Overlay the mixed audio on top of the background music, applying stereo manipulation
final_mix = background_music.overlay(mixed, position=0).set_channels(2)

# Optional: Add white noise softly in the background
final_mix_with_noise = final_mix.overlay(white_noise - 30, loop=True)

# Exporting the final complex mix to an MP3 file
final_mix_with_noise.export("./tmp/complex_generated_tone_with_effects.mp3", format="mp3")

# Optionally, you can un-comment the line below to play the generated file (requires pydub playback support)
# play(final_mix_with_noise)