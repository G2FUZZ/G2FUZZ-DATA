from gtts import gTTS
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB, TYER, error
import io

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Texts to convert to speech with different languages
texts = [
    ("English text example for encoding and decoding efficiency.", 'en', "slow"),
    ("Ejemplo de texto en español para eficiencia de codificación y decodificación.", 'es', "fast")
]

for i, (text, lang, speed) in enumerate(texts, start=1):
    # Adjust the speed parameter
    if speed == "slow":
        slow = True
    else:
        slow = False

    # Generate speech
    tts = gTTS(text, lang=lang, slow=slow)

    # Save to a temporary buffer
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)

    mp3_path = f'./tmp/encoding_and_decoding_efficiency_{lang}.mp3'
    with open(mp3_path, 'wb') as f:
        f.write(buf.read())

    # Add ID3 tags to the MP3 file
    audio = MP3(mp3_path)

    # Check if the file has ID3 tag, if not, add one
    if audio.tags is None:
        audio.add_tags()

    # Try to add the cover art
    try:
        with open('cover.png', 'rb') as img:
            audio.tags.add(APIC(mime='image/png', type=3, desc=u'Cover', data=img.read()))
    except FileNotFoundError:
        print("Cover image file 'cover.png' not found. Skipping cover art.")

    # Add other ID3 tags
    audio.tags.add(TIT2(encoding=3, text=u'Encoding and Decoding Efficiency'))
    audio.tags.add(TPE1(encoding=3, text=u'Author Name'))
    audio.tags.add(TRCK(encoding=3, text=str(i)))
    audio.tags.add(TALB(encoding=3, text=u'Album Title'))
    audio.tags.add(TYER(encoding=3, text=u'2023'))

    audio.save()

    print(f"MP3 file with enhanced features has been generated and saved to {mp3_path}")