import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

# Function to generate a sine wave, normalize it, encode it to MP3 with a specific stereo mode, and apply Replay Gain
def generate_normalized_sine_wave_mp3_with_replay_gain(stereo_mode, filename, duration_ms=1000, freq=440):
    # Generate stereo sine wave
    left_channel = Sine(freq).to_audio_segment(duration=duration_ms)
    right_channel = Sine(freq).to_audio_segment(duration=duration_ms)
    stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
    
    # Normalize the audio to a standard level
    normalized_sound = normalize(stereo_sound)

    # Convert to raw audio data
    raw_audio_data = normalized_sound.raw_data
    
    # Encoding settings
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(normalized_sound.frame_rate)
    encoder.set_channels(2)
    encoder.set_quality(2)  # High quality
    
    # Encode to MP3
    mp3_data = encoder.encode(raw_audio_data)
    mp3_data += encoder.flush()
    
    # Save to file
    with open(filename, 'wb') as f:
        f.write(mp3_data)

    # Apply Replay Gain
    # Since applying Replay Gain as described requires analysis and adjustment that's often done by players or specific software,
    # and is not directly supported by the pydub or lameenc, this step is a placeholder indicating where that process would integrate.
    # For actual application, you would need to use a library or external tool that supports Replay Gain analysis and tagging,
    # such as `mutagen` for tagging or a command-line tool that can be invoked from Python.
    print("Note: Actual Replay Gain adjustment and tagging is not implemented in this code snippet and requires additional tools.")

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save MP3 files for each stereo mode with normalization and a placeholder for Replay Gain
modes = ['stereo', 'joint_stereo', 'dual_channel', 'mono']
for mode in modes:
    filename = f'./tmp/sine_normalized_replay_gain_{mode}.mp3'
    generate_normalized_sine_wave_mp3_with_replay_gain(mode, filename)
    print(f'Generated {filename}')