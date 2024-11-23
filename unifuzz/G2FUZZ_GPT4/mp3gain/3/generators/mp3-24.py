import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

def generate_normalized_sine_wave_mp3(channel_configuration, filename, duration_ms=1000, freq=440):
    if channel_configuration == "multi_channel":
        # For simplicity, using a 5.1 channel setup as an example of multi-channel audio
        # Note: This workaround will still produce a stereo MP3, not a true multi-channel file.
        # Generating separate sine waves for each channel in a 5.1 setup
        channels = [Sine(freq).to_audio_segment(duration=duration_ms) for _ in range(6)]
        
        # Attempting to combine channels into a stereo mix as a simple workaround
        # This is not a true representation of the original multi-channel intent
        left_channel_mix = channels[0].overlay(channels[2]).overlay(channels[4])  # Combining some channels for left
        right_channel_mix = channels[1].overlay(channels[3]).overlay(channels[5])  # Combining the rest for right
        multi_channel_sound = AudioSegment.from_mono_audiosegments(left_channel_mix, right_channel_mix)
    else:
        # Generate stereo sine wave for other configurations
        left_channel = Sine(freq).to_audio_segment(duration=duration_ms)
        right_channel = Sine(freq).to_audio_segment(duration=duration_ms)
        multi_channel_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
        
        # Normalize the audio to a standard level
        multi_channel_sound = normalize(multi_channel_sound)

    # Convert to raw audio data
    raw_audio_data = multi_channel_sound.raw_data
    
    # Encoding settings
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(multi_channel_sound.frame_rate)
    encoder.set_channels(2)  # Always set to 2 channels as a workaround
    encoder.set_quality(2)  # High quality
    
    # Encode to MP3
    mp3_data = encoder.encode(raw_audio_data)
    mp3_data += encoder.flush()
    
    # Save to file
    with open(filename, 'wb') as f:
        f.write(mp3_data)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save MP3 files for each channel configuration including multi-channel
configurations = ['stereo', 'joint_stereo', 'dual_channel', 'mono', 'multi_channel']
for config in configurations:
    filename = f'./tmp/sine_normalized_{config}.mp3'
    generate_normalized_sine_wave_mp3(config, filename)
    print(f'Generated {filename}')