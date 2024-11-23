import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave as an example of audio
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return np.sin(2*np.pi*freq*t)

# Parameters for the audio
freq = 440  # Frequency of the sine wave (A4)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Generate a sine wave audio signal
audio = generate_sine_wave(freq, sample_rate, duration)

# Normalize to 16-bit range for WAV format
audio_normalized = np.int16((audio / audio.max()) * 32767)

# Use a temporary directory to first save as WAV (since direct MP3 generation might not be supported)
with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path_high_quality = './tmp/generated_audio_high_quality.mp3'
    mp3_path_low_quality = './tmp/generated_audio_low_quality.mp3'
    mp3_path_progressive = './tmp/generated_audio_progressive.mp3'
    
    # Write the audio data as a WAV file
    wavfile.write(wav_path, sample_rate, audio_normalized)
    
    # Convert WAV to MP3 with Customizable Quality Settings
    sound = AudioSegment.from_wav(wav_path)
    
    # High-quality settings
    bitrate_high = "320k"  # Bitrate as string for high quality
    encoding_quality_high = 2  # Encoding algorithm quality for high quality (0=best, 9=worst, for libmp3lame)
    
    # Low-quality settings for progressive streaming
    bitrate_low = "128k"  # Bitrate as string for low quality
    encoding_quality_low = 5  # Encoding algorithm quality for low quality (0=best, 9=worst, for libmp3lame)
    
    # Export with high-quality settings
    sound.export(mp3_path_high_quality, format="mp3", bitrate=bitrate_high, parameters=["-q:a", str(encoding_quality_high)])
    
    # Export with low-quality settings
    sound.export(mp3_path_low_quality, format="mp3", bitrate=bitrate_low, parameters=["-q:a", str(encoding_quality_low)])
    
    # Progressive Bitrate Streaming
    # Note: This simplistic approach first exports a low-quality version for quick start, followed by the high-quality version.
    # Actual progressive bitrate streaming would require server-side support to deliver audio in chunks of increasing quality.
    sound_low = AudioSegment.from_mp3(mp3_path_low_quality)
    sound_high = AudioSegment.from_mp3(mp3_path_high_quality)
    
    # Creating a progressive mp3 by concatenating a short low-quality segment with the high-quality one
    # This is a simple representation and not an actual streaming solution
    duration_low_quality = 1000  # 1 second of low-quality audio
    progressive_sound = sound_low[:duration_low_quality] + sound_high
    progressive_sound.export(mp3_path_progressive, format="mp3")

print(f"Generated Progressive MP3 saved to: {mp3_path_progressive}")