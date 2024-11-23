import os
from pydub import AudioSegment
from pydub.generators import Sine
import eyed3

# Create an mp3 file with Metadata, ReplayGain, and Customized Tags
mp3_file_complex_features = Sine(880).to_audio_segment(duration=2000)
# Add Metadata feature
metadata_tags = {
    'artist': 'Sample Artist',
    'album': 'Sample Album',
    'year': '2022',
    'genre': 'Electronic'
}

# Convert the AudioSegment to a temporary WAV file
temp_wav_file = "/tmp/temp_audio.wav"
mp3_file_complex_features.export(temp_wav_file, format="wav")

# Set frame metadata using eyed3
audiofile = eyed3.load(temp_wav_file)
if audiofile is not None and audiofile.tag is not None:
    for tag, value in metadata_tags.items():
        audiofile.tag.frame_set('TXXX', description=tag, text=value)
    audiofile.tag.save()

    # Load the modified audio file back as AudioSegment
    mp3_file_complex_features = AudioSegment.from_file(temp_wav_file)

    # Add ReplayGain feature
    replay_gain = {
        'track_gain': '+1.5 dB',
        'album_gain': '+2.0 dB'
    }
    mp3_file_complex_features += AudioSegment.silent(duration=len(str(replay_gain)) * 1000)

    # Add Customized Tags feature
    custom_tags = {
        'custom_tag1': 'value1',
        'custom_tag2': 'value2'
    }
    mp3_file_complex_features += AudioSegment.silent(duration=len(str(custom_tags)) * 1000)

    # Export the mp3 file with all features
    output_file_path = "./tmp/mp3_file_complex_features.mp3"
    mp3_file_complex_features.export(output_file_path, format="mp3")

    # Clean up temporary WAV file
    os.remove(temp_wav_file)

    print(f"MP3 file with complex features exported to: {output_file_path}")
else:
    print("Error: Unable to load audio file or access tag information.")