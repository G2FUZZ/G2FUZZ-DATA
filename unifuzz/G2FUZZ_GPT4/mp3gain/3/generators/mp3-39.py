import os
from pydub import AudioSegment, silence
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

def generate_complex_sine_wave_mp3(channel_configuration, filename, duration_ms=10000, start_freq=440, end_freq=880, start_vol=-20, end_vol=-3, silence_interval=2000):
    # Initialize an empty AudioSegment for the final mix
    complex_sound = AudioSegment.empty()

    # Calculate the frequency and volume change per step
    steps = 10  # Number of steps in the sweep
    freq_step = (end_freq - start_freq) / steps
    vol_step = (end_vol - start_vol) / steps
    segment_duration = duration_ms // (steps + (steps - 1) // (silence_interval // 1000))  # Adjust the segment duration

    for step in range(steps):
        # Calculate current frequency and volume
        current_freq = start_freq + (freq_step * step)
        current_vol = start_vol + (vol_step * step)
        
        if channel_configuration == "multi_channel":
            # Generate segments for a pseudo multi-channel configuration
            channels = [Sine(current_freq).to_audio_segment(duration=segment_duration).apply_gain(current_vol) for _ in range(6)]
            left_channel_mix = channels[0].overlay(channels[2]).overlay(channels[4])
            right_channel_mix = channels[1].overlay(channels[3]).overlay(channels[5])
            sound_segment = AudioSegment.from_mono_audiosegments(left_channel_mix, right_channel_mix)
        else:
            # Generate stereo segments with varying frequencies and volumes
            left_channel = Sine(current_freq).to_audio_segment(duration=segment_duration).apply_gain(current_vol)
            right_channel = Sine(current_freq).to_audio_segment(duration=segment_duration).apply_gain(current_vol)
            sound_segment = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

        # Normalize the sound segment
        sound_segment = normalize(sound_segment)
        
        # Append the sound segment and a silence segment to the complex sound
        complex_sound += sound_segment
        if step < steps - 1:  # Add silence except after the last segment
            complex_sound += AudioSegment.silent(duration=silence_interval)

    # Convert to raw audio data
    raw_audio_data = complex_sound.raw_data
    
    # Encoding settings
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(192)
    encoder.set_in_sample_rate(complex_sound.frame_rate)
    encoder.set_channels(2)  # Assuming a stereo output
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
    filename = f'./tmp/complex_sine_{config}.mp3'
    generate_complex_sine_wave_mp3(config, filename, duration_ms=10000, start_freq=440, end_freq=880, start_vol=-20, end_vol=-3, silence_interval=2000)
    print(f'Generated {filename}')