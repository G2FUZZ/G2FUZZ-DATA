import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TXXX

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with ID3 tags including CBR vs. VBR and Remix Stems features
audio_file = './tmp/sample_extended_remix.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text="Sample Genre"))
audio.add(TXXX(encoding=3, desc="Encoding", text="CBR vs. VBR"))
audio.add(TXXX(encoding=3, desc="Remix Stems", text="Some MP3 files may include separate tracks for remix stems, allowing for creative manipulation of the audio components"))
audio.save(audio_file)

print(f"Generated mp3 file with ID3 tags including CBR vs. VBR and Remix Stems features: {audio_file}")