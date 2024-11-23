from pydub import AudioSegment
from pydub.generators import Sine
import os

def ensure_dir(dir_path):
    """Ensure directory exists."""
    os.makedirs(dir_path, exist_ok=True)

def generate_tone(frequency, duration, volume):
    """Generate a sine tone with a specific frequency, duration, and volume."""
    return Sine(frequency).to_audio_segment(duration=duration).apply_gain(volume)

def combine_audio_segments(*segments):
    """Combine multiple audio segments sequentially."""
    combined = AudioSegment.empty()
    for segment in segments:
        combined += segment
    return combined

def export_audio(audio_segment, file_path, tags):
    """Export audio segment to a specified path with tags."""
    audio_segment.export(file_path, format="mp3", bitrate="192k", tags=tags)

# Define directories
base_dir = './tmp/complex_structure/'
ensure_dir(base_dir)
tone_dir = os.path.join(base_dir, 'tones/')
silence_dir = os.path.join(base_dir, 'silences/')
ensure_dir(tone_dir)
ensure_dir(silence_dir)

# Generate audio segments
silence_segment = AudioSegment.silent(duration=5000)  # 5 seconds of silence
tone_segment_440hz = generate_tone(frequency=440, duration=3000, volume=-3.0)  # A4 note, 3 seconds, slightly quieter
tone_segment_880hz = generate_tone(frequency=880, duration=3000, volume=0.0)  # A5 note, 3 seconds

# Combine segments in a specific pattern
combined_audio = combine_audio_segments(silence_segment, tone_segment_440hz, silence_segment, tone_segment_880hz)

# Export combined audio to tones directory
combined_audio_path = os.path.join(tone_dir, 'combined_tones_and_silences.mp3')
export_audio(combined_audio, combined_audio_path, tags={"title": "Combined Tones", "artist": "PyDub Generator"})

# Additionally, export individual segments for demonstration
export_audio(silence_segment, os.path.join(silence_dir, 'silence.mp3'), tags={"title": "Silence", "artist": "PyDub Generator"})
export_audio(tone_segment_440hz, os.path.join(tone_dir, 'tone_440hz.mp3'), tags={"title": "Tone 440Hz", "artist": "PyDub Generator"})
export_audio(tone_segment_880hz, os.path.join(tone_dir, 'tone_880hz.mp3'), tags={"title": "Tone 880Hz", "artist": "PyDub Generator"})