import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with audio codec MP3
with open('./tmp/audio_codec_MP3.flv', 'wb') as file:
    # Write some dummy audio data compressed with MP3 codec
    file.write(b'MP3 compressed audio data')

# Generate FLV files with audio codec AAC
with open('./tmp/audio_codec_AAC.flv', 'wb') as file:
    # Write some dummy audio data compressed with AAC codec
    file.write(b'AAC compressed audio data')