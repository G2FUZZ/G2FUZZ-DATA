import os
import numpy as np
from pydub import AudioSegment
import lameenc

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration_seconds=1, sample_rate=44100):
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    # Normalize to 16-bit range
    tone = np.int16(tone * 32767)
    return tone

# Function to save tone to an MP3 file with specified bit rate
def save_tone_as_mp3(filename, tone, sample_rate=44100, bit_rate=128):
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bit_rate)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(1)
    encoder.set_quality(2)  # 2 is the highest quality
    mp3_data = encoder.encode(tone.tobytes())
    mp3_data += encoder.flush()
    
    with open(filename, 'wb') as f:
        f.write(mp3_data)

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sine wave tone
tone = generate_tone()

# Bit rates to generate MP3 files for
bit_rates = [128, 192, 320]

# Generate and save MP3 files for each bit rate
for bit_rate in bit_rates:
    filename = os.path.join(output_dir, f'tone_{bit_rate}kbps.mp3')  # Corrected variable name here
    save_tone_as_mp3(filename, tone, bit_rate=bit_rate)

print(f'MP3 files have been generated at {", ".join(map(str, bit_rates))} kbps bit rates.')