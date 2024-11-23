import os
import soundfile as sf
import numpy as np
from mutagen.mp3 import MP3
from mutagen.id3 import APIC, ID3, PictureType

# Create a mono channel mp3 file with embedded image
mono_data = np.random.randn(44100)  # Generating random mono audio data
image_path = "./path_to_image/image.jpg"  # Path to the image file
audio_path = './tmp/mono_with_image.mp3'
sf.write(audio_path, mono_data, samplerate=44100)

# Check if the image file exists before embedding it
if os.path.exists(image_path):
    # Embedding the image into the mp3 file
    audio_file = MP3(audio_path, ID3=ID3)
    with open(image_path, 'rb') as img:
        audio_file.tags.add(APIC(3, 'image/jpeg', 3, 'Front cover', img.read()))
    audio_file.save()
else:
    print("Image file not found at the specified path.")