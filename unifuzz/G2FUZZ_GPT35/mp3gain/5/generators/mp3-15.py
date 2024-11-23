import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, COMM

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with ID3 tags including ReplayGain feature
audio_file = './tmp/sample_replaygain.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text="Sample Genre"))
audio.add(COMM(encoding=3, desc='ReplayGain', text='ReplayGain: MP3 files can include ReplayGain metadata to normalize playback volume levels'))
audio.save(audio_file)

print(f"Generated mp3 file with ID3 tags and ReplayGain feature: {audio_file}")