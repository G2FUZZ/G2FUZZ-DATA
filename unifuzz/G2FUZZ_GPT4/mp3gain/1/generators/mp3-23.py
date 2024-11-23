from pydub import AudioSegment
from pydub.generators import Sine
import os

def apply_3d_effect(sound, intensity=0.02):
    """
    Applies a simple 3D sound processing effect to an AudioSegment.
    The effect is achieved by delaying one channel slightly.
    
    :param sound: The AudioSegment to process.
    :param intensity: The delay time between the left and right channels in seconds. Default is 0.02 seconds.
    :return: Processed AudioSegment with 3D effect.
    """
    channels = sound.split_to_mono()
    
    # Ensure there are two channels, duplicating the channel for mono sounds
    if len(channels) == 1:
        channels.append(channels[0])
    
    left_channel, right_channel = channels
    right_channel = right_channel.invert_phase()

    # Delay one of the channels to simulate 3D sound
    delay = int(sound.frame_rate * intensity)
    right_channel_delayed = AudioSegment.silent(delay, frame_rate=sound.frame_rate) + right_channel

    # Ensure both channels are of the same length after adding the delay
    if len(left_channel) > len(right_channel_delayed):
        right_channel_delayed += AudioSegment.silent(len(left_channel) - len(right_channel_delayed), frame_rate=sound.frame_rate)
    else:
        left_channel += AudioSegment.silent(len(right_channel_delayed) - len(left_channel), frame_rate=sound.frame_rate)

    # Merge the channels back
    return AudioSegment.from_mono_audiosegments(left_channel, right_channel_delayed)

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a 440 Hz sine wave (A4 note) for 5 seconds
frequency = 440  # Frequency in Hz
duration = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generate sine wave
tone = Sine(frequency, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)

# Apply 3D Sound Processing
tone_with_3d = apply_3d_effect(tone)

# Save the generated tone with 3D effect as an MP3 file
output_path = os.path.join(output_dir, 'generated_tone_3d.mp3')
tone_with_3d.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file with 3D Sound Processing saved to {output_path}")