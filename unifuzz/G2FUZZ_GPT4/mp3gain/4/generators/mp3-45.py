import os
import numpy as np
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequencies, duration_ms=1000, volume=0.5, sample_rate=44100, pan=0.0):
    if not isinstance(frequencies, list):
        frequencies = [frequencies]
    
    waves = []
    for frequency in frequencies:
        t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), False)
        wave = np.sin(frequency * t * 2 * np.pi) * volume
        waves.append(wave)
    
    # Mix down to a single wave
    wave = np.sum(np.array(waves), axis=0) / len(frequencies)
    
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

def generate_melody(frequencies, durations, volume=0.5, sample_rate=44100, pan=0.0):
    melody = np.empty((0, 2), int)
    for frequency, duration in zip(frequencies, durations):
        tone = generate_tone(frequency, duration_ms=duration, volume=volume, sample_rate=sample_rate, pan=pan)
        melody = np.vstack((melody, tone))
    return melody

# Define a simple song structure
melody_frequencies = [440, 494, 523, 587, 659, 698, 784]
melody_durations = [500, 500, 500, 500, 500, 500, 500]
harmony_frequencies = [[349, 440], [392, 494], [440, 523], [494, 587], [523, 659], [587, 698], [659, 784]]
harmony_durations = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
bass_frequencies = [220, 247, 262, 294, 330, 349, 392]
bass_durations = [1000, 1000, 1000, 1000, 1000, 1000, 1000]

# Generate song parts
melody = generate_melody(melody_frequencies, melody_durations, volume=0.5, pan=0.0)
harmony = np.empty((0, 2), int)
for frequencies, duration in zip(harmony_frequencies, harmony_durations):
    tone = generate_tone(frequencies, duration_ms=duration, volume=0.4, pan=0.0)
    harmony = np.vstack((harmony, tone))
bass = generate_melody(bass_frequencies, bass_durations, volume=0.6, pan=-0.5)

# Combine parts
# Ensure all parts are of the same length before combining
max_length = max(melody.shape[0], harmony.shape[0], bass.shape[0])
pad_with_zeros = lambda array, length: np.vstack((array, np.zeros((length - array.shape[0], array.shape[1]), dtype=array.dtype)))
melody_padded = pad_with_zeros(melody, max_length)
harmony_padded = pad_with_zeros(harmony, max_length)
bass_padded = pad_with_zeros(bass, max_length)

combined_audio = melody_padded + harmony_padded + bass_padded
combined_audio = apply_fade(combined_audio, 44100, 1000, 1000)

# Convert the NumPy array to bytes and create a PyDub audio segment
audio_bytes = combined_audio.tobytes()
audio_segment = AudioSegment(audio_bytes, sample_width=2, frame_rate=44100, channels=2)

# Save the song
audio_segment.export("./tmp/song.mp3", format="mp3")

print("Song generated in './tmp/' directory.")