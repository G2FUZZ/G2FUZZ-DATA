import os
import numpy as np
import lameenc

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_stereo_tone(frequency=440, duration_seconds=1, sample_rate=44100, volume=0.5):
    """
    Generate a stereo sine wave at a specified frequency and duration.
    """
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
    tone_left = np.sin(frequency * 2 * np.pi * t)  # Left channel
    tone_right = np.sin(frequency * 2 * np.pi * t) * 0.5  # Right channel, half the amplitude for demonstration
    
    # Normalize to 16-bit range and interleave left and right channels
    tone_stereo = np.vstack((tone_left, tone_right)).T.flatten()
    tone_stereo = np.int16(tone_stereo * volume * 32767)
    return tone_stereo

def save_to_mp3_with_intensity_stereo(audio_data, file_path, sample_rate=44100, vbr_quality=4):
    """
    Save the audio data to an MP3 file using VBR encoding.
    """
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(0)  # VBR
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(2)  # Stereo
    encoder.set_quality(vbr_quality)  # VBR quality
    # Note: The problematic line has been removed as it's not supported by the encoder object.

    mp3_data = encoder.encode(audio_data.tobytes())
    mp3_data += encoder.flush()

    with open(file_path, 'wb') as f:
        f.write(mp3_data)

# Generate a stereo tone
stereo_tone = generate_stereo_tone()

# Save to MP3, ensuring the file path is correctly formed
save_to_mp3_with_intensity_stereo(stereo_tone, os.path.join(output_dir, 'intensity_stereo_tone.mp3'))