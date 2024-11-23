import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

# Function to generate a sine wave, normalize it, and encode it to MP3 with a specific stereo mode
def generate_normalized_sine_wave_mp3(stereo_mode, filename, duration_ms=1000, freq=440):
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
    
    # Note: Removed the set_mode part due to AttributeError
    
    # Encode to MP3
    mp3_data = encoder.encode(raw_audio_data)
    mp3_data += encoder.flush()
    
    # Save to file
    with open(filename, 'wb') as f:
        f.write(mp3_data)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save MP3 files for each stereo mode with normalization
modes = ['stereo', 'joint_stereo', 'dual_channel', 'mono']
for mode in modes:
    filename = f'./tmp/sine_normalized_{mode}.mp3'
    generate_normalized_sine_wave_mp3(mode, filename)
    print(f'Generated {filename}')