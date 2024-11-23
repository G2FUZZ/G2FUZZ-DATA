import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

def generate_complex_soundscape_mp3(filename, segments):
    # Initialize an empty AudioSegment for layering sounds
    combined_sound = AudioSegment.silent(duration=0)

    # Generate each segment defined in segments list
    for segment in segments:
        # Extract segment details
        freq, start_ms, duration_ms, channel = segment

        # Generate sine wave for the segment
        sine_wave = Sine(freq).to_audio_segment(duration=duration_ms)

        # Normalize the sine wave
        sine_wave = normalize(sine_wave)

        # Apply stereo effect based on the channel
        if channel == 'left':
            # Create a silent segment with the same length as the sine wave
            right_channel = AudioSegment.silent(duration=len(sine_wave))
            # Combine into a stereo track
            sine_wave = sine_wave.set_channels(2).overlay(right_channel.set_channels(2))
        elif channel == 'right':
            # Create a silent segment with the same length as the sine wave
            left_channel = AudioSegment.silent(duration=len(sine_wave))
            # Combine into a stereo track
            sine_wave = left_channel.set_channels(2).overlay(sine_wave.set_channels(2))
        # For simplicity, no specific handling for multi-channel, defaults to mono

        # Overlay this sine wave on the combined sound at the correct start time
        combined_sound = combined_sound.overlay(sine_wave, position=start_ms)

    # Convert to raw audio data
    raw_audio_data = combined_sound.raw_data
    
    # Encoding settings
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(combined_sound.frame_rate)
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

# Define a complex soundscape with multiple segments
segments = [
    (440, 0, 1000, 'left'),
    (660, 500, 1500, 'right'),
]

# Generate and save the complex soundscape MP3 file
filename = './tmp/complex_soundscape.mp3'
generate_complex_soundscape_mp3(filename, segments)
print(f'Generated {filename}')