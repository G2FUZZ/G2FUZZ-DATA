from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth
import os

def ensure_dir(dir_path):
    """Ensure directory exists."""
    os.makedirs(dir_path, exist_ok=True)

def generate_tone(generator, frequency, duration, volume, channels=1):
    """Generate a tone with a specific frequency, duration, and volume using different waveforms."""
    if generator == 'sine':
        tone = Sine(frequency)
    elif generator == 'square':
        tone = Square(frequency)
    elif generator == 'sawtooth':
        tone = Sawtooth(frequency)
    else:
        raise ValueError("Unsupported generator type. Choose 'sine', 'square', or 'sawtooth'.")
    
    audio_segment = tone.to_audio_segment(duration=duration).apply_gain(volume)
    if channels == 2:
        # Create a stereo effect by delaying one channel slightly
        audio_segment = audio_segment.set_channels(2).pan(-1) + audio_segment.set_channels(2).pan(1).invert_phase()
    return audio_segment

def combine_audio_segments(*segments):
    """Combine multiple audio segments sequentially."""
    combined = AudioSegment.empty()
    for segment in segments:
        combined += segment
    return combined

def export_audio(audio_segment, file_path, tags):
    """Export audio segment to a specified path with tags."""
    audio_segment.export(file_path, format="mp3", bitrate="320k", tags=tags)

# Define directories
base_dir = './tmp/advanced_structure/'
ensure_dir(base_dir)
tone_dir = os.path.join(base_dir, 'tones/')
silence_dir = os.path.join(base_dir, 'silences/')
ensure_dir(tone_dir)
ensure_dir(silence_dir)

# Generate audio segments
silence_segment = AudioSegment.silent(duration=2000)  # 2 seconds of silence
tone_segment_440hz_sine = generate_tone('sine', frequency=440, duration=2000, volume=-3.0, channels=2)  # Stereo sine wave
tone_segment_880hz_square = generate_tone('square', frequency=880, duration=2000, volume=0.0)  # Mono square wave
tone_segment_660hz_sawtooth = generate_tone('sawtooth', frequency=660, duration=2000, volume=-6.0, channels=2)  # Stereo sawtooth wave

# Combine segments in a specific pattern with varying volumes and channels
combined_audio = combine_audio_segments(silence_segment, tone_segment_440hz_sine, silence_segment, tone_segment_880hz_square, silence_segment, tone_segment_660hz_sawtooth)

# Export combined audio to tones directory
combined_audio_path = os.path.join(tone_dir, 'complex_tones_and_silences.mp3')
export_audio(combined_audio, combined_audio_path, tags={"title": "Complex Tones", "artist": "PyDub Generator"})

# Additionally, export individual segments for demonstration
export_audio(silence_segment, os.path.join(silence_dir, 'silence.mp3'), tags={"title": "Silence", "artist": "PyDub Generator"})
export_audio(tone_segment_440hz_sine, os.path.join(tone_dir, 'tone_440hz_sine_stereo.mp3'), tags={"title": "Tone 440Hz Sine Stereo", "artist": "PyDub Generator"})
export_audio(tone_segment_880hz_square, os.path.join(tone_dir, 'tone_880hz_square_mono.mp3'), tags={"title": "Tone 880Hz Square Mono", "artist": "PyDub Generator"})
export_audio(tone_segment_660hz_sawtooth, os.path.join(tone_dir, 'tone_660hz_sawtooth_stereo.mp3'), tags={"title": "Tone 660Hz Sawtooth Stereo", "artist": "PyDub Generator"})