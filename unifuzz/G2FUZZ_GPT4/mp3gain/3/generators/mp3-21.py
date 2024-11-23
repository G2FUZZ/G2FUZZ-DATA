import os
from pydub import AudioSegment
from pydub.generators import Sine
import lameenc

# Function to generate a sine wave with a 3D sound effect and encode it to MP3
def generate_sine_wave_mp3_with_3d_sound(filename, duration_ms=1000, freq=440):
    # Generate stereo sine wave with slightly different frequencies for 3D effect
    left_channel_freq = freq
    right_channel_freq = freq + 5  # Slight frequency variation for 3D effect
    
    left_channel = Sine(left_channel_freq).to_audio_segment(duration=duration_ms)
    right_channel = Sine(right_channel_freq).to_audio_segment(duration=duration_ms)
    stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

    # Apply fading to create a dynamic 3D sound effect (simulating movement)
    stereo_sound = stereo_sound.fade_in(200).fade_out(200)
    
    # Convert to raw audio data
    raw_audio_data = stereo_sound.raw_data
    
    # Encoding settings
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(stereo_sound.frame_rate)
    encoder.set_channels(2)
    encoder.set_quality(2)  # High quality
    
    # Encode to MP3
    mp3_data = encoder.encode(raw_audio_data)
    mp3_data += encoder.flush()
    
    # Save to file
    with open(filename, 'wb') as f:
        f.write(mp3_data)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save MP3 file with 3D Sound feature
filename = './tmp/sine_3D_sound.mp3'
generate_sine_wave_mp3_with_3d_sound(filename)
print(f'Generated {filename}')