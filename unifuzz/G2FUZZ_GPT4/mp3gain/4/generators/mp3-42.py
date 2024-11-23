import os
import numpy as np
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave tone with stereo and panning support
def generate_tone(frequency=440, duration_ms=1000, volume=0.5, sample_rate=44100, pan=0.0):
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), False)
    wave = np.sin(frequency * t * 2 * np.pi) * volume
    # Normalize to 16-bit range
    audio = wave * (2**15 - 1)
    audio = audio.astype(np.int16)
    # Pan the note left or right
    if pan != 0.0:
        left = audio * min(1.0 - pan, 1.0)
        right = audio * min(1.0 + pan, 1.0)
        audio = np.vstack((left, right)).T
    else:
        audio = np.vstack((audio, audio)).T  # Make it stereo without panning
    return audio

# Function to apply fade in and fade out
def apply_fade(audio, sample_rate, fade_in_duration_ms, fade_out_duration_ms):
    num_samples = audio.shape[0]
    fade_in_samples = int(fade_in_duration_ms * sample_rate / 1000)
    fade_out_samples = int(fade_out_duration_ms * sample_rate / 1000)

    # Apply fade in
    for i in range(fade_in_samples):
        audio[i, :] = audio[i, :] * (i / fade_in_samples)
    
    # Apply fade out
    for i in range(fade_out_samples):
        audio[-i-1, :] = audio[-i-1, :] * (i / fade_out_samples)
    
    return audio

# Generate a tone for left and right channels with panning and apply fade in/out
left_channel = generate_tone(frequency=440, volume=0.5, pan=-0.5)  # A4 note, panned left
right_channel = generate_tone(frequency=660, volume=0.5, pan=0.5)  # E5 note, panned right
stereo_audio = np.vstack((left_channel, right_channel))  # Combine into a single stereo track

# Apply fade in and fade out
stereo_audio = apply_fade(stereo_audio, 44100, 100, 100)  # 100 ms for both fade in and fade out

# Convert the NumPy array to bytes and create a PyDub audio segment
audio_bytes = stereo_audio.tobytes()
audio_segment = AudioSegment(audio_bytes, sample_width=2, frame_rate=44100, channels=2)

# Save stereo audio
audio_segment.export("./tmp/stereo_mode.mp3", format="mp3")

# Create and save a mono file by mixing down the stereo file
mono_audio = audio_segment.set_channels(1)
mono_audio.export("./tmp/mono_mode.mp3", format="mp3")

print("MP3 files generated in './tmp/' directory.")