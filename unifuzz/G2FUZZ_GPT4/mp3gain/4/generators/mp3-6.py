import os
import numpy as np
import lameenc

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_tone(frequency=440, duration_seconds=1, sample_rate=44100, volume=0.5):
    """
    Generate a sine wave at a specified frequency and duration.
    """
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    # Normalize to 16-bit range
    tone = np.int16(tone * volume * 32767)
    return tone

def save_to_mp3(audio_data, file_path, sample_rate=44100, vbr_quality=4):
    """
    Save the audio data to an MP3 file using VBR encoding.
    """
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(0)  # VBR
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(1)
    encoder.set_quality(vbr_quality)  # VBR quality
    
    mp3_data = encoder.encode(audio_data.tobytes())
    mp3_data += encoder.flush()

    with open(file_path, 'wb') as f:
        f.write(mp3_data)

# Generate a tone
tone = generate_tone()

# Save to MP3 with VBR, ensuring the file path is correctly formed
save_to_mp3(tone, os.path.join(output_dir, 'vbr_tone.mp3'))