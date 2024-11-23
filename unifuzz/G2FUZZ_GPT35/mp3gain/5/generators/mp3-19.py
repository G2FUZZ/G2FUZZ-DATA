import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TXXX

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with ID3 tags including CBR vs. VBR feature and Custom Tags
audio_file_extended = './tmp/sample_extended_custom.mp3'
audio_extended = ID3()
audio_extended.add(TIT2(encoding=3, text="Sample Extended Title"))
audio_extended.add(TPE1(encoding=3, text="Sample Extended Artist"))
audio_extended.add(TALB(encoding=3, text="Sample Extended Album"))
audio_extended.add(TCON(encoding=3, text="Sample Extended Genre"))
audio_extended.add(TXXX(encoding=3, desc="Encoding", text="CBR vs. VBR"))
audio_extended.add(TXXX(encoding=3, desc="Custom Tags", text="Additional metadata beyond standard ID3 tags"))
audio_extended.save(audio_file_extended)

print(f"Generated mp3 file with ID3 tags including CBR vs. VBR feature and Custom Tags: {audio_file_extended}")