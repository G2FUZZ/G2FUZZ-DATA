from pydub import AudioSegment
import os
import subprocess  # For calling external commands
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an audio segment of silence with a fade-in
silence = AudioSegment.silent(duration=5000)  # 5 seconds of silence
fade_in_silence = silence.fade_in(3000)  # Fade-in effect over the first 3 seconds

# Export the audio segment to a temporary WAV file
temp_wav_path = "./tmp/temp_silent_fadein.wav"
fade_in_silence.export(temp_wav_path, format="wav")

# Path for the final MP3 file
final_mp3_path = "./tmp/silent_mp3_with_features.mp3"

# Use FFmpeg to encode the WAV to MP3 with VBR and 5.1 surround sound
ffmpeg_command = [
    "ffmpeg",
    "-i", temp_wav_path,  # Input file
    "-codec:a", "libmp3lame",  # Use MP3 codec
    "-q:a", "2",  # VBR quality setting, 0 is highest, 9 is lowest quality
    "-ar", "44100",  # Audio sample rate
    "-ac", "6",  # Number of audio channels for 5.1 surround sound
    final_mp3_path  # Output file
]

# Execute the command
try:
    subprocess.run(ffmpeg_command, check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing FFmpeg: {e}")
else:
    # Load the MP3 file to embed metadata
    audio = MP3(final_mp3_path, ID3=ID3)

    # Add metadata
    audio.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/png',  # or 'image/jpeg'
            type=3,  # 3 is for front cover
            desc=u'Cover',
            data=open('./tmp/cover.png', 'rb').read()  # Your album art here
        )
    )
    audio.tags.add(
        TIT2(encoding=3, text=u'Title of the Track')
    )
    audio.tags.add(
        TPE1(encoding=3, text=u'Artist Name')
    )
    audio.tags.add(
        TALB(encoding=3, text=u'Album Name')
    )
    audio.tags.add(
        TRCK(encoding=3, text=u'1')
    )

    audio.save()

    # Clean up temporary WAV file
    os.remove(temp_wav_path)

    print("MP3 file with complex features generated.")