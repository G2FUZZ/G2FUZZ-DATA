import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import lameenc

def generate_enhanced_soundscape_mp3(filename, segments, background_files, fade_effects):
    # Initialize an empty AudioSegment for layering sounds
    combined_sound = AudioSegment.silent(duration=5000)  # Set to the expected total duration

    # Add background sounds from files
    for bg_file, start_ms in background_files:
        try:
            bg_sound = AudioSegment.from_file(bg_file)
            # Optionally, apply normalization to the background sounds
            bg_sound = normalize(bg_sound)
            combined_sound = combined_sound.overlay(bg_sound, position=start_ms)
        except FileNotFoundError as e:
            print(f"Warning: {e}. Skipping background file '{bg_file}'.")

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
            sine_wave = sine_wave.pan(-1)  # Pan fully to the left
        elif channel == 'right':
            sine_wave = sine_wave.pan(1)  # Pan fully to the right

        # Overlay this sine wave on the combined sound at the correct start time
        combined_sound = combined_sound.overlay(sine_wave, position=start_ms)

    # Apply fade in and fade out effects
    for fade in fade_effects:
        if fade['type'] == 'in':
            combined_sound = combined_sound.fade_in(fade['duration'])
        elif fade['type'] == 'out':
            combined_sound = combined_sound.fade_out(fade['duration'])

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

# Define a complex soundscape with multiple segments and background files
segments = [
    (440, 0, 3000, 'left'),
    (660, 1000, 3000, 'right'),
    (880, 2000, 3000, 'both'),
]

background_files = [
    # Ensure these paths point to valid files, or the script will skip them
    ('path_to_background_sound_1.mp3', 0),
    ('path_to_background_sound_2.mp3', 2000),
]

fade_effects = [
    {'type': 'in', 'duration': 1000},
    {'type': 'out', 'duration': 1000},
]

# Generate and save the complex soundscape MP3 file
filename = './tmp/enhanced_complex_soundscape.mp3'
generate_enhanced_soundscape_mp3(filename, segments, background_files, fade_effects)
print(f'Generated {filename}')