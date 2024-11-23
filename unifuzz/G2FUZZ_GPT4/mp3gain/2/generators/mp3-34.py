import os
from pydub import AudioSegment
from pydub.generators import Sine
import lameenc

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_complex_mp3(file_name, sequences, bit_rates):
    # Initialize an empty audio segment for assembling our tones
    combined = AudioSegment.empty()
    
    encoder = lameenc.Encoder()
    encoder.set_in_sample_rate(44100)  # Common sample rate for MP3 files
    encoder.set_channels(2)  # 2 Channels for stereo sound
    encoder.set_quality(2)  # High quality

    for sequence, bit_rate in zip(sequences, bit_rates):
        frequency, duration, channel = sequence

        # Generate tone for the specific frequency
        tone = Sine(frequency).to_audio_segment(duration=duration)
        
        # Adjust the tone to the specified channel
        if channel == 'left':
            tone = tone.pan(-1)  # Pan fully to the left
        elif channel == 'right':
            tone = tone.pan(1)  # Pan fully to the right
        
        # Ensure we handle stereo sound
        if combined.channels < tone.channels:
            combined = combined.set_channels(tone.channels)
            
        # Append the tone to our combined segment
        combined += tone

        # Encode the combined segment periodically to free memory for long sequences
        if len(combined) > 5000:  # If combined segment is longer than 5 seconds
            wave_data = combined.raw_data
            encoder.set_bit_rate(bit_rate)
            mp3_data = encoder.encode(wave_data)
            combined = AudioSegment.empty()  # Reset the combined segment for the next iteration

    # Encode any remaining audio
    if len(combined) > 0:
        wave_data = combined.raw_data
        encoder.set_bit_rate(bit_rates[-1])  # Use the last specified bit rate
        mp3_data += encoder.encode(wave_data)
    
    # Finalize encoding
    mp3_data += encoder.flush()

    # Save the MP3 data to a file
    with open(file_name, 'wb') as f:
        f.write(mp3_data)

    print(f'Generated complex MP3 file: {file_name}')

# Define sequences of tones as tuples of (frequency, duration in milliseconds, channel)
# and corresponding bit rates for each segment
sequences = [
    (440, 2000, 'left'),  # A4 tone for 2 seconds in the left channel
    (660, 2000, 'right'),  # E5 tone for 2 seconds in the right channel
    (880, 2000, 'left'),  # A5 tone for 2 seconds in the left channel
    (440, 2000, 'right')  # A4 tone for 2 seconds in the right channel
]
bit_rates = [128, 192, 256, 320]  # Varying bit rates

# Generate the complex MP3 file
generate_complex_mp3('./tmp/complex_tone_sequence.mp3', sequences, bit_rates)