import os
from pydub import AudioSegment
from pydub.generators import Sine
import lameenc

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_mp3(bit_rate):
    # Generate a 5-second sine wave tone at 440 Hz (A4)
    tone = Sine(440).to_audio_segment(duration=5000)

    # Convert the audio segment to raw audio data (WAV)
    wave_data = tone.raw_data

    # Setup the encoder with the specified bit rate
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bit_rate)
    encoder.set_in_sample_rate(tone.frame_rate)
    encoder.set_channels(tone.channels)
    encoder.set_quality(2)  # 2 is the highest quality

    # Encode the raw audio data to MP3
    mp3_data = encoder.encode(wave_data)
    mp3_data += encoder.flush()

    # Save the MP3 data to a file
    file_name = f'./tmp/sine_{bit_rate}kbps.mp3'
    with open(file_name, 'wb') as f:
        f.write(mp3_data)

    print(f'Generated MP3 file at {bit_rate} kbps: {file_name}')

# Generate MP3 files with different bit rates
for bit_rate in [128, 192, 320]:
    generate_mp3(bit_rate)