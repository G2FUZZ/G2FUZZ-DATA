import os
from pydub import AudioSegment
from pydub.generators import Sine
import lameenc

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_chord_mp3(chords, bit_rate):
    # Setup the encoder with the specified bit rate
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bit_rate)
    encoder.set_in_sample_rate(44100)  # Assuming a sample rate of 44100 Hz for all chords
    encoder.set_channels(2)  # Assuming stereo audio
    encoder.set_quality(2)  # 2 is the highest quality

    combined_mp3_data = b''

    for chord_freqs in chords:
        # Generate a chord by combining sine waves
        chord = AudioSegment.empty()
        for freq in chord_freqs:
            tone = Sine(freq).to_audio_segment(duration=2000)  # 2-second tone for each frequency
            chord = chord.overlay(tone)  # Overlay tones to create a chord

        # Convert the audio segment to raw audio data (WAV)
        wave_data = chord.raw_data

        # Encode the raw audio data of the chord to MP3
        mp3_data = encoder.encode(wave_data)
        combined_mp3_data += mp3_data
    
    # Flush the encoder to get the last bits of MP3 data
    combined_mp3_data += encoder.flush()

    # Save the combined MP3 data to a file
    file_name = f'./tmp/chord_progression_{bit_rate}kbps.mp3'
    with open(file_name, 'wb') as f:
        f.write(combined_mp3_data)

    print(f'Generated chord progression MP3 file at {bit_rate} kbps: {file_name}')

# Define chord progressions (in Hz)
chord_progressions = [
    [440, 554.37, 659.25],  # A major: A, C#, E
    [392, 493.88, 587.33],  # G major: G, B, D
    [349.23, 440, 523.25],  # F major: F, A, C
    [293.66, 369.99, 440]   # D minor: D, F, A
]

# Generate MP3 files with different bit rates for the chord progression
for bit_rate in [128, 192, 320]:
    generate_chord_mp3(chord_progressions, bit_rate)