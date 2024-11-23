import numpy as np
from pydub import AudioSegment
import os
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB
from mutagen.mp3 import MP3

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_tone(frequency, duration, sample_rate):
    """
    Generate a tone using a sine wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    tone = np.int16(tone * 32767)
    return tone

def save_to_mp3(filename, samples, sample_rate):
    """
    Save the given audio samples as an MP3 file in the ./tmp/ directory.
    """
    audio = AudioSegment(samples.tobytes(), frame_rate=sample_rate, sample_width=samples.dtype.itemsize, channels=1)
    audio.export(filename, format="mp3", bitrate="192k")

def embed_album_art(mp3_filename, album_art_filename):
    """
    Embed album art into an MP3 file, ensuring the file exists.
    """
    if not os.path.exists(album_art_filename):
        print(f"Album art file {album_art_filename} not found. Skipping album art embedding.")
        return

    audio = MP3(mp3_filename, ID3=ID3)

    if audio.tags is None:
        audio.add_tags()

    with open(album_art_filename, 'rb') as img_file:
        album_art_data = img_file.read()

    audio.tags.add(
        APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=u'Cover',
            data=album_art_data
        )
    )

    audio.tags.add(
        TIT2(
            encoding=3,
            text=[u'Example Title']
        )
    )

    audio.tags.add(
        TPE1(
            encoding=3,
            text=[u'Example Artist']
        )
    )

    audio.tags.add(
        TRCK(
            encoding=3,
            text=[u'1']
        )
    )

    audio.tags.add(
        TALB(
            encoding=3,
            text=[u'Example Album']
        )
    )

    audio.save()

# Define the properties of the tone to be generated
frequency = 440
duration = 2
album_art_filename = './tmp/album_art.jpg'

# Sampling rates to be used for the MP3 files
sampling_rates = [44100, 48000]

for sample_rate in sampling_rates:
    samples = generate_tone(frequency, duration, sample_rate)
    filename = f'./tmp/tone_{sample_rate // 1000}kHz.mp3'
    save_to_mp3(filename, samples, sample_rate)
    embed_album_art(filename, album_art_filename)

print("MP3 files with album art have been generated and saved.")