import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_stereo_tone(frequency_left=440, frequency_right=554, duration_ms=5000, fade_in_ms=500, fade_out_ms=500):
    """Generate a stereo sine wave tone with different frequencies for each channel, including fade in and fade out."""
    tone_left = Sine(frequency_left).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    tone_right = Sine(frequency_right).to_audio_segment(duration=duration_ms).fade_in(fade_in_ms).fade_out(fade_out_ms)
    return AudioSegment.from_mono_audiosegments(tone_left, tone_right)

# Generate a sine wave tone as an example of audio data with stereo, fade in, and fade out effects
# This will represent our "frame structure" concept in a rudimentary way but with added complexity

# Generate the stereo sine wave tone with different frequencies for each channel and with fades
tone = generate_stereo_tone(frequency_left=440, frequency_right=554, duration_ms=5000)

# Setting up multiple frames (in a very basic representation) by concatenating the same tone,
# simulating multiple frames of data in an MP3 file, but now with stereo sound
frames_to_generate = 5  # Number of frames to simulate
audio_frames = tone
for _ in range(1, frames_to_generate):
    audio_frames += tone

# Export the generated frames as an MP3 file, with naming that reflects the new stereo capabilities
audio_frames.export("./tmp/generated_stereo_frames.mp3", format="mp3")